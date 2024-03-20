
###################################################################################################################################
# This class will host all the common functions used in the mappings by diffrenet mapping scripts
###################################################################################################################################



from itertools import chain
from Crypto.Hash import SHA
from Crypto.Cipher import XOR
from base64 import b64decode, b64encode
from pyspark.sql.functions import udf, col, count, desc, upper, round,  lit
from pyspark.sql import SparkSession 
from pyspark import SparkConf, SparkContext
import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import pyspark
import time
import subprocess 
from pyspark.sql.types import StructType, StructField, StringType, NullType
import sys
from spark_secrets.py import * 
from pyspark.conf import SparkConf
import pandas as pd
from urllib import parse
from datetime import datetime
import pytz
from dateutil import parser as dp
import pyspark.sql.functions as F
import os
import importlib
import openpyxl




POOL_SIZE      = 10
MAX_OVERFLOW   = 5
POOL_RECYCLE   = 3600
BCP_DRIVER     = 'mssql'
  

class CommonFuncitons:


    def __init__(self, partner):




        self.partner = partner # specifying the partner / used for the hashing
        # print(self.partner)
        # sys.exit()
        self.get_time_from_datetime_udf = udf(self.get_time_from_datetime, StringType())
        self.get_date_from_datetime_udf = udf(self.get_date_from_datetime, StringType())
        self.format_date_udf = udf(self.format_date, StringType())
        self.format_time_udf = udf(self.format_time, StringType())
        self.encrypt_id_udf = udf(self.encrypt_id, StringType())
        self.get_current_time_udf = udf(self.get_current_time, StringType())
        self.get_date_from_date_str_with_default_value_udf = udf(self.get_date_from_date_str_with_default_value, StringType())
        self.get_datetime_from_date_str_with_default_value_udf = udf(self.get_datetime_from_date_str_with_default_value, StringType())
        self.copy_if_float_udf= udf(self.copy_if_float, StringType())

        






    


###################################################################################################################################
# This function will return the xor hashed value based on the partner name and input value/id
###################################################################################################################################

   
   

    # @classmethod
    def encrypt_id(cls, id):


            HASHING_KEY = SHA.new(SEED.encode('utf-8')).digest()

            cipher = XOR.new(HASHING_KEY)

            return b64encode(cipher.encrypt('{}{}'.format(cls.partner, id))).decode()



###################################################################################################################################
# This function will return the current datetime
###################################################################################################################################

   

    @classmethod
    def get_current_time(cls):

       # Set the timezone to Eastern Time (New York)
        eastern_timezone = pytz.timezone("US/Eastern")

        # Get the current time in the Eastern Time Zone
        current_time = datetime.now(eastern_timezone)

        # Define the desired time format
        time_format = "%Y-%m-%d %H:%M:%S"

        # Format and print the current time
        formatted_time = current_time.strftime(time_format)

        return formatted_time


        
    
###################################################################################################################################
# This function will output a pyspark dataframe and combine all the sub files into one file and delete the temprary files
###################################################################################################################################

   

    @classmethod
    def write_pyspark_output_file(cls,payspark_df, output_file_name, output_data_folder_path ):
        pass

        # pcornet_cdm = PcornetCDM()

        # print(pcornet_cdm.get_cdm_table_fields_list('demographic'))
    def write_pyspark_output_file(cls,payspark_df, output_file_name, output_data_folder_path ):

        # pcornet_cdm = PcornetCDM()

        # print(pcornet_cdm.get_cdm_table_fields_list('demographic'))

        date_format_pattern = "yyyy-MM-dd"
        work_directory = output_data_folder_path+"tmp_"+output_file_name

        payspark_df = payspark_df.select([
            F.lit(None).cast('string').alias(i.name)
            if isinstance(i.dataType, NullType)
            else i.name
            for i in payspark_df.schema
            ])
        
        payspark_df.coalesce(1).write.format("csv").option("header", True).option("nullValue",None).option("delimiter", "\t").mode("overwrite").save(work_directory)

        

        command = ["cp", work_directory+"/part-*.csv", output_data_folder_path+output_file_name]
        # Execute the command
        subprocess.run(" ".join(command), shell=True)

        command = ["rm","-r", work_directory]
        # Execute the command
        subprocess.run(" ".join(command), shell=True)



###################################################################################################################################
# This function will output the mapping gaps for the passed formatted file name
###################################################################################################################################

   

    @classmethod
    def get_mapping_gap(cls,partner,file_name,table_name, file_path,folder_name):


        spark = SparkSession.builder.master("spark://master:7077").appName("MAPPING GAPS").getOrCreate()

        complete_file_path = file_path+'/formatted_'+file_name.lower()+'.csv'
        partner_dictionaries_path = "partners."+partner+".dictionaries"
        partner_dictionaries = importlib.import_module(partner_dictionaries_path)

        mapping_dicionaries_list = []

        for key, value in partner_dictionaries.__dict__.items():


            
            if  file_name.lower() in key and '_dict' in key:

                # get the field name

                prefix = '@' #logic added to only remove the first word from the dictinary name

                temp_key = prefix+key


                field_name = temp_key.replace(prefix+file_name.lower()+'_',"").replace('_dict',"").upper()

                

                # get the aggreated data from the formatter for the field 

                aggregated_values = cls.get_aggregate_value_from_table(complete_file_path,field_name,spark)

                # aggregated_values.show()

                # get and output the aggreated data that has mapping 

                dictionary_dataframe = spark.createDataFrame(value.items(), ["dict_key", "dict_value"])
                # dictionary_dataframe.show()
                # aggregated_values.show()


                if 'UNIT' in field_name:
                    joined_df = aggregated_values.join(dictionary_dataframe, dictionary_dataframe['dict_key']==aggregated_values[field_name], how ="left").orderBy(desc("count"))
                else:
                    joined_df = aggregated_values.join(dictionary_dataframe, upper(dictionary_dataframe['dict_key'])==upper(aggregated_values[field_name]), how ="left").orderBy(desc("count"))

                # joined_df = aggregated_values.join(dictionary_dataframe, upper(dictionary_dataframe['dict_key'])==upper(aggregated_values[field_name]), how ="left")

                # joined_df.show()

                cls.diagnos_dictionary(dictionary_dataframe, file_path, key, file_name.lower())
                cls.daignos_mapping(joined_df, file_path, key, field_name, dictionary_dataframe, file_name.lower())

               


                # value_with_mapping =  spark.createDataFrame(dictionary_data.items(), ["GroupedName", "Value"])


                # get and output the aggregated tata that has no mapping

                # output a suggested new dicitonary



                mapping_dicionaries_list.append(key)
                # print(field_name)

        # Print the list of names
        # print(mapping_dicionaries_list)



       

        spark.stop()



###################################################################################################################################
# This function will diagnos a given dictionary data frame
########################################################################################################

    @classmethod
    def diagnos_dictionary(cls,dictionary_dataframe, file_path, file_name, table_name):

        # getting values that mapped to null or some flavor of null like 'OT, 'NI', and "UN
        filtered_df = dictionary_dataframe.filter((col("dict_value").isin("NI", "OT", "UN")) | (col("dict_value").isNull()) | (col("dict_value") == ""))

        out_file_path = file_path.replace('formatter','mapping_gaps')+"/"+table_name+"/mapping_to_flavor_of_null/"
        output_file_name = file_name+"_flavor_of_null.csv"


        cls.write_pyspark_output_file(cls,filtered_df, output_file_name, out_file_path )
           


###################################################################################################################################
# This function will diagnos a given joind dictionary dataframe
########################################################################################################

    @classmethod
    def daignos_mapping(cls,joined_df, file_path, file_name, field_name, dictionary_dataframe, table_name):


        try:

            # output all mapping
            all_values_df = joined_df.select(joined_df[field_name],joined_df['dict_value'],joined_df['count'],joined_df['percent'])
            all_mapping_out_file_path = file_path.replace('formatter','mapping_gaps')+"/"+table_name+"/all_mapping/"
            all_mapping_output_file_name = file_name+"_all_mapping.csv"
            cls.write_pyspark_output_file(cls,all_values_df, all_mapping_output_file_name, all_mapping_out_file_path )
            
            # output missing mapping
            missing_values_df = all_values_df.filter(col("dict_value").isNull() )

            missing_mapping_out_file_path = file_path.replace('formatter','mapping_gaps')+"/"+table_name+"/missing_mapping/"
            missing_mapping_output_file_name = file_name+"_missing_mapping.csv"
            cls.write_pyspark_output_file(cls,missing_values_df, missing_mapping_output_file_name, missing_mapping_out_file_path )

            # output suggested mapping

            
            to_be_added_field = missing_values_df.select(

                    missing_values_df[field_name].alias('dict_key'),
                    lit('').alias('dict_value'),


            )

            unioned_df= dictionary_dataframe.union(to_be_added_field)
            # unioned_df.show()
            suggested_mapping_out_file_path = file_path.replace('formatter','mapping_gaps')+"/"+table_name+"/suggested_mapping/"

            out_file_name = suggested_mapping_out_file_path+"suggested_"+file_name+".py"

            os.makedirs(os.path.dirname(out_file_name), exist_ok=True)


            formatted_text = unioned_df.rdd \
                .map(lambda row: f'       {cls.process_key(row["dict_key"],row["dict_value"],file_name, 20)}  :  "{row["dict_value"]}",') \
                .collect()

            # Join the formatted strings with newline characters
            formatted_text = "\n".join(formatted_text)

            # Write the formatted text to a text file
        
            first_line = "\n\n"+file_name+ " = {\n\n"
            last_line = "   \n\n}"

            with open(out_file_name, "w+") as file:
                file.write(first_line)
                file.write(formatted_text)
                file.write(last_line)


        except Exception as e:

            

            cls.print_with_style(str(e), 'danger red')
            
            
    
###################################################################################################################################
# 
########################################################################################################

    @classmethod
    def process_row(cls,row, file):


            print(row)


            key = cls.append_spaces(row.dict_key, 20),

            text = row.dict_value + '\n'

            # text = row['dict_value']

            file.write(text)


                
               

###################################################################################################################################
# 
########################################################################################################

    @classmethod
    def process_key(cls, key, value,file_name, size):

            key = str(key)

            if 'unit' not in file_name and 'UNIT' not in file_name:

                key = key.upper()

            key = '"'+key+'"'


            if value == "" or value == None:

                key = '# '+key

            while len(key) < size:

                key = key + ' '

            return key





###################################################################################################################################
# This function return and aggreated dataframe for a given table
###################################################################################################################################


    @classmethod
    def get_aggregate_value_from_table(cls,file_path,field_name,spark):

        df = cls.spark_read(file_path, spark)
        row_count= df.count()

        aggregated_df = df.groupBy(field_name).agg(count("*").alias("count"))
        aggregated_df_with_percent= aggregated_df.select(

                aggregated_df[field_name],
                aggregated_df['count'],
                round((aggregated_df['count']/row_count)*100,2).alias('percent')


        )
        



        return aggregated_df_with_percent




###################################################################################################################################
# This function will upload a pyspark df to mssql table in a specified server/dabase
###################################################################################################################################

   

    @classmethod
    def db_upload(cls,db, db_server,schema,file_name,table_name, file_path,folder_name):

        date_format_pattern = "yyyy-MM-dd"

        spark = SparkSession.builder.master("spark://master:7077").appName("MSSQL Upload").getOrCreate()

        try:
            conf = SparkConf()
            conf.set("spark.driver.extraClassPath", "mssql-jdbc-driver.jar")
            file_df = spark.read.option("inferSchema", "false").load(file_path+file_name+'*',format="csv", sep="\t", inferSchema="false", header="true",  quote= '"')
            
            # string_columns = [f'CAST({col} AS STRING)' for file_df in file_df.columns]
            string_columns = [f'CAST(`{col}` AS STRING) AS `{col}`' for col in file_df.columns]
            result_df = file_df.selectExpr(*string_columns)

            
            jdbc_url = f"jdbc:sqlserver://{db_server};databaseName={db}"
            
            if schema != None:
                properties = {
                    "user": DB_USER,
                    "password": DB_PASS,
                    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
                    "trustServerCertificate": "true",
                    "createTableColumnTypes": schema}
            else:
                properties = {
                    "user": DB_USER,
                    "password": DB_PASS,
                    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
                    "trustServerCertificate": "true"}


            table_name = f"PYSPARK_{folder_name}_{table_name}"
            
            result_df.write.jdbc(url=jdbc_url, table=table_name, mode="overwrite", properties=properties)

            spark.stop()
        except Exception as e:

            spark.stop()
            

            cls.print_with_style(str(e), 'danger red')



###################################################################################################################################
# This function will return a list of folder in a given path
###################################################################################################################################
    @classmethod
    def get_folders_list(cls, path):

       
        
        folders_names = os.listdir(path)

        folders_names_list = [file for file in folders_names if file]

        return folders_names_list


###################################################################################################################################
# This function generate a mapping report as a form of an excel file
###################################################################################################################################


    @classmethod
    def generate_mapping_report(cls,mapping_gaps_output_folder_path, folder, partner):

        spark = cls.get_spark_session('generate mapping report')

        empty_columns = pd.DataFrame(columns=[""] * 2)
        # Path to the Excel file
        excel_file_path = mapping_gaps_output_folder_path + partner+'_'+folder+"_mapping_report.xlsx"

        # Initialize a workbook object
        wb = openpyxl.Workbook()



        tables_list = cls.get_folders_list(mapping_gaps_output_folder_path)

        for table in tables_list :

           


            if 'mapping_report' not in table:

                ws = wb.create_sheet(title=table)

                combined_pd = empty_columns


                table_all_mappings_path = mapping_gaps_output_folder_path +"/"+table+"/all_mapping/"

                table_all_mapping_files_list = cls.get_folders_list(table_all_mappings_path)

                for mapping_file in table_all_mapping_files_list:

                    mapping_df =  cls.spark_read(table_all_mappings_path+mapping_file, spark)

                    pandas_df = mapping_df.toPandas()
                    combined_pd = pd.concat([combined_pd, empty_columns, pandas_df], axis=1)


                    for col_idx, col_name in enumerate(combined_pd.columns, 1):
                        ws.cell(row=1, column=col_idx, value=col_name)


                    for row_idx, row in enumerate(combined_pd.values, 2):  # Start from row 2 (after header row)
                        for col_idx, value in enumerate(row, 1):
                            cell = ws.cell(row=row_idx, column=col_idx, value=value)

                            # Calculate the width of the cell based on the length of the value
                            if isinstance(value, str):
                                width = len(value)
                            else:
                                width = len(str(value))

                            # Update the column width if necessary
                            if width > ws.column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width:
                                ws.column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = width


        if 'Sheet' in wb.sheetnames:
            # Remove the sheet
            wb.remove(wb['Sheet'])

        wb.save(excel_file_path)




        spark.stop()



###################################################################################################################################
# This function will return a pysark dataframe for a givin file path
###################################################################################################################################


    @classmethod
    def spark_read(cls,file_path, spark):

        return spark.read.option("inferSchema", "false").load(file_path,format="csv",   sep="\t", inferSchema="false", header="true",  quote= '"')



###################################################################################################################################
# This function will append any additional fields that are not in the Pcornet CDM to the mapper output
###################################################################################################################################

   

    @classmethod
    def append_additional_fields(cls,mapped_df, file_name, formatted_data_folder_path,join_field, spark ):


        # read the formatted file
        formatted_file = spark.read.load(formatted_data_folder_path+file_name,format="csv", sep="\t", inferSchema="true", header="true", quote= '"')
        
        #get the headers from the formatted and the mapped files for comparison
        formatted_file_columns = formatted_file.columns
        mapped_df_columns = mapped_df.columns


        # Identify common headers
        common_headers = set(mapped_df_columns).intersection(formatted_file_columns)
        common_headers_without_the_join_field = [item for item in common_headers if item != join_field]

        # Drop common headers from the second DataFrame
        additional_fields_data = formatted_file.drop(*common_headers_without_the_join_field)
        
        #Renaming the join field to avoid conflect during the join
        join_field_temp_name = join_field+"_new"

        additional_fields_data = additional_fields_data.withColumnRenamed(join_field, join_field_temp_name)
        
        # Join DataFrames based on the "Name" column
        appended_payspark_data_frame = mapped_df.join(additional_fields_data, mapped_df["JOIN_FIELD"]==additional_fields_data[join_field_temp_name])
       
       #Dropping the temporary join fields

        columns_to_drop = ["JOIN_FIELD",join_field_temp_name ]
        appended_payspark_data_frame = appended_payspark_data_frame.drop(*columns_to_drop)

        return appended_payspark_data_frame
        


###################################################################################################################################
# This function will convert all known time formats to the '%H:%M'format
###################################################################################################################################

    @staticmethod
    def format_time( val):
        """ Convenience method to try all known formats """

        try:
            parsed_time = dp.parse(val)
        except Exception as exc:
           
            return ""
        return parsed_time.strftime('%H:%M')


###################################################################################################################################
# This will ensure the value is a float or it will return None
###################################################################################################################################

    @staticmethod
    def copy_if_float( val):
        """ Convenience method to try all known formats """
        if not val:
            return None
        try:
            return float(val)
        except:

            return None



###################################################################################################################################
# This function will convert all known date formats to the '%Y-%m-%d format
###################################################################################################################################

   
    @staticmethod
    def format_date( val):
        """ Convenience method to try all known formats """

        try:
            parsed_date = dp.parse(val)
        except:
           
            return None

        return parsed_date.strftime('%Y-%m-%d')




###################################################################################################################################
# This function will return the time portion from a datetime value
###################################################################################################################################

   
    @staticmethod
    def get_time_from_datetime(  dateTime):
        
            try:
                
                return str(dateTime.time().strftime('%H:%M:%S'))[0:5]
            except:
                return None

###################################################################################################################################
# This function will return the date portion from a datetime value
###################################################################################################################################

   
    @staticmethod
    def get_date_from_datetime(  dateTime):
        
        try:
            
            return str(dateTime.strftime("%Y-%m-%d"))
        except:
            return None

        
  
###################################################################################################################################
# This function will validate if a giving partenr name is valid or not
###################################################################################################################################

   

    @classmethod
    def valid_partner_name(cls, input_partner_name ):

        partners_list = ["omop_partner_1","pcornet_partner_1","jhs"]

        if input_partner_name in  partners_list:

            return True
        else:
            return None

###################################################################################################################################
# This function will create and return a spark session
###################################################################################################################################

    @classmethod
    def get_spark_session(cls, appName):
        try:
            spark.stop()
        except:
            None

        spark = SparkSession.builder.master("spark://master:7077").appName(appName).getOrCreate()
        spark.sparkContext.setLogLevel('OFF')

        return spark

###################################################################################################################################
    @classmethod
    def print_failure_message(cls, folder,partner, job):


        current_utc_datetime = datetime.utcnow()
        new_york_tz = pytz.timezone('America/New_York')

        current_ny_datetime = current_utc_datetime.replace(tzinfo=pytz.utc).astimezone(new_york_tz)

        formatted_ny_datetime = current_ny_datetime.strftime("%Y-%m-%d %H:%M:%S %Z")

        message = formatted_ny_datetime


        while len(message) < 39:
            message = message + ' '


        message = message + "--Partner: " + partner

    
        while len(message) < 55:
            message = message + ' '


        message = message + "--Folder: " + folder

    
        while len(message) < 80:
            message = message + ' '
        

        message = message+' --Running '+ job+ ' Failed!!!' 

        while len(message) < 125:
            message = message + ' '

        while len(message) < 145:
            message = message + '.'


        cls.print_with_style(message, 'danger red')


###################################################################################################################################
# This function will get all the created mappers python script and return a list of thier names
###################################################################################################################################
    @classmethod
    def print_run_status(cls,job_num,total_jobs_count, job, folder, partner):
        


        current_utc_datetime = datetime.utcnow()
        new_york_tz = pytz.timezone('America/New_York')

        current_ny_datetime = current_utc_datetime.replace(tzinfo=pytz.utc).astimezone(new_york_tz)

        formatted_ny_datetime = current_ny_datetime.strftime("%Y-%m-%d %H:%M:%S %Z")

        message = formatted_ny_datetime

        while len(message) < 25:
            message = message + ' '

        message = message + 'Job: '+str(job_num)+'/'+str(total_jobs_count)
        while len(message) < 39:
            message = message + ' '

        message = message + "--Partner: " + partner

    
        while len(message) < 55:
            message = message + ' '


        message = message + "--Folder: " + folder

    
        while len(message) < 80:
            message = message + ' '
        

        message = message+' --Running '+job 

        while len(message) < 125:
            message = message + ' '

        while len(message) < 145:
            message = message + '.'


        cls.print_with_style(message, 'matrix green')

###################################################################################################################################
# This function will print a text with matrix green color
###################################################################################################################################

    @classmethod
    def print_with_style(cls, text, color):

        if color == 'matrix green':

            bold_code = '\033[1m'
            color_code = '\033[92m'
            reset_code = '\033[0m'  # Reset to default style
       
        if color == 'danger red':

            bold_code = '\033[1m'
            color_code = RED='\033[0;31m'
            reset_code = '\033[0m'  # Reset to default style
        
        # Print bold green text
        print(bold_code + color_code + text + reset_code)


###################################################################################################################################
# 
###################################################################################################################################

    @staticmethod
    def get_date_from_date_str_with_default_value(  input_date):

            try:
                
                return  str(datetime.strptime(input_date, "%Y-%m-%d").date())
            except:
                return '1900-01-01'        

 
###################################################################################################################################
# T
###################################################################################################################################



   
    @staticmethod
    def get_datetime_from_date_str_with_default_value(  input_date):
        
        try:
            
            return str(datetime.strptime(input_date+ " 00:00:00","%Y-%m-%d %H:%M:%S"))
        except:
            return '1900-01-01 00:00:00'    