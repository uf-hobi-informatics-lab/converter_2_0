
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
from settings import  VALID_JOBS

from PIL import Image


spark = SparkSession.builder.master("spark://master:7077").appName("Initial Run").getOrCreate()
spark.sparkContext.setLogLevel('OFF')
spark.stop()








 

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
parser.add_argument("-dt", "--database_type")



args = parser.parse_args()

input_jobs = args.job
input_partner = args.partner.lower()
input_tables = args.table
input_db = args.database
input_db_server = args.db_server
input_data_folders = args.data_folder
input_db_type = args.database_type




cf =CommonFuncitons(input_partner)


# cf.display_logo()
# sys.exit()

print("""

                            ▄█  ░█▀▀▀ ░█       ░█▀▀█ ░█ ░█  █▀▀█ ░█▄ ░█ ░█▀▀█ ░█▀▀▀ ▀█▀ ░█▄ ░█  █▀▀█ ▀▀█▀▀ ░█▀▀▀█ ░█▀▀█ 
                             █  ░█▀▀▀ ░█    ▀▀ ░█    ░█▀▀█ ░█▄▄█ ░█░█░█ ░█ ▄▄ ░█▀▀▀ ░█  ░█░█░█ ░█▄▄█  ░█   ░█  ░█ ░█▄▄▀ 
                            ▄█▄ ░█    ░█▄▄█    ░█▄▄█ ░█ ░█ ░█ ░█ ░█  ▀█ ░█▄▄█ ░█▄▄▄ ▄█▄ ░█  ▀█ ░█ ░█  ░█   ░█▄▄▄█ ░█ ░█

                                                                                                                                                            
                                                                              """
                                                   )

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
# This function will get all the created formatter python script and return a list of thier names
###################################################################################################################################
def get_partner_fixers_list(partner):

    folder_path = '/app/partners/'+partner.lower()+'/fixer_scripts/'
    suffix = 'fixer.py' 
    file_names = os.listdir(folder_path)

    partner_fixers_list = [file for file in file_names if file.endswith(suffix)]

    return partner_fixers_list

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

       
        prefix = 'fixed_' 
        file_names = os.listdir(folder_path)

        fixed_tables_list = [file for file in file_names if file.startswith(prefix)]

        return fixed_tables_list



###################################################################################################################################
# This function will get all the list names of all the formatted files
###################################################################################################################################

def get_partner_formatted_files_list(folder_path):

       
        prefix = 'formatted_' 
        file_names = os.listdir(folder_path)

        formatted_tables_list = [file for file in file_names if file.startswith(prefix)]

        return formatted_tables_list


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
# This function will run the formatter script for a single table
###################################################################################################################################

def run_fixer(partner, fixer, folder):

    global job_num

    job_num = job_num +1
    cf.print_run_status(job_num,total_jobs_count,fixer, folder, partner)


    command = ["python", "/app/partners/"+partner+"/fixer_scripts/"+fixer, '-f', folder ]
    # Execute the command
    subprocess.run(" ".join(command), shell=True)

###################################################################################################################################
# This function will run the deduplicator script for a single table
###################################################################################################################################

def run_deduplicator(partner, input_folder, output_folder):

    global job_num

    # process duplicates for each tablle
    for table in input_tables:
        job_num = job_num +1
        cf.print_run_status(job_num, total_jobs_count, f'{table}_deduplicator.py', os.path.split(input_folder)[1], partner)

        command = ["python", "/app/deduplicator.py", '-f', input_folder, '-of', output_folder , '-t' ]

        # add table list
        command.append(table)

        # Execute the command
        subprocess.run(" ".join(command), shell=True)
###################################################################################################################################
# This function will run the deduplicator script for a single table
###################################################################################################################################

def run_deduplicator(partner, input_folder, output_folder):

    global job_num

    # process duplicates for each tablle
    for table in input_tables:
        job_num = job_num +1
        cf.print_run_status(job_num, total_jobs_count, f'{table}_deduplicator.py', os.path.split(input_folder)[1], partner)

        command = ["python", "/app/deduplicator.py", '-f', input_folder, '-of', output_folder , '-t' ]

        # add table list
        command.append(table)

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
# This function will run the fixer scripts specified by the user
###################################################################################################################################
def run_fixers_jobs(folder):

    global total_fixers_count
    if 'all' in input_tables:

        partner_fixers_list = get_partner_fixers_list(input_partner)

        non_loinc_fixers = [fixer for fixer in partner_fixers_list if "loinc" not in fixer.lower()]
        loinc_mover_fixers = [fixer for fixer in partner_fixers_list if "loinc" in fixer.lower()]
        
        total_fixers_count = len(partner_fixers_list)
        
        # Run all non-loinc fixers
        for fixer in non_loinc_fixers:
            run_fixer(input_partner, fixer, folder)
        
        # Run the loinc_mover
        for fixer in loinc_mover_fixers:
            run_fixer(input_partner, fixer, folder)
            
    else:
        # Run all specified fixers except loinc_mover
        specified_fixers = [table.lower() for table in input_tables if table.lower() != "loinc"]

        for fixer in specified_fixers:
            run_fixer(input_partner, fixer + "_fixer.py", folder)
            
        # If loinc_mover was specified
        if "loinc" in [table.lower() for table in input_tables]:
            run_fixer(input_partner, "loinc_fixer.py", folder)


###################################################################################################################################
# This function will run the deduplicators script
###################################################################################################################################

def run_deduplicator_jobs(folder):

    formatted_files_list_path = '/app/partners/'+input_partner.lower()+'/data/formatter_output/'+folder+"/"


    global total_uploads_count
    global job_num

    if 'all' in input_tables:

        formatted_files_list = get_partner_formatted_files_list(formatted_files_list_path)
        # total_uploads_count = len(partner_uploads_list)

        

        for file_name  in formatted_files_list:

            table_name = file_name.replace('formatted_',"").replace('.csv',"")

            job_num = job_num +1
            cf.print_run_status(job_num,total_jobs_count, f"deduplicating {file_name}", folder, input_partner)

            cf.deduplicate(
                         partner = input_partner,
                         file_name=table_name.upper(), 
                         table_name = table_name.upper(),
                         file_path= formatted_files_list_path,
                         folder_name = folder
                          )
    else:

        for table in input_tables:
            formatted_table_name = "formatted_"+table.lower()+".csv"

            job_num = job_num +1
            cf.print_run_status(job_num,total_jobs_count, f"deduplicating {formatted_table_name}", folder, input_partner)


            cf.deduplicate(
                         partner = input_partner,
                         file_name=table.upper(),
                         table_name = table.upper(),
                         file_path= formatted_files_list_path,
                         folder_name = folder
                          )

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

def run_mapping_gap_jobs(folder):

    formatted_files_list_path = '/app/partners/'+input_partner.lower()+'/data/formatter_output/'+folder+"/"


    global total_uploads_count
    global job_num

    if 'all' in input_tables:

        formatted_files_list = get_partner_formatted_files_list(formatted_files_list_path)
        # total_uploads_count = len(partner_uploads_list)

        

        for file_name  in formatted_files_list:

            table_name = file_name.replace('formatted_',"").replace('.csv',"")

            job_num = job_num +1
            cf.print_run_status(job_num,total_jobs_count, f"mapping gap for {file_name}", folder, input_partner)

            cf.get_mapping_gap(
                         partner = input_partner,
                         file_name=table_name.upper(), 
                         table_name = table_name.upper(),
                         file_path= formatted_files_list_path,
                         folder_name = folder
                          )
    else:

        for table in input_tables:
            formatted_table_name = "formatted_"+table.lower()+".csv"

            job_num = job_num +1
            cf.print_run_status(job_num,total_jobs_count, f"mapping gap for {formatted_table_name}", folder, input_partner)


            cf.get_mapping_gap(
                         partner = input_partner,
                         file_name=table.upper(),
                         table_name = table.upper(),
                         file_path= formatted_files_list_path,
                         folder_name = folder
                          )


###################################################################################################################################
# This function will generate a mapping report as a form of an excel file
###################################################################################################################################

def run_mapping_report_job(folder):

    mapping_gap_output_folder_path = '/app/partners/'+input_partner.lower()+'/data/mapping_gap_output/'+folder+"/"

    global total_uploads_count 
    global job_num

    job_num = job_num +1

    cf.print_run_status(job_num,total_jobs_count, f"Generating the mapping report ", folder, input_partner)

    cf.generate_mapping_report(

        mapping_gap_output_folder_path = mapping_gap_output_folder_path,
        folder = folder,
        partner= input_partner
    )




###################################################################################################################################
# This function will run upload for all tables to the data base specified by the user 
###################################################################################################################################

def run_upload_jobs(folder):



        fixed_files_path = '/app/partners/'+input_partner.lower()+'/data/fixer_output/'+folder+"/"
        global total_uploads_count
        global job_num

        if 'all' in input_tables:

            partner_uploads_list = get_partner_uploads_list(fixed_files_path)
            # total_uploads_count = len(partner_uploads_list)

            

            for file_name  in partner_uploads_list:

                table_name = file_name.replace('fixed_',"").replace('.csv',"")

                job_num = job_num +1
                cf.print_run_status(job_num,total_jobs_count, f"upload {file_name}", folder, input_partner)

                # schema = schemas.get(table_name.upper(), None)

                schemas = cf.get_schemas( table_name.upper(), fixed_files_path)

                cf.db_upload(db= input_db,
                            db_server=input_db_server,
                            schemas=schemas,
                            file_name=file_name, 
                            table_name = table_name.upper(),
                            file_path= fixed_files_path, 
                            folder_name = folder,
                            db_type = input_db_type
                            )
        else:

            for table in input_tables:
                fixed_table_name = "fixed_"+table.lower()+".csv"

                # print(fixed_files_path+fixed_table_name)
                # print(os.path.exists(fixed_files_path+fixed_table_name))

                if os.path.exists(fixed_files_path+fixed_table_name):

                    job_num = job_num +1
                    cf.print_run_status(job_num,total_jobs_count, f"upload {fixed_table_name}", folder, input_partner)

                    # schema = schemas.get(table.upper(), None)

                    schemas = cf.get_schemas(table.upper(),fixed_files_path)

                    cf.db_upload(db= input_db,
                                db_server=input_db_server,
                                schemas=schemas,
                                file_name=fixed_table_name, 
                                table_name = table.upper(),
                                file_path= fixed_files_path,
                                folder_name = folder,
                                db_type = input_db_type
                                )
                    

                else:

                        cf.print_failure_message(
                                                folder  = folder,
                                                partner = input_partner,
                                                job     = 'upload '+ table.lower()  ,
                                                text    =  f"{fixed_table_name} Path does not exist!!!!"
                                                )




###################################################################################################################################
# checking for correct input
###################################################################################################################################

if  not cf.valid_partner_name(input_partner):

    print("Error: Unrecognized partner "+input_partner+" !!!!!")
    sys.exit()



for job in input_jobs:
   
    if job not in VALID_JOBS:

        print(job+ " is not a valid job!!!!!! Please enter a valid job name eg. -j format or -j deduplicate or -j map, or -j all")
        
        sys.exit()


if 'format' in input_jobs or 'all' in input_jobs:

    if input_data_folders == "" or input_data_folders == None:

        print("Please enter a valid data folder name !!!!!")
        sys.exit()
    else:

        for folder in input_data_folders:

            path = f"/data/{folder}"
            # path = f"/app/partners/avh/data/input/{folder}"

            if not os.path.exists(path):

                print("Path  "+path+" does not exits !!!!!!!")
                sys.exit()

# if 'deduplicate' or 'all' in input_jobs:

#     if input_tables == "" or input_tables == None or input_tables == []:
#         print("Please enter a valid data table name !!!!!")
#         sys.exit()

#     else:

#         for folder in input_data_folders:

#             path = f'/app/partners/{input_partner}/data/formatter_output/{folder}'

#             if not os.path.exists(path):

#                 print("Path  "+path+" does not exits !!!!!!!")
#                 sys.exit()


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
    jobs_count = 4
else:
    jobs_count = len(input_jobs)

if 'all' in input_tables:
    tables_count = len(get_partner_formatters_list(input_partner))
else:
    tables_count = len(input_tables)

total_jobs_count = folders_count * jobs_count * tables_count


###################################################################################################################################
# This function will run the dv_mapper script for tables specified by the user 
###################################################################################################################################

def run_dv_mapper_jobs(folder ):
    global job_num
    total_jobs_count = len(input_tables)
    job_num = 0

    # spark = SparkSession.builder \
    #     .appName("Update PATID Column") \
    #     .config("spark.sql.shuffle.partitions", "1000") \
    #     .getOrCreate()

    # Read the mapping table once

    
    dv_mapping_table_path = f'/app/partners/{input_partner}/data/dv_match/{folder}/DV_ORIGINAL_PATID_MAPPING.csv'
    dv_mapper_output_path = f'/app/partners/{input_partner}/data/dv_mapper_output/{folder}/'
    fixed_table_path      = f'/app/partners/{input_partner}/data/fixer_output/{folder}/'
   
    for table_name in input_tables:
        job_num += 1
        cf.print_run_status(job_num, total_jobs_count, f" mapping {table_name} to Datavant ids", "", "")


        cf.dv_match(partner_name=input_partner,
                    folder=folder,
                    dv_mapping_table_path=dv_mapping_table_path,
                    fixed_table_path = fixed_table_path,
                    table_name=table_name,
                    output_path=dv_mapper_output_path,
                    dv_mapper_output_path=dv_mapper_output_path
            
                )





###################################################################################################################################
# submitting the jobs to be run
###################################################################################################################################
 

for folder in input_data_folders:


    if  'all' in input_jobs:

        run_formatters_jobs(folder)
        run_mapping_gap_jobs(folder)
        run_mapping_report_job(folder)
        run_deduplicator_jobs(folder)
        run_mappers_jobs(folder)
        run_fixers_jobs(folder)
        run_upload_jobs(folder)

    else :


        if  'format' in input_jobs:
            run_formatters_jobs(folder)

        if  'mapping_gap' in input_jobs:
            run_mapping_gap_jobs(folder)

        if  'mapping_report' in input_jobs:
            run_mapping_report_job(folder)


        if  'deduplicate' in input_jobs:
            run_deduplicator_jobs(folder)

        if  'map' in input_jobs:
            run_mappers_jobs(folder)

        if  'fix' in input_jobs:
            run_fixers_jobs(folder)

        if  'dv_map' in input_jobs:
            run_dv_mapper_jobs(folder)

        if  'upload' in input_jobs:
            run_upload_jobs(folder)

        if  'dv_upload' in input_jobs:
            run_upload_dv_jobs(folder)


        

    

print("""

                                                    ▀▀█▀▀ ░█ ░█ ░█▀▀▀ 　 ░█▀▀▀ ░█▄ ░█ ░█▀▀▄ 　 █ 
                                                     ░█   ░█▀▀█ ░█▀▀▀ 　 ░█▀▀▀ ░█░█░█ ░█ ░█ 　 ▀ 
                                                     ░█   ░█ ░█ ░█▄▄▄ 　 ░█▄▄▄ ░█  ▀█ ░█▄▄▀ 　 ▄
            
    """)
             