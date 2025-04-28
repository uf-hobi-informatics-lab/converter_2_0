###################################################################################################################################
# This script will map a PCORNet veritas_expanded table 
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

# spin the pyspak cluster and
spark = cf.get_spark_session("veritas_expanded_mapper")
 
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

        # deduplicated_data_folder_path = '/app/partners/'+input_partner.lower()+'/data/deduplicator_output/'+ input_data_folder+'/'
        deduplicated_data_folder_path = '/app/partners/' + input_partner.lower() + '/data/deduplicator_output/' + input_data_folder + '/' 
        mapped_data_folder_path    = '/app/partners/'+input_partner.lower()+'/data/mapper_output/'+ input_data_folder+'/'



    ###################################################################################################################################
    # Loading the unmapped enctounter table
    ###################################################################################################################################


        unmapped_veritas_expanded    = cf.spark_read(deduplicated_data_folder_path+"deduplicated_veritas_expanded.csv", spark)




    ###################################################################################################################################
    # create the mapping from the dictionaries
    ###################################################################################################################################




    ###################################################################################################################################
    # Apply the mappings dictionaries and the common function on the fields of the unmmaped encoutner table
    ###################################################################################################################################


        veritas_expanded = unmapped_veritas_expanded.select(              
            
                                    cf.encrypt_id_udf(unmapped_veritas_expanded['PATID']).alias("PATID"),
                                    unmapped_veritas_expanded['DOB'],
                                    unmapped_veritas_expanded['DOD'],
                                    unmapped_veritas_expanded['GENDER'],
                                    unmapped_veritas_expanded['GENDER_PROB_SCORE'],
                                    unmapped_veritas_expanded['STATE'],
                                    unmapped_veritas_expanded['ZIP3'],
                                    unmapped_veritas_expanded['SSA_DEATH_VERIFICATION'],
                                    unmapped_veritas_expanded['SOURCE_GOVT_FLAG'],
                                    unmapped_veritas_expanded['SOURCE_INTERMENT_FLAG'],
                                    unmapped_veritas_expanded['SOURCE_MEMORIAL_FLAG'],
                                    unmapped_veritas_expanded['SOURCE_CLAIMS_FLAG'],
                                    cf.get_current_time_udf().alias("UPDATED"),
                                    lit(input_partner.upper()).alias("SOURCE"),



                                                            )

    ###################################################################################################################################
    # Create the output file
    ###################################################################################################################################

        cf.write_pyspark_output_file(
                        payspark_df = veritas_expanded,
                        output_file_name = "mapped_veritas_expanded.csv",
                        output_data_folder_path= mapped_data_folder_path)

        spark.stop()

    spark.stop()

except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = input_partner,
                            job     = 'veritas_expanded_mapper.py' ,
                            text = str(e)
                            )

    # cf.print_with_style(str(e), 'danger red')