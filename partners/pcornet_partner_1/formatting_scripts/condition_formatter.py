
import pyspark
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
spark = cf.get_spark_session("condition_formatter")



try:

    ###################################################################################################################################
    
    # Loading the condition_occurrence table to be converted to the condition table

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'


    condition_table_name   = 'Epic_Condition_*.txt'

    condition_in = spark.read.load(input_data_folder_path+condition_table_name,format="csv", sep="~", inferSchema="true", header="true", quote= '"')



    ###################################################################################################################################

    # This function will determine the condition status based on the condition end date
    ###################################################################################################################################





    ###################################################################################################################################

    #Converting the fileds to PCORNet condition Format

    ###################################################################################################################################

    condition = condition_in.select( 


                            condition_in['conditionid'].alias('CONDITIONID'),
                            condition_in['patid'].alias('PATID'),
                            condition_in['encounterid'].alias('ENCOUNTERID'),
                            cf.format_date_udf(condition_in['report_date']).alias('REPORT_DATE'),
                            cf.format_date_udf(condition_in['resolve_date']).alias('RESOLVE_DATE'),
                            cf.format_date_udf(condition_in['onset_date']).alias('ONSET_DATE'),
                            condition_in['condition_status'].alias('CONDITION_STATUS'),
                            condition_in['condition'].alias('CONDITION'),
                            condition_in['condition_type'].alias('CONDITION_TYPE'),
                            condition_in['condition_source'].alias('CONDITION_SOURCE'),
                            condition_in['raw_condition_status'].alias('RAW_CONDITION_STATUS'),
                            condition_in['raw_condition_type'].alias('RAW_CONDITION_TYPE'),
                            condition_in['raw_condition_source'].alias('RAW_CONDITION_SOURCE')


    )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = condition,
                        output_file_name = "formatted_condition.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'condition_formatter.py' )

    cf.print_with_style(str(e), 'danger red')


