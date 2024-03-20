###################################################################################################################################

# This script will convert an OMOP drug_exposure table to a PCORnet format as the med_admin table

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
spark = cf.get_spark_session("med_admin_formatter")



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


try: 


    ###################################################################################################################################

    # Loading the drug_exposure table to be converted to the med_admin table

    ###################################################################################################################################


    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'

    drug_exposure_table_name   = 'drug_exposure.csv'

    drug_exposure = spark.read.load(input_data_folder_path+drug_exposure_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')

    filter_values = ["Inpatient Administration","Inpatient administration","Inpatient","Medication list entry","Physician administered drug (identified from EHR order)"]
    filtered_drug_exposure = drug_exposure.filter(col("drug_type").isin(filter_values))






    ###################################################################################################################################

    #Converting the fileds to PCORNet med_admin Format

    ###################################################################################################################################

    med_admin = filtered_drug_exposure.select(      filtered_drug_exposure['drug_exposure_id'].alias("MEDADMINID"),
                                                    filtered_drug_exposure['person_id'].alias("PATID"),
                                                    filtered_drug_exposure['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    lit('').alias("PRESCRIBINGID"),
                                                    filtered_drug_exposure['provider_id'].alias("MEDADMIN_PROVIDERID"),
                                                    filtered_drug_exposure['drug_exposure_start_date'].alias("MEDADMIN_START_DATE"),
                                                    cf.get_time_from_datetime_udf(filtered_drug_exposure['drug_exposure_start_datetime']).alias("MEDADMIN_START_TIME"),
                                                    filtered_drug_exposure['drug_exposure_end_date'].alias("MEDADMIN_STOP_DATE"),
                                                    cf.get_time_from_datetime_udf(filtered_drug_exposure['drug_exposure_end_datetime']).alias("MEDADMIN_STOP_TIME"),
                                                    filtered_drug_exposure['drug_code_type'].alias("MEDADMIN_TYPE"),
                                                    filtered_drug_exposure['drug_code'].alias("MEDADMIN_CODE"),
                                                    filtered_drug_exposure['dose_ordered'].alias("MEDADMIN_DOSE_ADMIN"),
                                                    filtered_drug_exposure['dose_unit'].alias("MEDADMIN_DOSE_ADMIN_UNIT"),
                                                    filtered_drug_exposure['route'].alias("MEDADMIN_ROUTE"),
                                                    lit('OD').alias("MEDADMIN_SOURCE"),
                                                    filtered_drug_exposure['drug_code'].alias("RAW_MEDADMIN_MED_NAME"),
                                                    filtered_drug_exposure['drug_code'].alias("RAW_MEDADMIN_CODE"),
                                                    filtered_drug_exposure['dose_ordered_source_value'].alias("RAW_MEDADMIN_DOSE_ADMIN"),
                                                    filtered_drug_exposure['dose_unit'].alias("RAW_MEDADMIN_DOSE_ADMIN_UNIT"),
                                                    filtered_drug_exposure['route_source_value'].alias("RAW_MEDADMIN_ROUTE"),

                                                    
                                                    
                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = med_admin,
                        output_file_name = "formatted_med_admin.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'med_admin_formatter.py' )

    cf.print_with_style(str(e), 'danger red')








