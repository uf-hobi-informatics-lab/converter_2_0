###################################################################################################################################

# This script will convert an OMOP observation table to a PCORnet format as the obs_clin table

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

cf = CommonFuncitons('omop_partner_1')

#Create SparkSession
spark = cf.get_spark_session("obs_clin_formatter")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder



try:
    


    ###################################################################################################################################

    # Loading the observation table to be converted to the obs_clin table

    ###################################################################################################################################
    
    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'



    observation_table_name   = 'Observation.txt'

    observation = spark.read.load(input_data_folder_path+observation_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')

    filter_values = ["Observation from Measurement", "Observation from measurement"] # Only rows where observation_data_origin is in this list will convert to obsclin
    filtered_observation = observation.filter(col("observation_data_origin").isin(filter_values))







    ###################################################################################################################################

    #Converting the fileds to PCORNet obs_clin Format

    ###################################################################################################################################

    obs_clin = filtered_observation.select(         filtered_observation['observation_id'].alias("OBSCLINID"),
                                                    filtered_observation['person_id'].alias("PATID"),
                                                    filtered_observation['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    filtered_observation['provider_id'].alias("OBSCLIN_PROVIDERID"),
                                                    filtered_observation['observation_date'].alias("OBSCLIN_START_DATE"),
                                                    cf.get_time_from_datetime_udf(filtered_observation['observation_datetime']).alias("OBSCLIN_START_TIME"),
                                                    lit('').alias("OBSCLIN_STOP_DATE"),
                                                    lit('').alias("OBSCLIN_STOP_TIME"),
                                                    filtered_observation['observation_code_type'].alias("OBSCLIN_TYPE"),
                                                    filtered_observation['observation_code'].alias("OBSCLIN_CODE"),
                                                    filtered_observation['qualifier'].alias("OBSCLIN_RESULT_QUAL"),
                                                    filtered_observation['observation_code'].alias("OBSCLIN_RESULT_TEXT"),
                                                    filtered_observation['observation_code'].alias("OBSCLIN_RESULT_SNOMED"),
                                                    filtered_observation['value_as_number'].alias("OBSCLIN_RESULT_NUM"),
                                                    filtered_observation['qualifier'].alias("OBSCLIN_RESULT_MODIFIER"),
                                                    filtered_observation['unit'].alias("OBSCLIN_RESULT_UNIT"),
                                                    filtered_observation['observation_data_origin'].alias("OBSCLIN_SOURCE"),
                                                    lit('').alias("OBSCLIN_ABN_IND"),
                                                    filtered_observation['observation_code'].alias("RAW_OBSCLIN_NAME"),
                                                    filtered_observation['observation_code'].alias("RAW_OBSCLIN_CODE"),
                                                    filtered_observation['observation_code_type'].alias("RAW_OBSCLIN_TYPE"),
                                                    concat(col("value_as_string"),lit(' - '), col("value_as_number")).alias("RAW_OBSCLIN_RESULT"),
                                                    filtered_observation['qualifier_source_value'].alias("RAW_OBSCLIN_MODIFIER"),
                                                    filtered_observation['unit_source_value'].alias("RAW_OBSCLIN_UNIT"),



                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = obs_clin,
                        output_file_name = "formatted_obs_clin.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'obs_clin_formatter.py' )

    cf.print_with_style(str(e), 'danger red')






