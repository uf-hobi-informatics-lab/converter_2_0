###################################################################################################################################

# This script will take in the PCORnet formatted raw PROCEDURES file, do the necessary transformations, and output the formatted PCORnet PROCEDURES file

###################################################################################################################################

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
spark = cf.get_spark_session("procedures_formatter")

try: 

    ###################################################################################################################################

    # Loading the procedure table to be converted to the procedures table

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'



    procedures_table_name   = 'Epic_Procedure_*.txt'


    procedures_in = spark.read.load(input_data_folder_path+procedures_table_name,format="csv", sep="~", inferSchema="true", header="true", quote= '"')

    ###################################################################################################################################

    #Converting the fileds to PCORNet procedures Format

    ###################################################################################################################################

    procedures = procedures_in.select(



                    procedures_in['proceduresid'].alias('PROCEDURESID'),
                    procedures_in['patid'].alias('PATID'),
                    procedures_in['encounterid'].alias('ENCOUNTERID'),
                    procedures_in['enc_type'].alias('ENC_TYPE'),
                    cf.format_date_udf(procedures_in['admit_date']).alias('ADMIT_DATE'),
                    procedures_in['providerid'].alias('PROVIDERID'),
                    cf.format_date_udf(procedures_in['px_date']).alias('PX_DATE'),
                    procedures_in['px'].alias('PX'),
                    procedures_in['px_type'].alias('PX_TYPE'),
                    procedures_in['px_source'].alias('PX_SOURCE'),
                    procedures_in['ppx'].alias('PPX'),
                    procedures_in['rendering_providerid'].alias('RENDERING_PROVIDERID'),
                    procedures_in['raw_px'].alias('RAW_PX'),
                    procedures_in['raw_px_type'].alias('RAW_PX_TYPE'),
                    procedures_in['raw_ppx'].alias('RAW_PPX'),

    )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf =CommonFuncitons('UFH')
    cf.write_pyspark_output_file(
                        payspark_df = procedures,
                        output_file_name = "formatted_procedures.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'procedures_formatter.py' )

    cf.print_with_style(str(e), 'danger red')




