
###################################################################################################################################
# This class will host all the common functions used in the mappings by diffrenet mapping scripts
###################################################################################################################################



from itertools import chain
from Crypto.Hash import SHA
from Crypto.Cipher import XOR
from base64 import b64decode, b64encode
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import pyspark
import time
import subprocess
from pyspark.sql.types import StructType, StructField, StringType
import sys
from secrets import * 
from pcornet_cdm import PcornetCDM
from pyspark.conf import SparkConf
import pandas as pd
from urllib import parse
from datetime import datetime
import pytz
from dateutil import parser as dp


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
        """
        :rtype string: representation of the current time
        in the format "YYYY-MM-DD HH:MM:SS"
        """
        return time.strftime("%Y-%m-%d %H:%M:%S")


        
    
###################################################################################################################################
# This function will output a pyspark dataframe and combine all the sub files into one file and delete the temprary files
###################################################################################################################################

   

    @classmethod
    def write_pyspark_output_file(cls,payspark_df, output_file_name, output_data_folder_path ):

        # pcornet_cdm = PcornetCDM()

        # print(pcornet_cdm.get_cdm_table_fields_list('demographic'))

        date_format_pattern = "yyyy-MM-dd"
        work_directory = output_data_folder_path+"tmp_"+output_file_name
        
        payspark_df.coalesce(1).write.format("csv").option("header", True).option("nullValue",None).option("delimiter", "\t").mode("overwrite").save(work_directory)

        

        command = ["cp", work_directory+"/part-*.csv", output_data_folder_path+output_file_name]
        # Execute the command
        subprocess.run(" ".join(command), shell=True)

        command = ["rm","-r", work_directory]
        # Execute the command
        subprocess.run(" ".join(command), shell=True)





###################################################################################################################################
# This function will upload a pyspark df to mssql table in a specified server/dabase
###################################################################################################################################

   

    @classmethod
    def db_upload(cls,db, db_server,schema,file_name,table_name, file_path ):

        date_format_pattern = "yyyy-MM-dd"

        spark = SparkSession.builder.master("spark://master:7077").appName("MSSQL Upload").getOrCreate()


        conf = SparkConf()
        conf.set("spark.driver.extraClassPath", "mssql-jdbc-driver.jar")
        file_df = spark.read.option("inferSchema", "false").load(file_path+file_name,format="csv", sep="\t", inferSchema="false", header="true",  quote= '"')
        
        # string_columns = [f'CAST({col} AS STRING)' for file_df in file_df.columns]
        string_columns = [f'CAST(`{col}` AS STRING) AS `{col}`' for col in file_df.columns]
        result_df = file_df.selectExpr(*string_columns)

        
        jdbc_url = f"jdbc:sqlserver://{db_server};databaseName={db}"
        properties = {
            "user": DB_USER,
            "password": DB_PASS,
            "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
            "trustServerCertificate": "true"

            }

        table_name = f"PYSPARK_{schema}_{table_name}"
        
        result_df.write.jdbc(url=jdbc_url, table=table_name, mode="overwrite", properties=properties)


        spark.stop()








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
        if not val:
            return None
        try:
            parsed_time = dp.parse(val)
        except Exception as exc:
           
            return ""
        return parsed_time.strftime('%H:%M')


###################################################################################################################################
# This function will convert all known date formats to the '%Y-%m-%d format
###################################################################################################################################

   
    @staticmethod
    def format_date( val):
        """ Convenience method to try all known formats """
        if not val or val == 'NULL':
            return None
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
                
                return str(dateTime.time().strftime('%H:%M:%S'))
            except:
                return None

###################################################################################################################################
# This function will return the date portion from a datetime value
###################################################################################################################################

   
    @staticmethod
    def get_date_from_datetime(  dateTime):
        
        try:
            
            return str(dateTime.date().strftime("%Y-%m-%d"))
        except:
            return None

        
  
###################################################################################################################################
# This function will validate if a giving partenr name is valid or not
###################################################################################################################################

   

    @classmethod
    def valid_partner_name(cls, input_partner_name ):

        partners_list = ["omop_partner_1","pcornet_partner_1"]

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

