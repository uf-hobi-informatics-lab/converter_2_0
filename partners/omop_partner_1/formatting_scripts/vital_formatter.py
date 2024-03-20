###################################################################################################################################

# This script will convert an OMOP observation table to a PCORnet format as the vital table

###################################################################################################################################

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse


cf = CommonFuncitons('omop_partner_1')

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


#Create SparkSession
spark = SparkSession.builder.master("spark://master:7077").appName("vital_formatter").getOrCreate()
#spark://master:7077


###################################################################################################################################

# Loading the observation table to be converted to the vital table

###################################################################################################################################

input_data_folder_path               = '/app/partners/omop_partner_1/data/input/'+input_data_folder+'/'
formatter_output_data_folder_path    = '/app/partners/omop_partner_1/data/formatter_output/'+ input_data_folder+'/'

observation_table_name            = 'Observation.txt'

observation = spark.read.load(input_data_folder_path+observation_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')

ht_codes = ['89269-5', '3137-7', '91370-7', 'LP415671-9', '92999-2', 'LP415672-7', '8307-1', '8308-9', '8302-2', '8306-3', '8305-5', 'LP416419-2', '8301-4', '8303-0', 'LP64598-3', '3138-5']

wt_codes = ['11727-5', '11728-3', '11729-1', '11730-9', '11731-7', '11732-5', '11733-3', '11734-1', '11735-8', '11736-6', '11737-4', '11738-2', '11739-0', '11740-8', '11741-6', '11742-4', '11743-2', '11744-0', 
            '11745-7', '11746-5', '11747-3', '11748-1', '11749-9','11750-7', '11751-5', '11752-3', '11753-1', '11754-9', '11755-6', '11756-4', '11757-2', '11758-0', '11759-8', '11760-6', '11761-4', '11762-2',  
            '11763-0', '11764-8', '11765-5', '18690-8', '18833-4', '29463-7', '3141-9', '3142-7', '33139-7', '33140-5', '33141-3', '33142-1', '33143-9', '33144-7', '33162-9', '33163-7', '52416-5', '56056-5',   
            '56092-0', '56093-8', '57067-1', '58229-6', '69460-4', '69461-2', '73965-6', '75292-3', '79348-9', '8335-2', '8336-0', '8338-6', '8339-4', '8340-2', '8341-0', '8342-8', '8343-6','8344-4', '8345-1', 
            '8346-9', '8347-7', '8348-5', '8349-3', '8350-1', '8351-9', '89087-1', 'LP415674-3', 'LP415675-0', 'LP415676-8', 'LP416157-8', 'LP416420-0', 'LP416421-8', 'LP65139-5']

smoking_tobacco_codes = ['110483000', '26663004', '39789004', '428061000124105', '428081000124100', '66562002', '702979003', '81703003', '84498003']

diastolic_codes = ['8455-8','8454-1','8453-3', '8462-4']

systolic_codes = ['8461-6','8460-8','8459-0','8480-6']

bmi_codes = ['39156-5', '59574-4', 'Z68.53', 'Z68.52', 'Z68.54', 'Z68.51']

filter_values_codes = ht_codes + wt_codes + bmi_codes + smoking_tobacco_codes + diastolic_codes + systolic_codes

filtered_observation = observation.filter(trim(col("observation_code")).isin(filter_values_codes))

# Create a new column for each category based on the observation_code

filtered_observation = filtered_observation.withColumn('HT', when(col('observation_code').isin(ht_codes), col('value_as_string')).otherwise(None))
filtered_observation = filtered_observation.withColumn('WT', when(col('observation_code').isin(wt_codes), col('value_as_string')).otherwise(None))
filtered_observation = filtered_observation.withColumn('BMI', when(col('observation_code').isin(bmi_codes), col('value_as_string')).otherwise(None))
filtered_observation = filtered_observation.withColumn('SMOKING', when(col('observation_code').isin(smoking_tobacco_codes), col('value_as_string')).otherwise(None))
filtered_observation = filtered_observation.withColumn('TOBACCO', when(col('observation_code').isin(smoking_tobacco_codes), col('value_as_string')).otherwise(None))
filtered_observation = filtered_observation.withColumn('DIASTOLIC', when(col('observation_code').isin(diastolic_codes), col('value_as_string')).otherwise(None))
filtered_observation = filtered_observation.withColumn('SYSTOLIC', when(col('observation_code').isin(systolic_codes), col('value_as_string')).otherwise(None))

###################################################################################################################################

#Converting the fileds to PCORNet vital Format

###################################################################################################################################

vital_uncombined = filtered_observation.select(    filtered_observation['observation_id'].alias("VITALID"),
                                                   filtered_observation['person_id'].alias("PATID"),
                                                   filtered_observation['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                   filtered_observation['observation_date'].alias("MEASURE_DATE"),
                                                   cf.get_time_from_datetime_udf(observation['observation_datetime']).alias("MEASURE_TIME"),
                                                   filtered_observation['observation_data_origin'].alias("VITAL_SOURCE"),
                                                   filtered_observation['HT'].alias("HT"),
                                                   filtered_observation['WT'].alias("WT"),
                                                   filtered_observation['DIASTOLIC'].alias("DIASTOLIC"),
                                                   filtered_observation['SYSTOLIC'].alias("SYSTOLIC"),
                                                   filtered_observation['BMI'].alias("ORIGINAL_BMI"),
                                                   lit('').alias("BP_POSITION"),
                                                   filtered_observation['SMOKING'].alias("SMOKING"),
                                                   filtered_observation['TOBACCO'].alias("TOBACCO"),
                                                   lit('').alias("TOBACCO_TYPE"),
                                                   filtered_observation['DIASTOLIC'].alias("RAW_DIASTOLIC"),
                                                   filtered_observation['SYSTOLIC'].alias("RAW_SYSTOLIC"),
                                                   lit('').alias("RAW_BP_POSITION"),
                                                   filtered_observation['SMOKING'].alias("RAW_SMOKING"),
                                                   filtered_observation['TOBACCO'].alias("RAW_TOBACCO"),
                                                   lit('').alias("RAW_TOBACCO_TYPE"),
                                                )


# Columns used to group the data
key_columns = ["ENCOUNTERID", "PATID"]

# Columns to aggregate
columns_to_aggregate = [col for col in vital_uncombined.columns if col not in key_columns]

# Create aggregation expressions
aggregation_expr = [first(when(col(column_name) != "", col(column_name)), ignorenulls =True).alias(column_name) 
                    for column_name in columns_to_aggregate]

# Group and aggregate
vital = vital_uncombined.groupBy(*key_columns).agg(*aggregation_expr)


###################################################################################################################################

# Create the output file

###################################################################################################################################

cf.write_pyspark_output_file(
                    payspark_df = vital,
                    output_file_name = "formatted_vital.csv",
                    output_data_folder_path= formatter_output_data_folder_path)

spark.stop()