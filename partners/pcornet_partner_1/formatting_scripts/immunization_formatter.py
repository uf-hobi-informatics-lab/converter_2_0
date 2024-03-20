###################################################################################################################################

# This script will take in the PCORnet formatted raw LAB_RESULT_CM file, do the necessary transformations, and output the formatted PCORnet LAB_RESULT_CM file

###################################################################################################################################
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse



def format_float( val):
    float_val = None

    try:
        # remove ','
        val = str(val).replace(',', '')
        float_val = float(val)
    except :

        pass       
        
    return float_val

format_float_udf = udf(format_float, StringType())

partner_name = 'pcornet_partner_1'

cf =CommonFuncitons(partner_name.upper())

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder

#Create SparkSession
spark = cf.get_spark_session("immunization_formatter")

try: 

    ###################################################################################################################################

    # Loading the raw lab_result_cm table

    ###################################################################################################################################
    input_data_folder_path               = f'/data/{input_data_folder}/'
    # input_data_folder_path               = f'/app/partners/pcornet_partner_1/data/input/{input_data_folder}/'  


    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'


    immunization_table_name   = 'Epic_Immunization_*.txt'

    immunization_in = spark.read.load(input_data_folder_path+immunization_table_name,format="csv", sep="~", inferSchema="false", header="true", quote= '"')

    ###################################################################################################################################

    #Converting the fileds to PCORNet lab_result_cm Format

    ###################################################################################################################################

    immunization = immunization_in.select(


                    immunization_in['immunizationid'].alias('IMMUNIZATIONID'),
                    immunization_in['patid'].alias('PATID'),
                    immunization_in['encounterid'].alias('ENCOUNTERID'),
                    immunization_in['proceduresid'].alias('PROCEDURESID'),
                    immunization_in['vx_providerid'].alias('VX_PROVIDERID'),
                    cf.format_date_udf(immunization_in['vx_record_date']).alias('VX_RECORD_DATE'),
                    cf.format_date_udf(immunization_in['vx_admin_date']).alias('VX_ADMIN_DATE'),
                    immunization_in['raw_vx_code_type'].alias('VX_CODE_TYPE'),
                    immunization_in['raw_vx_code'].alias('VX_CODE'),
                    immunization_in['raw_vx_status'].alias('VX_STATUS'),
                    immunization_in['raw_vx_status_reason'].alias('VX_STATUS_REASON'),
                    immunization_in['vx_source'].alias('VX_SOURCE'),
                    format_float_udf(immunization_in['raw_vx_dose']).alias('VX_DOSE'),
                    immunization_in['raw_vx_dose_unit'].alias('VX_DOSE_UNIT'),
                    immunization_in['raw_vx_route'].alias('VX_ROUTE'),
                    immunization_in['raw_vx_body_site'].alias('VX_BODY_SITE'),
                    immunization_in['raw_vx_manufacturer'].alias('VX_MANUFACTURER'),
                    immunization_in['vx_lot_num'].alias('VX_LOT_NUM'),
                    cf.format_date_udf(immunization_in['vx_exp_date']).alias('VX_EXP_DATE'),
                    immunization_in['raw_vx_name'].alias('RAW_VX_NAME'),
                    immunization_in['raw_vx_code'].alias('RAW_VX_CODE'),
                    immunization_in['raw_vx_code_type'].alias('RAW_VX_CODE_TYPE'),
                    immunization_in['raw_vx_dose'].alias('RAW_VX_DOSE'),
                    immunization_in['raw_vx_dose_unit'].alias('RAW_VX_DOSE_UNIT'),
                    immunization_in['raw_vx_route'].alias('RAW_VX_ROUTE'),
                    immunization_in['raw_vx_body_site'].alias('RAW_VX_BODY_SITE'),
                    immunization_in['raw_vx_status'].alias('RAW_VX_STATUS'),
                    immunization_in['raw_vx_status_reason'].alias('RAW_VX_STATUS_REASON'),
                    immunization_in['raw_vx_manufacturer'].alias('RAW_VX_MANUFACTURER'),
    )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = immunization,
                        output_file_name = "formatted_immunization.csv",
                        output_data_folder_path= formatter_output_data_folder_path)


    spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'immunization_formatter.py' )

    cf.print_with_style(str(e), 'danger red')





