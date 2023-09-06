###################################################################################################################################

# This script will convert an OMOP person table to a PCORnet format as the demographic table

###################################################################################################################################


import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse


cf = CommonFuncitons('omop_partner_1')


#Create SparkSession
spark = cf.get_spark_session("demographic_formatter")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


try:

    ###################################################################################################################################

    # Loading the person table to be converted to the demographic table

    ###################################################################################################################################


    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'


    person_table_name       = 'Person.txt'

    person = spark.read.load(input_data_folder_path+person_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')



    ###################################################################################################################################

    #Converting the fileds to PCORNet demographic Format

    ###################################################################################################################################

    demographic = person.select(                       person['person_id'].alias("PATID"),
                                                    cf.get_date_from_datetime_udf(person['birth_datetime']).alias("BIRTH_DATE"),
                                                    cf.get_time_from_datetime_udf(person['birth_datetime']).alias("BIRTH_TIME"),
                                                    person['gender'].alias("SEX"),
                                                    lit("").alias("SEXUAL_ORIENTATION"),
                                                    person['gender'].alias("GENDER_IDENTITY"),
                                                    person['ethnicity_source_value'].alias("HISPANIC"),
                                                    person['race'].alias("RACE"),
                                                    person['day_of_birth'].alias("BIOBANK_FLAG"),
                                                    person['spoken_language'].alias("PAT_PREF_LANGUAGE_SPOKEN"),
                                                    person['gender_source_value'].alias("RAW_SEX"),
                                                    lit("").alias("RAW_SEXUAL_ORIENTATION"),
                                                    lit("").alias("RAW_GENDER_IDENTITY"),
                                                    person['ethnicity_source_value'].alias("RAW_HISPANIC"),
                                                    person['race_source_value'].alias("RAW_RACE"),
                                                    person['spoken_language_source_value'].alias("RAW_PAT_PREF_LANGUAGE_SPOKEN"),
                                                    lit("").alias("ZIP_CODE"),



                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################



    cf.write_pyspark_output_file(
                        payspark_df = demographic,
                        output_file_name = "formatted_demographic.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'death_formatter.py' )

    cf.print_with_style(str(e), 'danger red')







