###################################################################################################################################

# This script will take in the PCORnet formatted raw MED_ADMIN file, do the necessary transformations, and output the formatted PCORnet MED_ADMIN file

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
spark = cf.get_spark_session("med_admin_formatter")

try: 

    ###################################################################################################################################

    # Loading the drug_exposure table to be converted to the med_admin table

    ###################################################################################################################################
    input_data_folder_path               = f'/data/{input_data_folder}/'
    # input_data_folder_path               = f'/app/partners/pcornet_partner_1/data/input/{input_data_folder}/'    
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'


    med_admin_table_name   = 'Epic_Medadmin_*.txt'

    med_admin_in = spark.read.load(input_data_folder_path+med_admin_table_name,format="csv", sep="~", inferSchema="false", header="true", quote= '"')

    ###################################################################################################################################

    #Converting the fileds to PCORNet med_admin Format

    ###################################################################################################################################

    med_admin = med_admin_in.select(

                    med_admin_in['medadminid'].alias('MEDADMINID'),
                    med_admin_in['patid'].alias('PATID'),
                    med_admin_in['encounterid'].alias('ENCOUNTERID'),
                    med_admin_in['prescribingid'].alias('PRESCRIBINGID'),
                    med_admin_in['medadmin_providerid'].alias('MEDADMIN_PROVIDERID'),
                    cf.format_date_udf(med_admin_in['medadmin_start_date']).alias('MEDADMIN_START_DATE'),
                    cf.get_time_from_datetime_udf(med_admin_in['medadmin_start_time']).alias('MEDADMIN_START_TIME'),
                    cf.format_date_udf(med_admin_in['medadmin_stop_date']).alias('MEDADMIN_STOP_DATE'),
                    cf.get_time_from_datetime_udf(med_admin_in['medadmin_stop_time']).alias('MEDADMIN_STOP_TIME'),
                    med_admin_in['medadmin_type'].alias('MEDADMIN_TYPE'),
                    med_admin_in['medadmin_code'].alias('MEDADMIN_CODE'),
                    med_admin_in['medadmin_dose_admin'].alias('MEDADMIN_DOSE_ADMIN'),
                    med_admin_in['medadmin_dose_admin_unit'].alias('MEDADMIN_DOSE_ADMIN_UNIT'),
                    med_admin_in['medadmin_route'].alias('MEDADMIN_ROUTE'),
                    lit('OD').alias('MEDADMIN_SOURCE'),
                    med_admin_in['raw_medadmin_med_name'].alias('RAW_MEDADMIN_MED_NAME'),
                    med_admin_in['raw_medadmin_code'].alias('RAW_MEDADMIN_CODE'),
                    med_admin_in['raw_medadmin_dose_admin'].alias('RAW_MEDADMIN_DOSE_ADMIN'),
                    med_admin_in['raw_medadmin_dose_admin_unit'].alias('RAW_MEDADMIN_DOSE_ADMIN_UNIT'),
                    med_admin_in['raw_medadmin_route'].alias('RAW_MEDADMIN_ROUTE'),
    )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = med_admin,
                        output_file_name = "formatted_med_admin.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'med_admin_formatter.py' )

    cf.print_with_style(str(e), 'danger red')





