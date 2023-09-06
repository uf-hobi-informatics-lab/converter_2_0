###################################################################################################################################

# This script will convert an OMOP obsrevation_period table to a PCORnet format as the enrollment table

###################################################################################################################################


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse

cf = CommonFuncitons('omop_partner_1')
spark = cf.get_spark_session("encounter_formatter")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder

try :


    ###################################################################################################################################

    # Loading the obsrevation_period table to be converted to the enrollment table
    # loading the care_site, location, and visit_payer as they are been used to retrive some data for the mapping

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'


    obsrevation_period_table_name       = 'Observation_Period.txt'

    obsrevation_period = spark.read.load(input_data_folder_path+obsrevation_period_table_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')




    ###################################################################################################################################

    #Converting the fileds to PCORNet enrollment Format

    ###################################################################################################################################

    enrollment = obsrevation_period.select(         obsrevation_period['person_id'].alias("PATID"),
                                                    obsrevation_period['observation_period_start_date'].alias("ENR_START_DATE"),
                                                    obsrevation_period['observation_period_end_date'].alias("ENR_END_DATE"),
                                                    obsrevation_period['chart'].alias("CHART"),
                                                    obsrevation_period['enrollment_basis'].alias("ENR_BASIS"),
                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = enrollment,
                        output_file_name = "formatted_enrollment.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()

    
except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_1',
                            job     = 'enrollment_formatter.py' )

    cf.print_with_style(str(e), 'danger red')








