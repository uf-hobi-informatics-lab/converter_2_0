###################################################################################################################################

# This script will take in the PCORnet formatted raw VITAL file, do the necessary transformations, and output the formatted PCORnet VITAL file

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
spark = cf.get_spark_session("vital_formatter")


try:
        

    ###################################################################################################################################

    # Loading the raw vital table 

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'

    vital_table_name            = 'Epic_Vitals_*.txt'

    vital_in = spark.read.load(input_data_folder_path+vital_table_name,format="csv", sep="~", inferSchema="true", header="true", quote= '"')

    ###################################################################################################################################

    #Converting the fields to PCORNet vital Format

    ###################################################################################################################################
        
    vital = vital_in.select(


                        vital_in['vitalid'].alias('VITALID'),
                        vital_in['patid'].alias('PATID'),
                        vital_in['encounterid'].alias('ENCOUNTERID'),
                        cf.format_date_udf(vital_in['measure_date']).alias('MEASURE_DATE'),
                        cf.get_time_from_datetime_udf(vital_in['measure_time']).alias('MEASURE_TIME'),
                        vital_in['vital_source'].alias('VITAL_SOURCE'),
                        vital_in['ht'].alias('HT'),
                        vital_in['wt'].alias('WT'),
                        vital_in['diastolic'].alias('DIASTOLIC'),
                        vital_in['systolic'].alias('SYSTOLIC'),
                        vital_in['original_bmi'].alias('ORIGINAL_BMI'),
                        vital_in['bp_position'].alias('BP_POSITION'),
                        vital_in['smoking'].alias('SMOKING'),
                        vital_in['tobacco'].alias('TOBACCO'),
                        vital_in['tobacco_type'].alias('TOBACCO_TYPE'),
                        vital_in['raw_diastolic'].alias('RAW_DIASTOLIC'),
                        vital_in['raw_systolic'].alias('RAW_SYSTOLIC'),
                        vital_in['raw_bp_position'].alias('RAW_BP_POSITION'),
                        vital_in['raw_smoking'].alias('RAW_SMOKING'),
                        vital_in['raw_tobacco'].alias('RAW_TOBACCO'),
                        vital_in['raw_tobacco_type'].alias('RAW_TOBACCO_TYPE'),
    )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = vital,
                        output_file_name = "formatted_vital.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()

except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'vital_formatter.py' )

    cf.print_with_style(str(e), 'danger red')
