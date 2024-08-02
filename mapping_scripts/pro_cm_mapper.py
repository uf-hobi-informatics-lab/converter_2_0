###################################################################################################################################
# This script will map a PCORNet pro_cm table 
###################################################################################################################################

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons
import importlib
import sys
# from partners import partners_list
from itertools import chain
import argparse


###################################################################################################################################
# parsing the input arguments to select the partner name
###################################################################################################################################


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--partner")
parser.add_argument("-f", "--data_folder")
args = parser.parse_args()
input_partner = args.partner.lower()
input_data_folder = args.data_folder

cf =CommonFuncitons(input_partner)

spark = cf.get_spark_session("pro_cm_mapper")

try:


    ###################################################################################################################################
    # Test if the partner name is valid or not
    ###################################################################################################################################


    if  not cf.valid_partner_name(input_partner):

        print("Error: Unrecognized partner "+input_partner+" !!!!!")
        sys.exit()

    else:


    ###################################################################################################################################
    # Load the config file for the selected parnter
    ###################################################################################################################################

        partner_dictionaries_path = "partners."+input_partner+".dictionaries"
        partner_dictionaries = importlib.import_module(partner_dictionaries_path)

        # deduplicated_data_folder_path = '/app/partners/'+input_partner.lower()+'/data/formatter_output/'+ input_data_folder+'/'
        deduplicated_data_folder_path = '/app/partners/' + input_partner.lower() + '/data/deduplicator_output/' + input_data_folder  + '/'
        mapped_data_folder_path    = '/app/partners/'+input_partner.lower()+'/data/mapper_output/'+ input_data_folder+'/'


    ###################################################################################################################################
    # spin the pyspak cluster and
    # Loading the unmapped enctounter table
    ###################################################################################################################################

        spark = cf.get_spark_session("pro_cm_mapper")

        unmapped_pro_cm = spark.read.option("inferSchema", "false").load(deduplicated_data_folder_path+"deduplicated_pro_cm.csv",format="csv", sep="\t", inferSchema="false", header="true",  quote= '"')

    ###################################################################################################################################
    # create the mapping from the dictionaries
    ###################################################################################################################################
        
        mapping_pro_cm_type_dict = create_map([lit(x) for x in chain(*partner_dictionaries.pro_cm_pro_type_dict.items())])
        mapping_pro_method_dict = create_map([lit(x) for x in chain(*partner_dictionaries.pro_cm_pro_method_dict.items())])
        mapping_pro_mode_dict = create_map([lit(x) for x in chain(*partner_dictionaries.pro_cm_pro_mode_dict.items())])
        mapping_pro_cat_dict = create_map([lit(x) for x in chain(*partner_dictionaries.pro_cm_pro_cat_dict.items())])
        mapping_pro_source_dict = create_map([lit(x) for x in chain(*partner_dictionaries.pro_cm_pro_source_dict.items())])       

    ###################################################################################################################################
    # Apply the mappings dictionaries and the common function on the fields of the unmmaped encoutner table
    ###################################################################################################################################

        pro_cm = unmapped_pro_cm.select(              
            
            #MODIFY THIS SECTION
            cf.encrypt_id_udf(unmapped_pro_cm['PRO_CM_ID']).alias('PRO_CM_ID'),
            cf.encrypt_id_udf(unmapped_pro_cm['PATID']).alias('PATID'),
            cf.encrypt_id_udf(unmapped_pro_cm['ENCOUNTERID']).alias('ENCOUNTERID'),
            unmapped_pro_cm['PRO_DATE'].alias('PRO_DATE'),
            unmapped_pro_cm['PRO_TIME'].alias('PRO_TIME'),
            mapping_pro_cm_type_dict[upper(col('PRO_TYPE'))].alias('PRO_TYPE'),
            unmapped_pro_cm['PRO_ITEM_NAME'],
            unmapped_pro_cm['PRO_ITEM_LOINC'],
            unmapped_pro_cm['PRO_RESPONSE_TEXT'],
            unmapped_pro_cm['PRO_RESPONSE_NUM'],
            mapping_pro_method_dict[upper(col('PRO_METHOD'))].alias('PRO_METHOD'),
            mapping_pro_mode_dict[upper(col('PRO_MODE'))].alias('PRO_MODE'),
            mapping_pro_cat_dict[upper(col('PRO_CAT'))].alias('PRO_CAT'),
            mapping_pro_source_dict[upper(col('PRO_SOURCE'))].alias('PRO_SOURCE'),
            unmapped_pro_cm['PRO_ITEM_VERSION'],
            unmapped_pro_cm['PRO_MEASURE_NAME'],
            unmapped_pro_cm['PRO_MEASURE_SEQ'],
            unmapped_pro_cm['PRO_MEASURE_SCORE'],
            unmapped_pro_cm['PRO_MEASURE_THETA'],
            unmapped_pro_cm['PRO_MEASURE_SCALED_TSCORE'],
            unmapped_pro_cm['PRO_MEASURE_STANDARD_ERROR'],
            unmapped_pro_cm['PRO_MEASURE_COUNT_SCORED'],
            unmapped_pro_cm['PRO_MEASURE_LOINC'],
            unmapped_pro_cm['PRO_MEASURE_VERSION'],
            unmapped_pro_cm['PRO_ITEM_FULLNAME'],
            unmapped_pro_cm['PRO_ITEM_TEXT'],
            unmapped_pro_cm['PRO_MEASURE_FULLNAME'],
            cf.get_current_time_udf().alias("UPDATED"),
            lit(input_partner.upper()).alias("SOURCE"),
            unmapped_pro_cm['PRO_CM_ID'].alias('JOIN_FIELD')
        )

    ###################################################################################################################################
    # Create the output file
    ###################################################################################################################################

        pro_cm_with_additional_fileds = cf.append_additional_fields(
            mapped_df = pro_cm,
            file_name = "deduplicated_pro_cm.csv",
            deduplicated_data_folder_path = deduplicated_data_folder_path,
            join_field = "PRO_CM_ID",
            spark = spark)

        cf.write_pyspark_output_file(
                        payspark_df = pro_cm_with_additional_fileds,
                        output_file_name = "mapped_pro_cm.csv",
                        output_data_folder_path= mapped_data_folder_path)

        spark.stop()

except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = input_partner,
                            job     = 'pro_cm_mapper.py' ,
                            text = str(e)
                            )

    # cf.print_with_style(str(e), 'danger red')
