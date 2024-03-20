###################################################################################################################################

#  

###################################################################################################################################


import pyspark
from pyspark import SparkConf, SparkContext
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

spark = cf.get_spark_session("demographic_formatter")

try: 

    ###################################################################################################################################

    # Loading the person table to be converted to the demographic table

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'


    demographic_table_name       = 'Epic_Demographics_*.txt'

    demographic_IN = spark.read.load(input_data_folder_path+demographic_table_name,format="csv", sep="~", inferSchema="false", header="true", quote= '"')



    ###################################################################################################################################

    #Converting the fileds to PCORNet demographic Format

    ###################################################################################################################################

    demographic = demographic_IN.select(
        
                        demographic_IN['patid'].alias('PATID'),
                        cf.format_date_udf(demographic_IN['birth_date']).alias('BIRTH_DATE'),
                        cf.get_time_from_datetime_udf(demographic_IN['birth_time']).alias('BIRTH_TIME'),
                        demographic_IN['sex'].alias('SEX'),
                        demographic_IN['sexual_orientation'].alias('SEXUAL_ORIENTATION'),
                        demographic_IN['gender_identity'].alias('GENDER_IDENTITY'),
                        demographic_IN['hispanic'].alias('HISPANIC'),
                        demographic_IN['race'].alias('RACE'),
                        lit('N').alias('BIOBANK_FLAG'),
                        demographic_IN['pat_pref_language_spoken'].alias('PAT_PREF_LANGUAGE_SPOKEN'),
                        demographic_IN['raw_sex'].alias('RAW_SEX'),
                        demographic_IN['raw_sexual_orientation'].alias('RAW_SEXUAL_ORIENTATION'),
                        demographic_IN['raw_gender_identity'].alias('RAW_GENDER_IDENTITY'),
                        demographic_IN['raw_hispanic'].alias('RAW_HISPANIC'),
                        demographic_IN['raw_race'].alias('RAW_RACE'),
                        demographic_IN['raw_pat_pref_language_spoken'].alias('RAW_PAT_PREF_LANGUAGE_SPOKEN'),
                        demographic_IN['zipcode'].alias('ZIP_CODE'),


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
                            partner = partner_name.lower(),
                            job     = 'demographic_formatter.py' )

    cf.print_with_style(str(e), 'danger red')







