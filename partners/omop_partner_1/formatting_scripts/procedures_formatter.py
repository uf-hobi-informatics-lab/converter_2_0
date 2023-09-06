###################################################################################################################################

# This script will convert an OMOP procedure_occurrence table to a PCORnet format as the procedures table

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
spark = cf.get_spark_session("procedures_formatter")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder

try:

    ###################################################################################################################################

    # Loading the procedure_occurrence table to be converted to the procedures table

    ###################################################################################################################################


    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'


    procedure_occurrence_table_name   = 'Procedure_Occurrence.txt'
    visit_occurrence_table_name       = 'Visit_Occurrence.txt'


    procedure_occurrence = spark.read.load(input_data_folder_path+procedure_occurrence_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')
    visit_occurrence = spark.read.load(input_data_folder_path+visit_occurrence_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')

    visit_occurrence_data = visit_occurrence.collect()

    admit_date_dict = {row["visit_occurrence_id"]: str(row["visit_start_date"].strftime("%Y-%m-%d")) for row in visit_occurrence_data}
    admit_date_dict_udf = udf(lambda visit_start_date: admit_date_dict.get(visit_start_date, None), StringType())

    enc_type_dict = {row["visit_occurrence_id"]: row["visit_type"] for row in visit_occurrence_data}
    enc_type_dict_udf = udf(lambda visit_type: enc_type_dict.get(visit_type, None), StringType())





    ###################################################################################################################################

    #Converting the fileds to PCORNet procedures Format

    ###################################################################################################################################

    procedures = procedure_occurrence.select(       procedure_occurrence['procedure_occurrence_id'].alias("PROCEDURESID"),
                                                    procedure_occurrence['person_id'].alias("PATID"),
                                                    procedure_occurrence['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    enc_type_dict_udf(col('visit_occurrence_id')).alias("ENC_TYPE"),
                                                    admit_date_dict_udf(col('visit_occurrence_id')).alias("ADMIT_DATE"),
                                                    procedure_occurrence['provider_id'].alias("PROVIDERID"),
                                                    procedure_occurrence['procedure_date'].alias("PX_DATE"),
                                                    procedure_occurrence['procedure_code'].alias("PX"),
                                                    procedure_occurrence['procedure_code_type'].alias("PX_TYPE"),
                                                    lit('OD').alias("PX_SOURCE"),
                                                    lit('').alias("PPX"),
                                                    procedure_occurrence['procedure_code_source_value'].alias("RAW_PX"),
                                                    procedure_occurrence['procedure_code_type'].alias("RAW_PX_TYPE"),
                                                    lit('').alias("RAW_PPX"),                                             
                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = procedures,
                        output_file_name = "formatted_procedures.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'procedures_formatter.py' )

    cf.print_with_style(str(e), 'danger red')











