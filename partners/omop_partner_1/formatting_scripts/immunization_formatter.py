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


cf = CommonFuncitons('omop_partner_1')

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
    formatter_output_data_folder_path    = f'/app/partners/omop_partner_1/data/formatter_output/{input_data_folder}/'



    drug_exposure_table_name   = 'drug_exposure.csv'

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

    immunization = filtered_drug_exposure.select(    filtered_drug_exposure['drug_exposure_id'].alias("immunizationID"),
                                                    filtered_drug_exposure['person_id'].alias("PATID"),
                                                    filtered_drug_exposure['visit_occurrence_id'].alias("ENCOUNTERID"),
                                                    filtered_drug_exposure['provider_id'].alias("RX_PROVIDERID"),
                                                    filtered_drug_exposure['drug_exposure_start_date'].alias("RX_ORDER_DATE"),
                                                    filtered_drug_exposure['drug_exposure_start_datetime'].alias("RX_ORDER_TIME"),
                                                    filtered_drug_exposure['drug_exposure_start_date'].alias("RX_START_DATE"),
                                                    filtered_drug_exposure['drug_exposure_end_date'].alias("RX_END_DATE"),
                                                    filtered_drug_exposure['dose_ordered'].alias("RX_DOSE_ORDERED"),
                                                    filtered_drug_exposure['dose_unit'].alias("RX_DOSE_ORDERED_UNIT"),
                                                    get_float_format_udf(filtered_drug_exposure['quantity']).alias("RX_QUANTITY"),
                                                    filtered_drug_exposure['drug_code'].alias("RX_DOSE_FORM"),
                                                    filtered_drug_exposure['refills'].alias("RX_REFILLS"),
                                                    filtered_drug_exposure['days_supply'].alias("RX_DAYS_SUPPLY"),
                                                    filtered_drug_exposure['rx_frequency'].alias("RX_FREQUENCY"),
                                                    filtered_drug_exposure['sig'].alias("RX_PRN_FLAG"),
                                                    filtered_drug_exposure['route'].alias("RX_ROUTE"),
                                                    filtered_drug_exposure['drug_type'].alias("RX_BASIS"),
                                                    filtered_drug_exposure['drug_code'].alias("RXNORM_CUI"),
                                                    lit('OD').alias("RX_SOURCE"),
                                                    lit('OD').alias("RX_DISPENSE_AS_WRITTEN"),
                                                    filtered_drug_exposure['drug_code'].alias("RAW_RX_MED_NAME"),
                                                    filtered_drug_exposure['rx_frequency'].alias("RAW_RX_FREQUENCY"),
                                                    filtered_drug_exposure['drug_code'].alias("RAW_RXNORM_CUI"),
                                                    filtered_drug_exposure['quantity'].alias("RAW_RX_QUANTITY"),
                                                    filtered_drug_exposure['drug_code'].alias("RAW_RX_NDC"),
                                                    filtered_drug_exposure['dose_ordered_source_value'].alias("RAW_RX_DOSE_ORDERED"),
                                                    filtered_drug_exposure['dose_unit'].alias("RAW_RX_DOSE_ORDERED_UNIT"),
                                                    filtered_drug_exposure['route_source_value'].alias("RAW_RX_ROUTE"),
                                                    filtered_drug_exposure['refills'].alias("RAW_RX_REFILLS"),

                                                    
                                                    
                                                    
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
                            partner = 'omop_partner_1',
                            job     = 'immunization_formatter.py' )

    cf.print_with_style(str(e), 'danger red')





