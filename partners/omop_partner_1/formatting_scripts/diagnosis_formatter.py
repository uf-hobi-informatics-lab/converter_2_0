###################################################################################################################################

# This script will convert an OMOP condition_occurrence table to a PCORnet format as the diagnosis table

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
spark = cf.get_spark_session("diagnosis_formatter")



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder



def get_dx_code_omop_partner_1(val):


    try:

        return val.split(' ')[1]

    except:

        return val

get_dx_code_omop_partner_1_udf = udf(get_dx_code_omop_partner_1, StringType())


def get_dx_type_omop_partner_1(val):


    try:

        return val.split(' ')[0]

    except:

        return val

get_dx_type_omop_partner_1_udf = udf(get_dx_type_omop_partner_1, StringType())




try:


    ###################################################################################################################################

    # Loading the condition_occurrence table to be converted to the diagnosis table

    ###################################################################################################################################


    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'


    condition_occurrence_table_name   = 'condition_occurrence.csv'
    visit_occurrence_table_name       = 'visit_occurrence.csv'


    condition_occurrence = spark.read.load(input_data_folder_path+condition_occurrence_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')
    visit_occurrence = spark.read.load(input_data_folder_path+visit_occurrence_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')


    filter_values = ["Primary Condition", "Secondary Condition"] # Only rows where condition_data_origin is in this list will convert to the DIAGNOSIS table
    filtered_condition_occurrence = condition_occurrence.filter(col("condition_data_origin").isin(filter_values))


    visit_occurrence_data = visit_occurrence.collect()

    admit_date_dict = {row["visit_occurrence_id"]: row["visit_start_date"] for row in visit_occurrence_data}
    admit_date_dict_udf = udf(lambda visit_start_date: admit_date_dict.get(visit_start_date, None), StringType())

    enc_type_dict = {row["visit_occurrence_id"]: row["visit_type"] for row in visit_occurrence_data}
    enc_type_dict_udf = udf(lambda visit_type: enc_type_dict.get(visit_type, None), StringType())





    ###################################################################################################################################

    #Converting the fileds to PCORNet enrollment Format

    ###################################################################################################################################

    diagnosis = filtered_condition_occurrence.select(  filtered_condition_occurrence['condition_occurrence_id'].alias("DIAGNOSISID"),
                                                    filtered_condition_occurrence['person_id'].alias("PATID"),
                                                    filtered_condition_occurrence['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    enc_type_dict_udf(col('visit_occurrence_id')).alias("ENC_TYPE"),
                                                    admit_date_dict_udf(col('visit_occurrence_id')).alias("ADMIT_DATE"),
                                                    filtered_condition_occurrence['provider_id'].alias("PROVIDERID"),
                                                    get_dx_code_omop_partner_1_udf(filtered_condition_occurrence['condition_source_value']).alias("DX"),
                                                    get_dx_type_omop_partner_1_udf(filtered_condition_occurrence['condition_source_value']).alias("DX_TYPE"),
                                                    filtered_condition_occurrence['condition_start_date'].alias("DX_DATE"),
                                                    filtered_condition_occurrence['condition_status_source_value'].alias("DX_SOURCE"),
                                                    filtered_condition_occurrence['condition_data_origin'].alias("DX_ORIGIN"),
                                                    filtered_condition_occurrence['condition_data_origin'].alias("PDX"),
                                                    filtered_condition_occurrence['Poa'].alias("DX_POA"),
                                                    filtered_condition_occurrence['condition_code'].alias("RAW_DX"),
                                                    filtered_condition_occurrence['condition_code_type'].alias("RAW_DX_TYPE"),
                                                    filtered_condition_occurrence['condition_status_source_value'].alias("RAW_DX_SOURCE"),
                                                    filtered_condition_occurrence['condition_data_origin'].alias("RAW_PDX"),
                                                    filtered_condition_occurrence['Poa'].alias("RAW_DX_POA"),
                                            
                                                
                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = diagnosis,
                        output_file_name = "formatted_diagnosis.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'diagnosis_formatter.py' )

    cf.print_with_style(str(e), 'danger red')






