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


partner_name = 'pcornet_partner_1'

cf =CommonFuncitons(partner_name.upper())

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


def fh_pdx( key):
        """
        PDX lookup table contains 5 choices but has about 20 that appear.
        Everything but a PDX of 1 is considered a Secondary PDX with a PDX of 1
        being a primary PDX.
        """
        if key == "Primary":
            return "P"  # primary
        elif key == "Secondary":
            return "S"  # secondary
        else:
            return "NI"


fh_pdx_udf= udf(fh_pdx, StringType())

# @classmethod
# def fh_ppx( key):
#     """
#     Mapping for PPX - Per Duke 12/11/2019
#     0 -                           UN=Unknown
#     1 -                           P=Principal;
#     2 -                           S=Secondary
#     3-999                    OT=Other
#     """
#     value = None
#     if key == '0': value = 'UN'
#     elif key == '1': value = 'P'
#     elif key == '2': value = 'S'
#     elif key >= '3': value = 'OT'
#     else: value = 'UN'
    
#     return value



#Create SparkSession
spark = cf.get_spark_session("diagnosis_formatter")

try:


    ###################################################################################################################################

    # Loading the condition_occurrence table to be converted to the diagnosis table

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'


    diagnosis_table_name       = 'Epic_Diagnosis_*.txt'



    diagnosis_in = spark.read.load(input_data_folder_path+diagnosis_table_name,format="csv", sep="~", inferSchema="false", header="true", quote= '"')


    ###################################################################################################################################

    #Converting the fileds to PCORNet enrollment Format

    ###################################################################################################################################

    diagnosis = diagnosis_in.select(

                    diagnosis_in['diagnosisid'].alias('DIAGNOSISID'),
                    diagnosis_in['patid'].alias('PATID'),
                    diagnosis_in['encounterid'].alias('ENCOUNTERID'),
                    diagnosis_in['enc_type'].alias('ENC_TYPE'),
                    cf.format_date_udf(diagnosis_in['admit_date']).alias('ADMIT_DATE'),
                    diagnosis_in['providerid'].alias('PROVIDERID'),
                    diagnosis_in['raw_dx_type'].alias('DX'),
                    diagnosis_in['dx_type'].alias('DX_TYPE'),
                    cf.format_date_udf(diagnosis_in['dx_date']).alias('DX_DATE'),
                    diagnosis_in['raw_dx_source'].alias('DX_SOURCE'),
                    lit('OD').alias('DX_ORIGIN'),
                    fh_pdx_udf(diagnosis_in['pdx']).alias('PDX'),
                    diagnosis_in['raw_dx'].alias('DX_POA'),
                    diagnosis_in['dx'].alias('RAW_DX'),
                    diagnosis_in['raw_dx_type'].alias('RAW_DX_TYPE'),
                    diagnosis_in['raw_dx_source'].alias('RAW_DX_SOURCE'),
                    diagnosis_in['raw_pdx'].alias('RAW_PDX'),
                    diagnosis_in['dx_poa'].alias('RAW_DX_POA'),




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
                            partner = partner_name.lower(),
                            job     = 'diagnosis_formatter.py' )

    cf.print_with_style(str(e), 'danger red')





