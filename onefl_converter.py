
from commonFunctions import CommonFuncitons
import importlib
import sys
import os
import subprocess
import pyspark
from pyspark.sql import SparkSession
import argparse
from datetime import datetime
import pytz


spark = SparkSession.builder.master("spark://master:7077").appName("Initial Run").getOrCreate()
spark.sparkContext.setLogLevel('OFF')
spark.stop()

print("""

                            ▄█  ░█▀▀▀ ░█    　 ░█▀▀█ ░█▀▀▀█ ░█▄ ░█ ░█  ░█ ░█▀▀▀ ░█▀▀█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ 　 █▀█   █▀▀█ 
                             █  ░█▀▀▀ ░█    　 ░█    ░█  ░█ ░█░█░█  ░█░█  ░█▀▀▀ ░█▄▄▀  ░█   ░█▀▀▀ ░█▄▄▀ 　  ▄▀   █  █ 
                            ▄█▄ ░█    ░█▄▄█ 　 ░█▄▄█ ░█▄▄▄█ ░█  ▀█   ▀▄▀  ░█▄▄▄ ░█ ░█  ░█   ░█▄▄▄ ░█ ░█ 　 █▄▄ ▄ █▄▄█                                                                                                                                            
                                                                                                                                                            
                                                                              """
                                                   )






job_num = 0

# spark = SparkSession.builder.master("spark://master:7077").appName("onefl_converter").getOrCreate()

###################################################################################################################################
# parsing the input arguments to select the partner name
###################################################################################################################################


parser = argparse.ArgumentParser()

parser.add_argument("-j", "--job", nargs="+")
parser.add_argument("-p", "--partner")
parser.add_argument("-t", "--table", nargs="+")
parser.add_argument("-db", "--database")
parser.add_argument("-s", "--db_server")
parser.add_argument("-f", "--data_folder",nargs="+")




args = parser.parse_args()

input_jobs = args.job
input_partner = args.partner.lower()
input_tables = args.table
input_db = args.database
input_db_server = args.db_server
input_data_folders = args.data_folder




cf =CommonFuncitons(input_partner)

###################################################################################################################################
# This function will get all the created formatter python script and return a list of thier names
###################################################################################################################################
def get_partner_formatters_list(partner):

    folder_path = '/app/partners/'+partner.lower()+'/formatting_scripts/'
    suffix = 'formatter.py' 
    file_names = os.listdir(folder_path)

    partner_formatters_list = [file for file in file_names if file.endswith(suffix)]

    return partner_formatters_list

###################################################################################################################################
# This function will get all the created mappers python script and return a list of thier names
###################################################################################################################################

def get_partner_mappers_list():


        folder_path = '/app/mapping_scripts/'
        suffix = 'mapper.py' 
        file_names = os.listdir(folder_path)

        partner_mappers_list = [file for file in file_names if file.endswith(suffix)]

        return partner_mappers_list

###################################################################################################################################
# This function will get all the list names of all the mapped files
###################################################################################################################################

def get_partner_uploads_list(folder_path):

       
        prefix = 'mapped_' 
        file_names = os.listdir(folder_path)

        mapped_tables_list = [file for file in file_names if file.startswith(prefix)]

        return mapped_tables_list








###################################################################################################################################
# This function will run the formatter script for a single table
###################################################################################################################################

def run_formatter(partner, formatter, folder):

    global job_num

    job_num = job_num +1
    cf.print_run_status(job_num,total_jobs_count,formatter, folder, partner)


    command = ["python", "/app/partners/"+partner+"/formatting_scripts/"+formatter, '-f', folder ]
    # Execute the command
    subprocess.run(" ".join(command), shell=True)


###################################################################################################################################
# This function will run the mapper script for a single table
###################################################################################################################################
def run_mapper(partner, mapper, folder):

    global job_num

    job_num = job_num +1
    cf.print_run_status(job_num,total_jobs_count, mapper, folder, partner)

    command = ["python", "/app/mapping_scripts/"+mapper,"-p",partner, '-f', folder ]
    # Execute the command
    subprocess.run(" ".join(command), shell=True)

    

###################################################################################################################################
# This function will run the formatter scripts specified by the user
###################################################################################################################################
def run_formatters_jobs(folder):

    global total_fomatters_count
    if 'all' in input_tables:

        partner_formatters_list = get_partner_formatters_list(input_partner)

        total_fomatters_count = len(partner_formatters_list)

        for formatter  in partner_formatters_list:
            run_formatter(input_partner,formatter,folder)
            
    else:

        for table in input_tables:

            formatter = table.lower()+"_formatter.py"
            run_formatter(input_partner,formatter, folder)
###################################################################################################################################
# This function will run the mapper scripts specified by the user
###################################################################################################################################

def run_mappers_jobs(folder):

    global total_mappers_count

    if 'all' in input_tables:

        partner_mappers_list = get_partner_mappers_list()
        # total_mappers_count = len(partner_mappers_list)


        for mapper  in partner_mappers_list:
            run_mapper(input_partner,mapper, folder)
    else:

        for table in input_tables:
            mapper = table.lower()+"_mapper.py"
            run_mapper(input_partner,mapper, folder)


###################################################################################################################################
# This function will run upload for all tables to the data base specified by the user 
###################################################################################################################################

def run_upload_jobs(folder):

    mapped_files_path = '/app/partners/'+input_partner.lower()+'/data/mapper_output/'+folder+"/"
    global total_uploads_count
    global job_num

    if 'all' in input_tables:

        partner_uploads_list = get_partner_uploads_list(mapped_files_path)
        # total_uploads_count = len(partner_uploads_list)

        

        for file_name  in partner_uploads_list:

            table_name = file_name.replace('mapped_',"").replace('.csv',"")

            job_num = job_num +1
            cf.print_run_status(job_num,total_jobs_count, f"upload {file_name}", folder, input_partner)

            cf.db_upload(db= input_db,
                         db_server=input_db_server,
                         schema=folder,
                         file_name=file_name, 
                         table_name = table_name.upper(),
                         file_path= mapped_files_path
                          )
    else:

        for table in input_tables:
            mapped_table_name = "mapped_"+table.lower()+".csv"

            job_num = job_num +1
            cf.print_run_status(job_num,total_jobs_count, f"upload {mapped_table_name}", folder, input_partner)

            cf.db_upload(db= input_db,
                         db_server=input_db_server,
                         schema=folder,
                         file_name=mapped_table_name, 
                         table_name = table.upper(),
                         file_path= mapped_files_path
                          )




###################################################################################################################################
# checking for correct input
###################################################################################################################################

if  not cf.valid_partner_name(input_partner):

    print("Error: Unrecognized partner "+input_partner+" !!!!!")
    sys.exit()


valid_jobs = ['all','map','format','upload']

for job in input_jobs:
   
    if job not in valid_jobs:

        print(job+ " is not a valid job!!!!!! Please enter a valid job name eg. -j format or -j map, or -j all")
        sys.exit()


if 'format' in input_jobs or 'all' in input_jobs:

    if input_data_folders == "" or input_data_folders == None:

        print("Please enter a valid data folder name !!!!!")
        sys.exit()
    else:

        for folder in input_data_folders:

            path = f"/data/{folder}"

            if not os.path.exists(path):

                print("Path  "+path+" does not exits !!!!!!!")
                sys.exit()







# if 'ALL' not in input_tables:

#     for table in input_tables :

#         if table.upper() not in pcornet_tables:

#             print( table + " is not a valid table name!!!!!! Please enter a valid table name eg. -t all or -t demographic")
#             sys.exit()
    





###################################################################################################################################
# Getting Jobs count
###################################################################################################################################

global total_jobs_count

folders_count = len(input_data_folders)


if 'all' in  input_jobs:
    jobs_count = 3
else:
    jobs_count = len(input_jobs)

if 'all' in input_tables:
    tables_count = len(get_partner_formatters_list(input_partner))
else:
    tables_count = len(input_tables)

total_jobs_count = folders_count * jobs_count * tables_count


###################################################################################################################################
# submitting the jobs to be run
###################################################################################################################################
 

for folder in input_data_folders:


    if  'all' in input_jobs:

        run_formatters_jobs(folder)
        run_mappers_jobs(folder)
        run_upload_jobs(folder)

    else :


        if  'format' in input_jobs:
            run_formatters_jobs(folder)

        if  'map' in input_jobs:
            run_mappers_jobs(folder)

        if  'upload' in input_jobs:
            run_upload_jobs(folder)

        

    

print("""

                                                    ▀▀█▀▀ ░█ ░█ ░█▀▀▀ 　 ░█▀▀▀ ░█▄ ░█ ░█▀▀▄ 　 █ 
                                                     ░█   ░█▀▀█ ░█▀▀▀ 　 ░█▀▀▀ ░█░█░█ ░█ ░█ 　 ▀ 
                                                     ░█   ░█ ░█ ░█▄▄▄ 　 ░█▄▄▄ ░█  ▀█ ░█▄▄▀ 　 ▄
            
    """)
             