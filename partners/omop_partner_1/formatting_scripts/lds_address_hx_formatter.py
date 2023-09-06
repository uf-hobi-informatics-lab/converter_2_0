###################################################################################################################################

# This script will convert an OMOP lds_address_hx table to a PCORnet format as the lds_address_hx table

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
spark = cf.get_spark_session("lds_address_hx_formatter")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder



try: 

    ###################################################################################################################################

    # Loading the lds_address_hx table to be converted to the lds_address_hx table

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'


    lds_address_hx_table_name         = 'Lds_Address_hx.txt'
    location_table_name               = 'Locations.txt'


    lds_address_hx = spark.read.load(input_data_folder_path+lds_address_hx_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')
    location = spark.read.load(input_data_folder_path+location_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')

    location_data = location.collect()



    city_dict = {row["location_id"]: row["city"] for row in location_data}
    city_dict_udf = udf(lambda city: city_dict.get(city, None), StringType())


    state_dict = {row["location_id"]: row["state"] for row in location_data}
    state_dict_udf = udf(lambda state: state_dict.get(state, None), StringType())


    zip5_dict = {row["location_id"]: row["zip_5"] for row in location_data}
    zip5_dict_udf = udf(lambda zip_5: zip5_dict.get(zip_5, None), StringType())


    zip9_dict = {row["location_id"]: row["zip_9"] for row in location_data}
    zip9_dict_udf = udf(lambda zip_9: zip9_dict.get(zip_9, None), StringType())



    ###################################################################################################################################

    #Converting the fileds to PCORNet lds_address_hx Format

    ###################################################################################################################################

    lds_address_hx = lds_address_hx.select(         lds_address_hx['address_id'].alias("ADDRESSID"),
                                                    lds_address_hx['person_id'].alias("PATID"),
                                                    lds_address_hx['address_use'].alias("ADDRESS_USE"),
                                                    lds_address_hx['address_type'].alias("ADDRESS_TYPE"),
                                                    lds_address_hx['address_preferred'].alias("ADDRESS_PREFERRED"),
                                                    city_dict_udf(col('location_id')).alias("ADDRESS_CITY"), 
                                                    state_dict_udf(col('location_id')).alias("ADDRESS_STATE"),
                                                    lit('').alias("ADDRESS_COUNTY"),
                                                    zip5_dict_udf(col('location_id')).alias("ADDRESS_ZIP5"),
                                                    zip9_dict_udf(col('location_id')).alias("ADDRESS_ZIP9"), 
                                                    lds_address_hx['address_period_start'].alias("ADDRESS_PERIOD_START"),
                                                    lds_address_hx['address_period_end'].alias("ADDRESS_PERIOD_END"),                                          
                                                    
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
                            partner = 'omop_partner_1',
                            job     = 'lds_address_hx_formatter.py' )

    cf.print_with_style(str(e), 'danger red')





