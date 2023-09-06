###################################################################################################################################

# This script will convert an OMOP measurement table to a PCORnet format as the lab_result_cm table

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
spark = cf.get_spark_session("lab_result_cm_formatter")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder

###################################################################################################################################

# This function will rertun lab_result_loc base on the measurement_source_value

###################################################################################################################################

def get_lab_result_loc( measurement_source_value):

        if measurement_source_value[0:3] == 'POC':
            return 'P'
        else:
            return 'L'

get_lab_result_loc_udf = udf(get_lab_result_loc, StringType())

try: 

    ###################################################################################################################################

    # Loading the measurement table to be converted to the lab_result_cm table

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'



    measurement_table_name   = 'Measurement.txt'

    measurement = spark.read.load(input_data_folder_path+measurement_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')






    ###################################################################################################################################

    #Converting the fileds to PCORNet lab_result_cm Format

    ###################################################################################################################################

    lab_result_cm = measurement.select(             measurement['measurement_id'].alias("LAB_RESULT_CM_ID"),
                                                    measurement['person_id'].alias("PATID"),
                                                    measurement['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    measurement['measurement_code'].alias("SPECIMEN_SOURCE"),
                                                    measurement['measurement_code'].alias("LAB_LOINC"),
                                                    lit('OD').alias("LAB_RESULT_SOURCE"),
                                                    measurement['measurement_loinc_source'].alias("LAB_LOINC_SOURCE"),
                                                    measurement['priority'].alias("PRIORITY"),
                                                    get_lab_result_loc_udf(measurement['measurement_code_source_value']).alias("RESUTL_LOC"),
                                                    lit('').alias("LAB_PX"),
                                                    lit('').alias("LAB_PX_TYPE"),
                                                    measurement['measurement_order_date'].alias("LAB_ORDER_DATE"),
                                                    measurement['measurement_date'].alias("SPECIMEN_DATE"),
                                                    cf.get_time_from_datetime_udf(measurement['measurement_datetime']).alias("SPECIMEN_TIME"),
                                                    measurement['measurement_date'].alias("RESULT_DATE"),
                                                    cf.get_time_from_datetime_udf(measurement['measurement_datetime']).alias("RESTULT_TIME"),
                                                    measurement['value_as_string'].alias("RESULT_QUAL"),
                                                    lit('').alias("RESULT_SNOMED"),
                                                    measurement['value_as_number'].alias("RESULT_NUM"),
                                                    measurement['operator'].alias("RESULT_MODIFIER"),
                                                    measurement['unit'].alias("RESULT_UNIT"),
                                                    measurement['range_low'].alias("NORM_RANGE_LOW"),
                                                    measurement['operator'].alias("NORM_MODIFIER_LOW"),
                                                    measurement['range_high'].alias("NORM_RANGE_HIGH"),
                                                    measurement['operator'].alias("NORM_MODIFIER_HIGH"),
                                                    lit('').alias("ABN_IND"),
                                                    measurement['measurement_code_source_value'].alias("RAW_LAB_NAME"),
                                                    measurement['measurement_code_source_value'].alias("RAW_LAB_CODE"),
                                                    lit('').alias("RAW_PANEL"),
                                                    measurement['measurement_code_source_value'].alias("RAW_RESULT"),
                                                    measurement['unit_source_value'].alias("RAW_UNIT"),
                                                    lit('').alias("RAW_ORDER_DEPT"),
                                                    lit('').alias("RAW_FACILITY_CODE"),
                                
                                                                                        
                                                
                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = lab_result_cm,
                        output_file_name = "formatted_lab_result_cm.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()

except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'lab_result_cm_formatter.py' )

    cf.print_with_style(str(e), 'danger red')








