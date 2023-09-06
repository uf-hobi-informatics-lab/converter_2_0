###################################################################################################################################

# This script will format the death_cause dataset to a PCORnet formatted death_cause table.

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
spark = cf.get_spark_session("death_cause_formatter")


try:
        
    ###################################################################################################################################

    # Loading the death dataset to be formatted to the pcornet_death_cause table.

    ###################################################################################################################################

    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name.lower()}/data/formatter_output/{input_data_folder}/'

    death_table_name       = 'Epic_Deathcause_*.txt'

    unformatted_death_cause = spark.read.load(input_data_folder_path+death_table_name,format="csv", sep="~", inferSchema="true", header="true", quote= '"')

    ###################################################################################################################################

    # Converting the fields to the PCORnet format.

    ###################################################################################################################################

    pcornet_death = unformatted_death_cause.select(    
                                                    
                                                    unformatted_death_cause['patid'].alias("PATID"),
                                                    unformatted_death_cause['death_cause'].alias("DEATH_CAUSE"),
                                                    unformatted_death_cause['death_cause_code'].alias("DEATH_CAUSE_CODE"),
                                                    unformatted_death_cause['death_cause_type'].alias("DEATH_CAUSE_TYPE"),
                                                    unformatted_death_cause['death_cause_source'].alias("DEATH_CAUSE_SOURCE"),
                                                    unformatted_death_cause['death_cause_confidence'].alias("DEATH_CAUSE_CONFIDENCE"),
                                                        )

    ###################################################################################################################################

    # Create the output file.

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = pcornet_death,
                        output_file_name = "formatted_death_cause.csv",
                        output_data_folder_path = formatter_output_data_folder_path)

    # Once the script has finished, time to shutdown the resources used to run the PySpark Cluster.
    spark.stop()


except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = partner_name.lower(),
                            job     = 'death_cause_formatter.py' )

    cf.print_with_style(str(e), 'danger red')






