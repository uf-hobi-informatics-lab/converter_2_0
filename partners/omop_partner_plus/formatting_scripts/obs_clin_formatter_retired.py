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

cf = CommonFuncitons('emy')


#Create SparkSession
spark = cf.get_spark_session("obs_clin_formatter")



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder



def get_time_from_datetime_uab(datetime_str):
        if datetime_str == None or datetime_str =='':
            return None

        return datetime_str[11:16]

get_time_from_datetime_uab_udf = udf(get_time_from_datetime_uab, StringType())


try: 


###################################################################################################################################

# Loading the observation table to be converted to the obs_clin table

###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/emy/data/formatter_output/{input_data_folder}/'
    concept_table_path                   = f'/app/common/omop_cdm/CONCEPT.csv'


    observation_table_name       = 'observation_v7.txt'
    observation_sup_table_name   = 'observation_sup.csv'

    concept       = cf.spark_read(concept_table_path,spark)

    observation_concept = concept.filter(concept.domain_id == 'Observation').withColumnRenamed("concept_code", "observation_concept_code").withColumnRenamed("vocabulary_id", "observation_vocabulary_id")
    unit_concept = concept.filter(concept.domain_id == 'Unit').withColumnRenamed("concept_code", "unit_concept_code")

    observation = spark.read.load(input_data_folder_path+observation_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')
    observation_sup = spark.read.load(input_data_folder_path+observation_sup_table_name,format="csv", sep=",", inferSchema="false", header="true", quote= '"').withColumnRenamed("observation_id", "observation_sup_id")


    filter_values = ["37079395"] # 37079395	LA29742-6	LOINC	Answer	Standard	Valid	Meas Value	LOINC

    filtered_observation = observation.filter(col("observation_type_concept_id").isin(filter_values))


    joined_observation = filtered_observation.join(observation_concept, observation_concept['concept_id']==filtered_observation['observation_concept_id'], how='left').drop("concept_id")\
                                                .join(observation_sup, observation_sup['observation_sup_id']== filtered_observation['observation_id'], how = 'left')\
                                                .join(unit_concept, unit_concept['concept_id']== filtered_observation['unit_concept_id'], how = 'left')





    ###################################################################################################################################

    #Converting the fileds to PCORNet obs_clin Format

    ###################################################################################################################################


    obs_clin = joined_observation.select(           joined_observation['observation_id'].alias("OBSCLINID"),
                                                    joined_observation['person_id'].alias("PATID"),
                                                    joined_observation['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    joined_observation['provider_id'].alias("OBSCLIN_PROVIDERID"),
                                                    cf.format_date_udf(joined_observation['observation_date']).alias("OBSCLIN_START_DATE"),
                                                    cf.format_time_udf(joined_observation['observation_datetime']).alias("OBSCLIN_START_TIME"),
                                                    cf.format_date_udf(joined_observation['observation_date']).alias("OBSCLIN_STOP_DATE"),
                                                    cf.format_time_udf(joined_observation['observation_datetime']).alias("OBSCLIN_STOP_TIME"),                                            
                                                    joined_observation['observation_vocabulary_id'].alias("OBSCLIN_TYPE"),
                                                    joined_observation['observation_concept_code'].alias("OBSCLIN_CODE"),
                                                    joined_observation['qualifier_source_value'].alias("OBSCLIN_RESULT_QUAL"),
                                                    joined_observation['observation_concept_code'].alias("OBSCLIN_RESULT_TEXT"),
                                                    joined_observation['observation_concept_code'].alias("OBSCLIN_RESULT_SNOMED"),
                                                    joined_observation['value_as_number'].alias("OBSCLIN_RESULT_NUM"),
                                                    joined_observation['qualifier_source_value'].alias("OBSCLIN_RESULT_MODIFIER"),
                                                    joined_observation['unit_concept_code'].alias("OBSCLIN_RESULT_UNIT"),
                                                    joined_observation['observation_data_origin'].alias("OBSCLIN_SOURCE"),
                                                    joined_observation['abn_ind'].alias("OBSCLIN_ABN_IND"),
                                                    joined_observation['observation_concept_code'].alias("RAW_OBSCLIN_NAME"),
                                                    joined_observation['observation_concept_code'].alias("RAW_OBSCLIN_CODE"),
                                                    joined_observation['observation_vocabulary_id'].alias("RAW_OBSCLIN_TYPE"),
                                                    concat(col("value_as_string"),lit(' - '), col("value_as_number")).alias("RAW_OBSCLIN_RESULT"),
                                                    joined_observation['qualifier_source_value'].alias("RAW_OBSCLIN_MODIFIER"),
                                                    joined_observation['unit_source_value'].alias("RAW_OBSCLIN_UNIT"),



                                                    
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
                            partner = 'emy',
                            job     = 'obs_clin_formatter.py',
                            text = str(e))






