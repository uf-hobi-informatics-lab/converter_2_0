###################################################################################################################################

# This script will convert an OMOP drug_exposure table to a PCORnet format as the immunization table

###################################################################################################################################


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse


cf = CommonFuncitons('jhs')

#Create SparkSession
spark = cf.get_spark_session("immunization_formatter")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


try: 


    ###################################################################################################################################

    # Loading the drug_exposure table to be converted to the immunization table

    ###################################################################################################################################


    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/jhs/data/formatter_output/{input_data_folder}/'



    drug_exposure_table_name   = 'OneFlorida_Drug_Exposure_tab.txt'

    drug_exposure = spark.read.load(input_data_folder_path+drug_exposure_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')

    filter_values = ["Prescription written","Prescription","Home-Med","Prescription dispensed in pharmacy"]
    filtered_drug_exposure = drug_exposure.filter(col("drug_type").isin(filter_values))




    ###################################################################################################################################

    # This function will attemp to return the float value of an input

    ###################################################################################################################################

    def get_float_format( val):
        float_val = None

        try:
            # remove ','
            val = str(val).replace(',', '')
            float_val = float(val)
        except Exception:
            # cls.logger.warning("Unable to format_float({}). Will use None".format(val))  # noqa
            pass
        return float_val

    get_float_format_udf = udf(get_float_format, StringType())


    ###################################################################################################################################

    #Converting the fields to PCORNet immunization Format

    ###################################################################################################################################

    immunization = filtered_drug_exposure.select(     filtered_drug_exposure['drug_exposure_id'].alias("IMMUNIZATIONID"),
                                                    filtered_drug_exposure['person_id'].alias("PATID"),
                                                    filtered_drug_exposure['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    filtered_drug_exposure['procedure_occurrence_id'].alias("PROCEDURESID"),
                                                    filtered_drug_exposure['provider_id'].alias("VX_PROVIDERID"),
                                                    to_date(filtered_drug_exposure['drug_exposure_record_date']).alias("VX_RECORD_DATE"),
                                                    to_date(filtered_drug_exposure['drug_exposure_start_date']).alias("VX_ADMIN_DATE"),
                                                    filtered_drug_exposure['drug_code_type'].alias("VX_CODE_TYPE"),
                                                    filtered_drug_exposure['drug_code'].alias("VX_CODE"),
                                                    filtered_drug_exposure['vx_status'].alias("VX_STATUS"),
                                                    filtered_drug_exposure['vx_status_reason'].alias("VX_STATUS_REASON"),
                                                    lit('DR').alias("VX_SOURCE"),
                                                    filtered_drug_exposure['dose_ordered'].alias("VX_DOSE"),
                                                    filtered_drug_exposure['dose_unit'].alias("VX_DOSE_UNIT"),
                                                    filtered_drug_exposure['route'].alias("VX_ROUTE"),
                                                    filtered_drug_exposure['body_site_source_value'].alias("VX_BODY_SITE"),
                                                    filtered_drug_exposure['vx_manufacturer'].alias("VX_MANUFACTURER"),
                                                    filtered_drug_exposure['lot_number'].alias("VX_LOT_NUM"),
                                                    to_date(filtered_drug_exposure['drug_exposure_end_date']).alias("VX_EXP_DATE"),
                                                    filtered_drug_exposure['drug_type_source_value'].alias("RAW_VX_NAME"),
                                                    filtered_drug_exposure['drug_code'].alias("RAW_VX_CODE"),
                                                    filtered_drug_exposure['drug_code_type'].alias("RAW_VX_CODE_TYPE"),
                                                    filtered_drug_exposure['dose_ordered'].alias("RAW_VX_DOSE"),
                                                    filtered_drug_exposure['dose_unit'].alias("RAW_VX_DOSE_UNIT"),
                                                    filtered_drug_exposure['route_source_value'].alias("RAW_VX_ROUTE"),
                                                    filtered_drug_exposure['body_site_source_value'].alias("RAW_VX_BODY_SITE"),
                                                    filtered_drug_exposure['vx_status'].alias("RAW_VX_STATUS"),
                                                    filtered_drug_exposure['vx_status_reason'].alias("RAW_VX_STATUS_REASON"),
                                                    filtered_drug_exposure['vx_manufacturer'].alias("RAW_VX_MANUFACTURER"),

                                                    
                                                    
                                                    
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
                            partner = 'jhs',
                            job     = 'immunization_formatter.py' )

    cf.print_with_style(str(e), 'danger red')





