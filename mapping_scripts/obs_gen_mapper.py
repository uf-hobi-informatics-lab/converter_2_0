###################################################################################################################################
# This script will map a PCORNet obs_gen table 
###################################################################################################################################

 
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import importlib
import sys
# from partners import partners_list
from itertools import chain
import argparse



###################################################################################################################################
# parsing the input arguments to select the partner name
###################################################################################################################################


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--partner")
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_partner = args.partner.lower()
input_data_folder = args.data_folder


cf =CommonFuncitons(input_partner)

# spin the pyspak cluster and
spark = cf.get_spark_session("obs_gen_mapper") 

try:

    ###################################################################################################################################
    # Test if the partner name is valid or not
    ###################################################################################################################################


    if  not cf.valid_partner_name(input_partner):

        print("Error: Unrecognized partner "+input_partner+" !!!!!")
        sys.exit()

    else:



    ###################################################################################################################################
    # Load the config file for the selected parnter
    ###################################################################################################################################

        partner_dictionaries_path = "partners."+input_partner+".dictionaries"
        partner_dictionaries = importlib.import_module(partner_dictionaries_path)

                
        formatted_data_folder_path = '/app/partners/'+input_partner.lower()+'/data/formatter_output/'+ input_data_folder+'/'
        mapped_data_folder_path    = '/app/partners/'+input_partner.lower()+'/data/mapper_output/'+ input_data_folder+'/'



    ###################################################################################################################################
    # Loading the unmapped enctounter table
    ###################################################################################################################################



        unmapped_obs_gen = spark.read.option("inferSchema", "false").load(formatted_data_folder_path+"formatted_obs_gen.csv",format="csv", sep="\t", inferSchema="true", header="true",  quote= '"')



    ###################################################################################################################################
    # create the mapping from the dictionaries
    ###################################################################################################################################
        mapping_obsgen_type_dict = create_map([lit(x) for x in chain(*partner_dictionaries.obs_gen_obsgen_type_dict.items())])
        mapping_obsgen_result_qual_dict = create_map([lit(x) for x in chain(*partner_dictionaries.obs_gen_result_qual_dict.items())])
        mapping_obsgen_result_modifier_dict = create_map([lit(x) for x in chain(*partner_dictionaries.obs_gen_result_modifier_dict.items())])
        mapping_obsgen_result_unit_dict = create_map([lit(x) for x in chain(*partner_dictionaries.obs_gen_result_unit_dict.items())])
        mapping_obsgen_source_dict = create_map([lit(x) for x in chain(*partner_dictionaries.obs_gen_obsgen_source_dict.items())])




    ###################################################################################################################################
    # Apply the mappings dictionaries and the common function on the fields of the unmmaped encoutner table
    ###################################################################################################################################


        obs_gen = unmapped_obs_gen.select(              
            
            
                                    cf.encrypt_id_udf(unmapped_obs_gen['OBSGENID']).alias("OBSGENID"),
                                    cf.encrypt_id_udf(unmapped_obs_gen['PATID']).alias("PATID"),
                                    cf.encrypt_id_udf(unmapped_obs_gen['ENCOUNTERID']).alias("ENCOUNTERID"),
                                    cf.encrypt_id_udf(unmapped_obs_gen['OBSGEN_PROVIDERID']).alias("OBSGEN_PROVIDERID"),
                                    cf.get_date_from_datetime_udf(unmapped_obs_gen['OBSGEN_START_DATE']).alias("OBSGEN_START_DATE"),
                                    cf.get_time_from_datetime_udf(unmapped_obs_gen['OBSGEN_START_TIME']).alias("OBSGEN_START_TIME"),
                                    cf.get_date_from_datetime_udf(unmapped_obs_gen['OBSGEN_STOP_DATE']).alias("OBSGEN_STOP_DATE"),
                                    cf.get_time_from_datetime_udf(unmapped_obs_gen['OBSGEN_STOP_TIME']).alias("OBSGEN_STOP_TIME"),
                                    mapping_obsgen_type_dict[upper(col("OBSGEN_TYPE"))].alias("OBSGEN_TYPE"),
                                    unmapped_obs_gen['OBSGEN_CODE'].alias("OBSGEN_CODE"),
                                    mapping_obsgen_result_qual_dict[upper(col("OBSGEN_RESULT_QUAL"))].alias("OBSGEN_RESULT_QUAL"),
                                    unmapped_obs_gen['OBSGEN_RESULT_TEXT'].alias("OBSGEN_RESULT_TEXT"),
                                    unmapped_obs_gen['OBSGEN_RESULT_NUM'].alias("OBSGEN_RESULT_NUM"),
                                    mapping_obsgen_result_modifier_dict[upper(col("OBSGEN_RESULT_MODIFIER"))].alias("OBSGEN_RESULT_MODIFIER"),
                                    mapping_obsgen_result_unit_dict[upper(col("OBSGEN_RESULT_UNIT"))].alias("OBSGEN_RESULT_UNIT"),
                                    unmapped_obs_gen['OBSGEN_TABLE_MODIFIED'].alias("OBSGEN_TABLE_MODIFIED"),
                                    unmapped_obs_gen['OBSGEN_ID_MODIFIED'].alias("OBSGEN_ID_MODIFIED"),                             
                                    mapping_obsgen_source_dict[upper(col("OBSGEN_SOURCE"))].alias("OBSGEN_SOURCE"),
                                    unmapped_obs_gen['RAW_OBSGEN_NAME'].alias("RAW_OBSGEN_NAME"),
                                    unmapped_obs_gen['RAW_OBSGEN_CODE'].alias("RAW_OBSGEN_CODE"),
                                    unmapped_obs_gen['RAW_OBSGEN_TYPE'].alias("RAW_OBSGEN_TYPE"),
                                    unmapped_obs_gen['RAW_OBSGEN_RESULT'].alias("RAW_OBSGEN_RESULT"),
                                    unmapped_obs_gen['RAW_OBSGEN_UNIT'].alias("RAW_OBSGEN_UNIT"),
                                    cf.get_current_time_udf().alias("UPDATED"),
                                    lit(input_partner.upper()).alias("SOURCE"),
                                    unmapped_obs_gen['OBSGENID'].alias("JOIN_FIELD"),


                                                            )

    ###################################################################################################################################
    # Create the output file
    ###################################################################################################################################
        obs_gen_with_additional_fileds = cf.append_additional_fields(
            mapped_df = obs_gen,
            file_name = "formatted_obs_gen.csv",
            formatted_data_folder_path = formatted_data_folder_path,
            join_field = "OBSGENID",
            spark = spark)


        cf.write_pyspark_output_file(
                        payspark_df = obs_gen_with_additional_fileds,
                        output_file_name = "mapped_obs_gen.csv",
                        output_data_folder_path= mapped_data_folder_path)

        spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = input_partner,
                            job     = 'obs_gen_mapper.py' )

    cf.print_with_style(str(e), 'danger red')