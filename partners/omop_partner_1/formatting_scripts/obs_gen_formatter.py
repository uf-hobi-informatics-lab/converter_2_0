###################################################################################################################################

# This script will convert an OMOP observation table to a PCORnet format as the obs_gen table

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
spark = cf.get_spark_session("obs_gen_formatter")



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


def get_time_from_datetime_omop_partner_1(datetime_str):
        if datetime_str == None or datetime_str =='':
            return None

        return datetime_str[11:16]

get_time_from_datetime_omop_partner_1_udf = udf(get_time_from_datetime_omop_partner_1, StringType())

try:

    ###################################################################################################################################

    # Loading the observation table to be converted to the obs_gen table

    ###################################################################################################################################
 
    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'


    observation_table_name   = 'observation.csv'

    observation = spark.read.load(input_data_folder_path+observation_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')

    filter_values = ["LOINC"]# Rows where observation_data_origin is in this list will not convert to obsclin
    filtered_observation = observation.filter(~col("observation_code_type").isin(filter_values))




    ###################################################################################################################################

    obs_gen = filtered_observation.select(          filtered_observation['observation_id'].alias("OBSGENID"),
                                                    filtered_observation['person_id'].alias("PATID"),
                                                    filtered_observation['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    filtered_observation['provider_id'].alias("OBSGEN_PROVIDERID"),
                                                    filtered_observation['observation_start_date'].alias("OBSGEN_START_DATE"),
                                                    get_time_from_datetime_omop_partner_1_udf(filtered_observation['observation_start_datetime']).alias("OBSGEN_START_TIME"),
                                                    filtered_observation['observation_end_date'].alias("OBSGEN_STOP_DATE"),
                                                    get_time_from_datetime_omop_partner_1_udf(filtered_observation['observation_end_datetime']).alias("OBSGEN_STOP_TIME"),
                                                    filtered_observation['observation_code_type'].alias("OBSGEN_TYPE"),
                                                    filtered_observation['observation_code'].alias("OBSGEN_CODE"),
                                                    filtered_observation['qualifier'].alias("OBSGEN_RESULT_QUAL"),
                                                    filtered_observation['observation_code'].alias("OBSGEN_RESULT_TEXT"),
                                                    filtered_observation['value_as_number'].alias("OBSGEN_RESULT_NUM"),
                                                    filtered_observation['qualifier'].alias("OBSGEN_RESULT_MODIFIER"),
                                                    filtered_observation['unit'].alias("OBSGEN_RESULT_UNIT"),                                           
                                                    lit('').alias("OBSGEN_TABLE_MODIFIED"),
                                                    lit('').alias("OBSGEN_ID_MODIFIED"),
                                                    filtered_observation['observation_data_origin'].alias("OBSGEN_SOURCE"),
                                                    filtered_observation['abn_ind'].alias("OBSGEN_ABN_IND"),
                                                    filtered_observation['observation_code'].alias("RAW_OBSGEN_NAME"),
                                                    filtered_observation['observation_code'].alias("RAW_OBSGEN_CODE"),
                                                    filtered_observation['observation_code_type'].alias("RAW_OBSGEN_TYPE"),
                                                    concat(col("value_as_string"),lit(' - '), col("value_as_number")).alias("RAW_OBSGEN_RESULT"),
                                                    filtered_observation['unit_source_value'].alias("RAW_OBSGEN_UNIT"),



                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = obs_gen,
                        output_file_name = "formatted_obs_gen.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'obs_gen_formatter.py' )

    cf.print_with_style(str(e), 'danger red')









