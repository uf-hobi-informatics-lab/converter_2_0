###################################################################################################################################
# This script will map a PCORNet condition table 
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
spark = cf.get_spark_session("condition_mapper")


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


        unmapped_condition = spark.read.option("inferSchema", "false").load(formatted_data_folder_path+"formatted_condition.csv",format="csv", sep="\t", inferSchema="true", header="true",  quote= '"')



    ###################################################################################################################################
    # create the mapping from the dictionaries
    ###################################################################################################################################
        mapping_condition_status_dict = create_map([lit(x) for x in chain(*partner_dictionaries.condition_condition_status_dict.items())])
        mapping_condition_type_dict = create_map([lit(x) for x in chain(*partner_dictionaries.condition_condition_type_dict.items())])
        mapping_condition_source_dict = create_map([lit(x) for x in chain(*partner_dictionaries.condition_condition_source_dict.items())])



    ###################################################################################################################################
    # Apply the mappings dictionaries and the common function on the fields of the unmmaped encoutner table
    ###################################################################################################################################


        condition = unmapped_condition.select(              
            
            
                                    cf.encrypt_id_udf(unmapped_condition['CONDITIONID']).alias("CONDITIONID"),
                                    cf.encrypt_id_udf(unmapped_condition['PATID']).alias("PATID"),
                                    cf.encrypt_id_udf(unmapped_condition['ENCOUNTERID']).alias("ENCOUNTERID"),
                                    cf.get_date_from_datetime_udf(unmapped_condition['REPORT_DATE']).alias("REPORT_DATE"),
                                    cf.get_date_from_datetime_udf(unmapped_condition['RESOLVE_DATE']).alias("RESOLVE_DATE"),
                                    cf.get_date_from_datetime_udf(unmapped_condition['ONSET_DATE']).alias("ONSET_DATE"),
                                    mapping_condition_status_dict[upper(col("CONDITION_STATUS"))].alias("CONDITION_STATUS"),
                                    unmapped_condition['CONDITION'].alias("CONDITION"),
                                    mapping_condition_type_dict[upper(col("CONDITION_TYPE"))].alias("CONDITION_TYPE"),
                                    mapping_condition_source_dict[upper(col("CONDITION_SOURCE"))].alias("CONDITION_SOURCE"),
                                    unmapped_condition['RAW_CONDITION_STATUS'].alias("RAW_CONDITION_STATUS"),
                                    unmapped_condition['RAW_CONDITION'].alias("RAW_CONDITION"),
                                    unmapped_condition['RAW_CONDITION_TYPE'].alias("RAW_CONDITION_TYPE"),
                                    unmapped_condition['RAW_CONDITION_SOURCE'].alias("RAW_CONDITION_SOURCE"),
                                    cf.get_current_time_udf().alias("UPDATED"),
                                    lit(input_partner.upper()).alias("SOURCE"),
                                    unmapped_condition['CONDITIONID'].alias("JOIN_FIELD"),
                                                            )

    ###################################################################################################################################
    # Create the output file
    ###################################################################################################################################
        condition_with_additional_fileds = cf.append_additional_fields(
            mapped_df = condition,
            file_name = "formatted_condition.csv",
            formatted_data_folder_path = formatted_data_folder_path,
            join_field = "CONDITIONID",
            spark = spark)

        cf.write_pyspark_output_file(
                        payspark_df = condition_with_additional_fileds,
                        output_file_name = "mapped_condition.csv",
                        output_data_folder_path= mapped_data_folder_path)


        spark.stop()

except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = input_partner,
                            job     = 'condition_mapper.py' )

    cf.print_with_style(str(e), 'danger red')