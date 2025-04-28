###################################################################################################################################

# This script will convert an OMOP drug_exposure table to a PCORnet format as the external_meds table

###################################################################################################################################


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import argparse

partner_name = 'omop_partner_plus'
cf = CommonFuncitons('omop_partner_plus')

#Create SparkSession
spark = cf.get_spark_session("external_meds_formatter")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_data_folder = args.data_folder


try: 


    ###################################################################################################################################

    # Loading the drug_exposure table to be converted to the external_meds table

    ###################################################################################################################################


    input_data_folder_path               = f'/data/{input_data_folder}/'
    formatter_output_data_folder_path    = f'/app/partners/{partner_name}/data/formatter_output/{input_data_folder}/'
    concept_table_path                   = f'/app/common/omop_cdm/CONCEPT.csv'


    drug_exposure_table_name   = 'drug_exposure.csv'
    drug_exposure_sup_table_name   = 'drug_exposure_sup2.csv'

    drug_exposure = spark.read.load(input_data_folder_path+drug_exposure_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')

    drug_exposure_sup = spark.read.load(input_data_folder_path+drug_exposure_sup_table_name,format="csv", sep=",", inferSchema="false", header="true", quote= '"').withColumnRenamed("drug_exposure_id", "drug_exposure_id_sup")

    concept      = cf.spark_read(concept_table_path,spark)
    drug_concept = concept.filter(concept.domain_id == 'Drug').withColumnRenamed("concept_name", "drug_concept_name").withColumnRenamed("vocabulary_id", "drug_vocabulary_id").withColumnRenamed("concept_code", "drug_concept_code")
    drug_concept = broadcast(drug_concept)

    external_meds_drug_type_concept = concept.filter((col("domain_id") == "Type Concept"))# & (col("concept_name").rlike(r"(?i)Prescri") ))
    external_meds_drug_type_concept = broadcast(external_meds_drug_type_concept)

    route_concept = concept.filter(concept.domain_id == 'Route').withColumnRenamed("concept_name", "route_concept_name")
    route_concept = broadcast(route_concept)


    filter_values = ["Yes","yes","YES"]
    filtered_drug_exposure = drug_exposure_sup.filter(col("external_med_flag").isin(filter_values))


    joined_drug_exposure = drug_exposure.join(external_meds_drug_type_concept, external_meds_drug_type_concept['concept_id']==drug_exposure['drug_type_concept_id'], how='inner').drop("concept_id")\
                                            .join(drug_concept, drug_concept['concept_id']==drug_exposure['drug_concept_id'], how='left').drop("concept_id")\
                                            .join(filtered_drug_exposure, filtered_drug_exposure['drug_exposure_id_sup']== drug_exposure['drug_exposure_id'], how = 'inner')\
                                            .join(route_concept, route_concept['concept_id']== drug_exposure['route_concept_id'], how = 'left')

    
    ###################################################################################################################################

    #Converting the fields to PCORNet external meds Format

    ###################################################################################################################################

    external_meds = joined_drug_exposure.select(    joined_drug_exposure['drug_exposure_id'].alias("EXTMEDID"),
                                                    joined_drug_exposure['person_id'].alias("PATID"),
                                                    joined_drug_exposure['drug_exposure_record_date'].alias("EXT_RECORD_DATE"),
                                                    joined_drug_exposure['drug_exposure_start_date'].alias("EXT_PAT_START_DATE"),
                                                    joined_drug_exposure['drug_exposure_end_date'].alias("EXT_END_DATE"),
                                                    joined_drug_exposure['drug_exposure_end_date'].alias("EXT_PAT_END_DATE "),
                                                    joined_drug_exposure['days_supply'].alias("EXT_DOSE"),
                                                    joined_drug_exposure['dose_unit_source_value'].alias("EXT_DOSE_ORDERED_UNIT"),
                                                    joined_drug_exposure['drug_concept_code'].alias("EXT_DOSE_FORM"),
                                                    joined_drug_exposure['route_concept_name'].alias("EXT_ROUTE"),
                                                    joined_drug_exposure['drug_vocabulary_id'].alias("EXT_BASIS"),
                                                    joined_drug_exposure['drug_concept_code'].alias("RXNORM_CUI"),
                                                    lit('OD').alias("EXTMED_SOURCE "),
                                                    joined_drug_exposure['drug_concept_name'].alias("RAW_EXT_MED_NAME"),
                                                    joined_drug_exposure['drug_concept_code'].alias("RAW_RXNORM_CUI"),
                                                    joined_drug_exposure['drug_concept_code'].alias("RAW_EXT_NDC"),
                                                    joined_drug_exposure['days_supply'].alias("RAW_EXT_DOSE"),
                                                    joined_drug_exposure['dose_unit_source_value'].alias("RAW_EXT_DOSE_UNIT"),
                                                    joined_drug_exposure['route_source_value'].alias("RAW_EXT_ROUTE"),
                                                    

                                                    
                                                    
                                                    
                                                        )

    ###################################################################################################################################

    # Create the output file

    ###################################################################################################################################

    cf.write_pyspark_output_file(
                        payspark_df = external_meds,
                        output_file_name = "formatted_external_meds.csv",
                        output_data_folder_path= formatter_output_data_folder_path)

    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = 'omop_partner_plus',
                            job     = 'external_meds_formatter.py' ,
                            text    = str(e))





