

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from datetime import datetime
from pyspark.sql.functions import *
from commonFunctions import CommonFuncitons


import argparse


cf =CommonFuncitons('NotUsed')


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
parser.add_argument("-t", "--table")
parser.add_argument("-p", "--partner")
parser.add_argument("-ftm", "--fixed_table_name")
parser.add_argument("-i", "--input_path")
parser.add_argument("-o", "--output_path")
parser.add_argument("-sr1", "--src1")
parser.add_argument("-sr2", "--src2")

args = parser.parse_args()
input_data_folder         = args.data_folder
examined_table_name       = args.table
input_partner_name        = args.partner
source_list_name          = args.src1
source_column             = args.src2
input_data_folder_path    = args.input_path
output_data_folder_path   = args.output_path
fixed_table_name          = args.fixed_table_name
spark = cf.get_spark_session("list_remover_fix")

this_fix_name = 'common_list_remover_fix_1.0'
examined_table_name_parsed = examined_table_name.replace('mapped_','').replace('.csv','')
source_list_path = 'common/lists/'+source_list_name+'.csv'
source_list = spark.read.load(source_list_path,format="csv", inferSchema="false", header="false", quote= '"')
source_list = [row['_c0'] for row in source_list.collect()]


try:



    cf.print_fixer_status(

        current_count = '**',
        total_count   ='**',
        fix_type      = 'common', 
        fix_name      = this_fix_name
        
        )
   
   
    # this is the lab_result_cm table for example no need for a source table 
    input_table             = spark.read.load(input_data_folder_path+examined_table_name,format="csv", sep="\t", inferSchema="false", header="true", quote= '"')
    
    # Filter rows where the actual column's value is in loinc_list
    dropped_loincs = input_table.filter(input_table[source_column].isin(source_list))

    #clean the original table of bad loincs
    cleaned_loinc_table = input_table.filter((col(source_column).isNull()) | (~col(source_column).isin(source_list)))


   
    
    cf.write_pyspark_output_file(
                            payspark_df = cleaned_loinc_table,
                            output_file_name = fixed_table_name ,
                            output_data_folder_path= output_data_folder_path)


    cf.write_pyspark_output_file(
                            payspark_df = dropped_loincs,
                            output_file_name = f"{examined_table_name.replace('.csv','')}_dropped_loincs.csv" ,
                            output_data_folder_path= output_data_folder_path+ "/fixers_output/"+examined_table_name_parsed+"_fixer/"+this_fix_name+"/")






    spark.stop()



except Exception as e:

    spark.stop()
    cf.print_failure_message(
                            folder  = input_data_folder,
                            partner = input_partner_name.lower(),
                            job     = this_fix_name )

    cf.print_with_style(str(e), 'danger red')



