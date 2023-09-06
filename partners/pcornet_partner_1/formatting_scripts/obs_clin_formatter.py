###################################################################################################################################

# This script will take in the PCORnet formatted raw OBS_CLIN file, do the necessary transformations, and output the formatted PCORnet OBS_CLIN file

###################################################################################################################################

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import pickle
from pyspark.sql import SparkSession
import argparse


partner_name = 'pcornet_partner_1'

cf =CommonFuncitons(partner_name.upper())

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder

#Create SparkSession
spark = cf.get_spark_session("obs_clin_formatter")

try:
        
    ###################################################################################################################################

    # Loading the observation table to be converted to the obs_clin table

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'


    obs_clin_table_name   = 'Epic_Clinical_*.txt'

    obs_clin_in= spark.read.load(input_data_folder_path+obs_clin_table_name,format="csv", sep="~", inferSchema="true", header="true", quote= '"')

    ###################################################################################################################################

    #Converting the fileds to PCORNet obs_clin Format

    ###################################################################################################################################

    obs_clin = obs_clin_in.select(


                            obs_clin_in['obsclinid'].alias('OBSCLINID'),
                            obs_clin_in['patid'].alias('PATID'),
                            obs_clin_in['encounterid'].alias('ENCOUNTERID'),
                            obs_clin_in['obsclin_providerid'].alias('OBSCLIN_PROVIDERID'),
                            cf.format_date_udf(obs_clin_in['obsclin_start_date']).alias('OBSCLIN_START_DATE'),
                            cf.get_time_from_datetime_udf(obs_clin_in['obsclin_start_time']).alias('OBSCLIN_START_TIME'),
                            cf.format_date_udf(obs_clin_in['obsclin_stop_date']).alias('OBSCLIN_STOP_DATE'),
                            cf.get_time_from_datetime_udf(obs_clin_in['obsclin_stop_time']).alias('OBSCLIN_STOP_TIME'),
                            obs_clin_in['obsclin_type'].alias('OBSCLIN_TYPE'),
                            obs_clin_in['obsclin_code'].alias('OBSCLIN_CODE'),
                            obs_clin_in['obsclin_result_qual'].alias('OBSCLIN_RESULT_QUAL'),
                            obs_clin_in['obsclin_result_text'].alias('OBSCLIN_RESULT_TEXT'),
                            obs_clin_in['obsclin_result_snomed'].alias('OBSCLIN_RESULT_SNOMED'),
                            obs_clin_in['obsclin_result_num'].alias('OBSCLIN_RESULT_NUM'),
                            obs_clin_in['obsclin_result_modifier'].alias('OBSCLIN_RESULT_MODIFIER'),
                            obs_clin_in['obsclin_result_unit'].alias('OBSCLIN_RESULT_UNIT'),
                            obs_clin_in['obsclin_source'].alias('OBSCLIN_SOURCE'),
                            obs_clin_in['obsclin_abn_ind'].alias('OBSCLIN_ABN_IND'),
                            obs_clin_in['raw_obsclin_name'].alias('RAW_OBSCLIN_NAME'),
                            obs_clin_in['raw_obsclin_code'].alias('RAW_OBSCLIN_CODE'),
                            obs_clin_in['raw_obsclin_type'].alias('RAW_OBSCLIN_TYPE'),
                            obs_clin_in['raw_obsclin_result'].alias('RAW_OBSCLIN_RESULT'),
                            obs_clin_in['raw_obsclin_modifier'].alias('RAW_OBSCLIN_MODIFIER'),
                            obs_clin_in['raw_obsclin_unit'].alias('RAW_OBSCLIN_UNIT'),
    )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf =CommonFuncitons('UFH')
    cf.write_pyspark_output_file(
                        payspark_df = obs_clin,
                        output_file_name = "formatted_obs_clin.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'obs_clin_formatter.py' )

    cf.print_with_style(str(e), 'danger red')


