###################################################################################################################################

# This script will convert an OMOP omop_provider table to a PCORnet format as the pcornet_provider table

###################################################################################################################################


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse


cf = CommonFuncitons('omop_partner_1')

#Create SparkSession
spark = cf.get_spark_session("pcornet_provider_formatter")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder

try :




    ###################################################################################################################################

    # Loading the omop_provider table to be converted to the pcornet_provider table
    # loading the care_site, location, and visit_payer as they are been used to retrive some data for the mapping

    ###################################################################################################################################


    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'


    omop_provider_table_name       = 'Providers.txt'

    omop_provider = spark.read.load(input_data_folder_path+omop_provider_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')

    ###################################################################################################################################

    #Converting the fileds to PCORNet pcornet_provider Format

    ###################################################################################################################################

    def get_provider_npi_flag(npi):
        try:

            if len(npi)== 10 and npi.isnumeric():
                return "Y"
            else:
                return "N"
        except:
            return "N"


    get_provider_npi_flag_udf = udf(get_provider_npi_flag, StringType())

    ###################################################################################################################################

    #Converting the fileds to PCORNet pcornet_provider Format

    ###################################################################################################################################

    pcornet_provider = omop_provider.select(        omop_provider['provider_id'].alias("PROVIDERID"),
                                                    omop_provider['gender'].alias("PROVIDER_SEX"),
                                                    omop_provider['provider_specialty_source_value'].alias("PROVIDER_SPECIALTY_PRIMARY"),
                                                    omop_provider['npi'].alias("PROVIDER_NPI"),
                                                    get_provider_npi_flag_udf(omop_provider['npi']).alias("PROVIDER_NPI_FLAG"),
                                                    omop_provider['provider_specialty_source_value'].alias("RAW_PROVIDER_SPECIALTY_PRIMARY"),
                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################


    cf.write_pyspark_output_file(
                        payspark_df = pcornet_provider,
                        output_file_name = "formatted_provider.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'provider_formatter.py' )

    cf.print_with_style(str(e), 'danger red')















