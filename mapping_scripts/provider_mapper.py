###################################################################################################################################
# This script will map a PCORNet provider table 
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
spark = cf.get_spark_session("provider_mapper") 


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


        unmapped_provider = spark.read.option("inferSchema", "false").load(formatted_data_folder_path+"formatted_provider.csv",format="csv", sep="\t", inferSchema="true", header="true",  quote= '"')



    ###################################################################################################################################
    # create the mapping from the dictionaries
    ###################################################################################################################################
        mapping_provider_sex_dict = create_map([lit(x) for x in chain(*partner_dictionaries.provider_provider_sex_dict.items())])
        mapping_provider_specialty_primary_dict = create_map([lit(x) for x in chain(*partner_dictionaries.provider_provider_specialty_primary_dict.items())])
        mapping_provider_npi_flag_dict = create_map([lit(x) for x in chain(*partner_dictionaries.provider_provider_npi_flag_dict.items())])



    ###################################################################################################################################
    # Apply the mappings dictionaries and the common function on the fields of the unmmaped encoutner table
    ###################################################################################################################################


        provider = unmapped_provider.select(              
            
                                    cf.encrypt_id_udf(unmapped_provider['PROVIDERID']).alias("PROVIDERID"),
                                    mapping_provider_sex_dict[upper(col('PROVIDER_SEX'))].alias("PROVIDER_SEX"),
                                    mapping_provider_specialty_primary_dict[upper(col('PROVIDER_SPECIALTY_PRIMARY'))].alias("PROVIDER_SPECIALTY_PRIMARY"),
                                    unmapped_provider['PROVIDER_NPI'].alias("PROVIDER_NPI"),
                                    mapping_provider_npi_flag_dict[upper(col('PROVIDER_NPI_FLAG'))].alias("PROVIDER_NPI_FLAG"),
                                    unmapped_provider['RAW_PROVIDER_SPECIALTY_PRIMARY'].alias("RAW_PROVIDER_SPECIALTY_PRIMARY"),
                                    cf.get_current_time_udf().alias("UPDATED"),
                                    lit(input_partner.upper()).alias("SOURCE"),
                                    unmapped_provider['PROVIDERID'].alias("JOIN_FIELD"),

                                                            )

    ###################################################################################################################################
    # Create the output file
    ###################################################################################################################################

        provider_with_additional_fileds = cf.append_additional_fields(
            mapped_df = provider,
            file_name = "formatted_provider.csv",
            formatted_data_folder_path = formatted_data_folder_path,
            join_field = "PROVIDERID",
            spark = spark)


        cf.write_pyspark_output_file(
                        payspark_df = provider_with_additional_fileds,
                        output_file_name = "mapped_provider.csv",
                        output_data_folder_path= mapped_data_folder_path)


        spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = input_partner,
                            job     = 'provider_mapper.py' )

    cf.print_with_style(str(e), 'danger red')