###
# Stubbed out formatter template
###


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

<<<<<<< HEAD
partner_name = 'partner_name'
cf = CommonFuncitons(partner_name.upper())
=======

cf = CommonFuncitons('PartnerCode')
>>>>>>> origin/docker_container_alib

## Argument to take in a folder name to run through all files in that folder of the same type
## Can be left blank for individual files
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


#Create SparkSession

spark = cf.get_spark_session("FileName_formatter")
#spark://master:7077


###################################################################################################################################

# Loading the person table to be converted to the demographic table

###################################################################################################################################

input_data_folder_path               = '/data/'+input_data_folder+'/'
formatter_output_data_folder_path    = '/app/partners/PartnerCode/data/formatter_output/'+ input_data_folder+'/'

## Using person since partner is submitting OMOP data, can also use wildcards for multiple files with the same name
FileName_table_name       = 'File*.txt'

<<<<<<< HEAD
  FileName_table = spark.read.load(input_data_folder_path+person_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')
=======
FileName_table = spark.read.load(input_data_folder_path+person_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')
>>>>>>> origin/docker_container_alib

###################################################################################################################################
# Insert file type specific functions below, may not be needed for each partner
###################################################################################################################################

###################################################################################################################################

#Converting the fileds to PCORNet output Format 
#Example of few columns from person table to demographic 

###################################################################################################################################

<<<<<<< HEAD
  OutputFileName = FileName_table.select(            
                                         FileName_table['person_id'].alias("PATID"), #renaming the input column person_id to the output name PATID
                                                     cf.get_date_from_datetime_udf(FileName_table['birth_datetime']).alias("BIRTH_DATE"), # Using common function to get date and then rename column
                                                     ...
                                                     ...
                                                     lit("").alias("SEXUAL_ORIENTATION"), # data is not received so creating column and filling with blanks and renaming it

=======
OutputFileName = FileName_table.select(            FileName_table['person_id'].alias("PATID"), #renaming the input column person_id to the output name PATID
                                                   cf.get_date_from_datetime_udf(FileName_table['birth_datetime']).alias("BIRTH_DATE"), # Using common function to get date and then rename column
                                                   ...
                                                   ...
                                                   lit("").alias("SEXUAL_ORIENTATION"), # data is not received so creating column and filling with blanks and renaming it
                                                   
>>>>>>> origin/docker_container_alib



                                                    )

###################################################################################################################################

# Create the output file

###################################################################################################################################



cf.write_pyspark_output_file(
                    payspark_df = demographic,
                    output_file_name = "formatted_demographic.csv",
                    output_data_folder_path= formatter_output_data_folder_path)


spark.stop()









