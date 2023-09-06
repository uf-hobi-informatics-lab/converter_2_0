###################################################################################################################################

# This script will take in the PCORnet formatted raw LDS_ADDRESS_HISTORY file, do the necessary transformations, and output the formatted PCORnet LDS_ADDRESS_HISTORY file

###################################################################################################################################

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse


partner_name = 'pcornet_partner_1'

cf =CommonFuncitons(partner_name.upper())

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder

#Create SparkSession
spark = cf.get_spark_session("lds_address_hx_formatter")

try: 

    ###################################################################################################################################

    # Loading the lds_address_hx table 

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'


    lds_address_hx_table_name         = 'Epic_Address_*.txt'


    lds_address_hx_in = spark.read.load(input_data_folder_path+lds_address_hx_table_name,format="csv", sep="~", inferSchema="true", header="true", quote= '"')

    ###################################################################################################################################

    #Converting the fileds to PCORNet lds_address_hx Format

    ###################################################################################################################################

    lds_address_hx = lds_address_hx_in.select(
        lds_address_hx_in['addressid'].alias('ADDRESSID'),
        lds_address_hx_in['patid'].alias('PATID'),
        lds_address_hx_in['address_use'].alias('ADDRESS_USE'),
        lds_address_hx_in['address_type'].alias('ADDRESS_TYPE'),
        lds_address_hx_in['address_preferred'].alias('ADDRESS_PREFERRED'),
        lds_address_hx_in['address_city'].alias('ADDRESS_CITY'),
        lds_address_hx_in['address_state'].alias('ADDRESS_STATE'),
        lds_address_hx_in['address_zip5'].alias('ADDRESS_ZIP5'),
        lds_address_hx_in['address_zip9'].alias('ADDRESS_ZIP9'),
        cf.format_date_udf(lds_address_hx_in['address_period_start']).alias('ADDRESS_PERIOD_START'),
        cf.format_date_udf(lds_address_hx_in['adress_period_end']).alias('ADDRESS_PERIOD_END')
    )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = lds_address_hx,
                        output_file_name = "formatted_lds_address_hx.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()




except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'lds_address_hx_formatter.py' )

    cf.print_with_style(str(e), 'danger red')





