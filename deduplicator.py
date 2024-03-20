"""
Goal: De-Duplicate partner csv files

If docker gets locked up do:
    docker rm name

@authors:
    Jim Seipp <jseipp@ufl.edu>

Goal: de-duplicate the formatted input files generating deduplicated files

    Folder layout:
        INPUT:  partners/partner/data/formatter_output/folder/file(s).csv
        OUTPUT: partners/partner/data/deduplicator_output/folder/generated_duplicates/
                            generated_deduplicates/file(s).csv                                      # file with no duplicates
                            generated_duplicates/File_Summary_for_file(s).csv                       # summary of duplicates (key and count)
                            generated_duplicates/file(s).csv                                        # list of duplicate rows removed from original

    EG: partners/uab/data/formatter_output/20230929/DIAGNOSIS.csv
        partners/uab/data/deduplicator_output/20230929/generated_deduplicates/DIAGNOSIS.csv
        partners/uab/data/deduplicator_output/20230929/generated_duplicates/File_Summary_for_DIAGNOSIS.csv


Inputs:
    -f formatter_output_folder --output_folder deduplicator_output_folder -t table(s)

    EG:

    -f partners/uab/data/formatter_output/20230929 --output_folder partners/uab/data/deduplicator_output/20230929 -t all
    -f partners/uab/data/formatter_output/20230929 --output_folder partners/uab/data/deduplicator_output/20230929 -t demographic death

==================

"""


#external imports
from commonFunctions import CommonFuncitons
import os
import sys
from sys import platform as _platform
import logging
from itertools import (takewhile, repeat)
from time import sleep
import pandas as pd
import datetime
from time import time
import collections
import glob
import shutil
import csv
import subprocess
import argparse

# spark libs
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext


class process_duplicates():
    # dictionary names
    PD_STATUS           = 'Status'
    PD_DEDUPS           = 'Unique Rows'
    PD_DUPS             = 'Duplicate Rows'
    PD_TABLE            = 'Table'
    PD_ERROR            = "Error"
    PD_TIME             = "Processing Time"

    # from old constants.py
    SFTP_PROVIDERS_WITH_SUB_FOLDERS = {"1F-CHIT": ["meridian", "rboi"]}  # providers that have sub folders
    SFTP_DATAVANT_HASH_HEADERS = ["patid", "token1", "token2", "token3", "token4", "token5", "token16"]  # "token_encryption_key"] DATAVANT HEADER
    DATAVANT_PATID_MAP = ["personid"]  # maps to patid

    # aias dictionary for files that have different names and headers than standard
    ALIAS_INFO_TABLES = {}
    ALIAS_INFO_TABLES['DRUG_EXPOSURE'] = ['DRUG_EXPOSURE_ID']

    def __init__(self, input_data_folder, output_data_folder, input_tables, spark):
        self.spark = spark
        self.using_static_table_key_info = True             # using static tables instead of dynamically creating them
        self.ignored_file_types = ['.pdf', '.bin', '.ds_store']
        self.subfolder_name = ''
        self.input_tables = []
        # set display names
        self.display_table_name = input_tables[0]
        split_path_names = input_data_folder.split(os.sep)
        self.display_folder_name = split_path_names[len(split_path_names) - 1]
        for j, folder_name in enumerate(split_path_names, start=0):
            if folder_name == 'partners':
                self.display_partner_name = split_path_names[j+1]
                break
        self.display_python_name = f'{self.display_table_name}_deduplicator.py'
        self.cf =CommonFuncitons(self.display_partner_name)
        if 'all' in input_tables:
            self.input_tables.append('all')
        else:
            for table in input_tables:
                self.input_tables.append(f'formatted_{table}.csv')
        if _platform == 'darwin':
            working_folder = os.getcwd()
            self.input_data_folder = f'{working_folder}{os.sep}{input_data_folder}'
            self.output_data_folder = f'{working_folder}{os.sep}{output_data_folder}'
        else:
            app_prefix = f'{os.sep}app{os.sep}'
            if input_data_folder.startswith(app_prefix):
                self.input_data_folder = input_data_folder
                self.output_data_folder = output_data_folder
            else:
                self.input_data_folder = f'{app_prefix}{input_data_folder}'
                self.output_data_folder = f'{app_prefix}{output_data_folder}'
        self.results_info = collections.OrderedDict()
        self.generated_deduplicates = "generated_deduplicates"
        self.generated_duplicates = "generated_duplicates"
        self.temp_generated_file = "temp_generated"
        self.generate_duplicate_detail_file = True          # generate detail duplicate file
        self.max_duplicate_detail_rows = 100            # limit to detail number or rows we display, NOTE it gets a java memory exception on Linux if i add many more

    def init(self):
        if self.using_static_table_key_info:
            self.ids_info = collections.OrderedDict([('LDS_ADDRESS_HISTORY', ['ADDRESSID']),
                                                   ('CONDITION_ORG', ['CONDITIONID']),
                                                   ('DEATH_ORG', ['PATID', 'DEATH_SOURCE']),
                                                   ('DEATH_CAUSE_ORG', ['PATID', 'DEATH_CAUSE', 'DEATH_CAUSE_CODE', 'DEATH_CAUSE_TYPE', 'DEATH_CAUSE_SOURCE']),
                                                   ('DEMOGRAPHIC_ORG', ['PATID']),
                                                   ('DIAGNOSIS_ORG', ['DIAGNOSISID']),
                                                   ('DISPENSING_ORG', ['DISPENSINGID']), ('ENCOUNTER_ORG', ['ENCOUNTERID']),
                                                   ('ENROLLMENT_ORG', ['PATID', 'ENR_START_DATE', 'ENR_BASIS']),
                                                   ('HASH_TOKEN_ORG', ['PATID']),
                                                   ('IMMUNIZATION_ORG', ['IMMUNIZATIONID']),
                                                   ('LAB_RESULT_CM_ORG', ['LAB_RESULT_CM_ID']),
                                                   ('LDS_ADDRESS_HISTORY_ORG', ['ADDRESSID']),
                                                   ('MED_ADMIN_ORG', ['MEDADMINID']),
                                                   ('OBS_CLIN_ORG', ['OBSCLINID']),
                                                   ('OBS_GEN', ['OBSGENID']),
                                                   ('PCORNET_TRIAL', ['PATID', 'TRIALID', 'PARTICIPANTID']),
                                                   ('PRESCRIBING_ORG', ['PRESCRIBINGID']),
                                                   ('PRO_CM_ORG', ['PRO_CM_ID']),
                                                   ('LDS_ADDRESS_HX', ['ADDRESSID']),
                                                   ('PROCEDURES_ORG', ['PROCEDURESID']),
                                                   ('PROVIDER_ORG', ['PROVIDERID']),
                                                   ('VITAL_ORG', ['VITALID']),
                                                   ('LAB_HISTORY', ['LABHISTORYID']),
                                                   ('DIAGNOSIS', ['DIAGNOSISID']),
                                                   ('DEMOGRAPHIC', ['PATID']),
                                                   ('ENROLLMENT', ['PATID', 'ENR_START_DATE', 'ENR_BASIS']),
                                                   ('PROCEDURES', ['PROCEDURESID']),
                                                   ('VITAL', ['VITALID']),
                                                   ('DISPENSING', ['DISPENSINGID']),
                                                   ('ENCOUNTER', ['ENCOUNTERID']),
                                                   ('LAB_RESULT_CM', ['LAB_RESULT_CM_ID']),
                                                   ('CONDITION', ['CONDITIONID']),
                                                   ('PRO_CM', ['PRO_CM_ID']),
                                                   ('PRESCRIBING', ['PRESCRIBINGID']),
                                                   ('DEATH', ['PATID', 'DEATH_SOURCE']),
                                                   ('DEATH_CAUSE', ['PATID', 'DEATH_CAUSE', 'DEATH_CAUSE_CODE', 'DEATH_CAUSE_TYPE', 'DEATH_CAUSE_SOURCE']),
                                                   ('MED_ADMIN', ['MEDADMINID']),
                                                   ('PROVIDER', ['PROVIDERID']),
                                                   ('OBS_CLIN', ['OBSCLINID']),
                                                   ('IMMUNIZATION', ['IMMUNIZATIONID']),
                                                   ('DRUG_EXPOSURE', ['DRUG_EXPOSURE_ID'])])
        else:
            self.init_database()
            self.create_unique_id_info()

    # check if file is a unrecognized file
    def is_recognized_data_file(self, file_path):
        for file_type in self.ignored_file_types:
            if file_type in file_path.lower():
                logging.info("is_recognized_data_file({}),  We ignore this file".format(file_type, file_path))
                return False                        # we ignorew this type file
        if os.path.isdir(file_path) or self.find_delimeter(file_path) == '\n':
            return False
        return True

    # check if file is a datavant hash file
    # ‘hash’ or ‘token’ or ‘datavant’ in name and header looks like template header
    def is_datavant_hash_file(self, full_file_name):
        try:
            # if "datavant" in file_name.lower() or "hash" in file_name.lower() or "token" in file_name.lower():
            f1 = open(full_file_name, "r")
            header = f1.readline().lower().replace("_", "")
            for replacement_patid_name in process_duplicates.DATAVANT_PATID_MAP:
                header = header.replace(replacement_patid_name, "patid")
            for col in process_duplicates.SFTP_DATAVANT_HASH_HEADERS:
                if col not in header:
                    return False
            logging.info("is_datavant_hash_file found {}".format(full_file_name))
            return True
        except Exception as e:
            logging.error("ERROR: is_datavant_hash_file={} Error={}".format(full_file_name, str(e)))
        return False

    # display job error message and exit
    def display_error_message_and_exit(self, display_msg, log_msg):
        logging.error(log_msg)
        self.cf.print_failure_message(
            folder=self.display_folder_name,
            partner=self.display_partner_name,
            job=self.display_python_name)
        self.cf.print_with_style(display_msg, 'danger red')
        exit()

    # find the csv file delimiter
    def find_delimeter(self, file_path):
        def head(filename: str, n: int):
            try:
                with open(filename) as f:
                    head_lines = [next(f).rstrip() for x in range(n)]
            except StopIteration:
                with open(filename) as f:
                    head_lines = f.read().splitlines()
            return head_lines
        def find_delimiter(filename):
            sniffer = csv.Sniffer()
            with open(filename) as fp:
                delimiter = sniffer.sniff(fp.read(5000)).delimiter
            return delimiter
        def detect_delimiter(filename: str, n=2):
            try:
                return find_delimiter(filename)     # new way to get delimeter using sniffer
                """ old way
                sample_lines = head(filename, n)
                common_delimiters = [',', ';', '\t', ' ', '|', ':']
                for d in common_delimiters:
                    ref = sample_lines[0].count(d)
                    if ref > 0:
                        if all([ref == sample_lines[i].count(d) for i in range(1, n)]):
                            return d
                """
            except Exception as e:
                log_msg = "ERROR find_delimeter/detect_delimiter FileName={}, Error={}".format(filename, str(e))
                display_msg = str(e)
                self.display_error_message_and_exit(display_msg, log_msg)
            return '\n'
        return detect_delimiter(file_path)

    # run the process
    def run(self):
        try:
            self.init()
            self.email_enabled = False
            process_duplicates = time()
            logging.info("STARTING deduplicator.py for Folder {}".format(self.input_data_folder))
            path_list = self.output_data_folder.split(os.sep)
            temp_output_path = f'{os.sep}'
            check_folder_created = False
            for path_item in path_list:
                temp_output_path = os.path.join(temp_output_path, path_item)
                if path_item == 'deduplicator_output':
                    check_folder_created = True
                if check_folder_created and not os.path.isdir(temp_output_path):
                    logging.info("run creating folder folder {}".format(temp_output_path))
                    os.mkdir(temp_output_path)
            self.if_name = self.input_data_folder.split(os.path.sep)[self.input_data_folder.count(os.path.sep)]
            if os.path.exists(self.input_data_folder):
                self.results_info[self.if_name] = collections.OrderedDict()
                self.process_folder(self.input_data_folder, self.output_data_folder)
                if os.path.isdir(self.temp_generated_file_path):
                    shutil.rmtree(self.temp_generated_file_path)
                    logging.info("Deleted temp folder {}".format(self.temp_generated_file_path))
                logging.info("FINISHED process_duplicates->run() for Folder {}, took {}".format(self.input_data_folder, format(datetime.timedelta(seconds=int(time() - process_duplicates)))))
            else:
                logging.error("Error process_duplicates->run could not find folder {}".format(self.input_data_folder))
        except Exception as e:
            log_msg = "ERROR process_duplicates->run, Error={}".format(str(e))
            display_msg = str(e)
            self.display_error_message_and_exit(display_msg, log_msg)
        if self.email_enabled:
            command = ["/app/email_app"]
            # Execute the command
            print("emailing {}".format(command))
            subprocess.run(" ".join(command), shell=True)

    # check if CSV file
    def is_csv_file(self, file):
        filename, file_extension = os.path.splitext(file)
        if file_extension.upper() == ".CSV":
            return True
        return False

    # get_group_keys_str Keys str for sql queries
    def get_group_keys_str(self, keys):
        keys_str = ''
        for index, key in enumerate(keys):
            if index > 0:
                keys_str += ", "
            keys_str += key
        return keys_str

    # rename temp spark file
    def rename_temp_spark_file(self, name, folder):
        success = False
        try:
            temp_folder_path = "{}{}".format(self.temp_generated_file_path, os.sep)
            folder_path = "{}{}".format(folder, os.sep)
            name_path = "{}{}".format(folder_path, name)
            logging.info("rename_temp_spark_file {}".format(name_path))
            file_list = os.listdir(temp_folder_path)
            for file_num, file in enumerate(file_list, start=0):
                temp_path = "{}{}".format(temp_folder_path, file)
                if self.is_csv_file(file):
                    os.rename(temp_path, name_path)
                elif "SUCCESS" in file.upper():
                    os.remove(temp_path)
                    success = True
        except Exception as e:
            log_msg = "ERROR rename_temp_spark_file rename {} {} Error={}".format(name, folder, str(e))
            display_msg = str(e)
            self.display_error_message_and_exit(display_msg, log_msg)
        return success

    # process path data
    def process_folder(self, input_folder_path, output_folder_path):
        try:
            process_folder_time = time()  # used to time the process
            logging.info(f'STARTING process_folder Input: {input_folder_path}    Output: {output_folder_path}')
            self.create_dedup_folders(output_folder_path)
            file_list = os.listdir(input_folder_path)  # Get list of files
            file_created = False
            for file_num, file in enumerate(file_list, start=0):
                if 'all' in self.input_tables or file in self.input_tables:
                    file_path = f'{input_folder_path}{os.sep}{file}'
                    if not self.is_csv_file(file):
                        logging.info(f'process_folder Ignoring NON CSV File: {file_path}')
                        continue
                    if not file_created:
                        file_created = True
                        self.create_dedup_folders(output_folder_path)
                    self.results_info[self.if_name][file] = collections.OrderedDict()
                    if not self.is_recognized_data_file(file_path):
                        self.results_info[self.if_name][file][process_duplicates.PD_STATUS] = "Ignoring Unrecognized file"
                        logging.info(f'process_folder Unrecognized File: {file_path}')
                    elif self.is_datavant_hash_file(file_path):
                        self.results_info[self.if_name][file][process_duplicates.PD_STATUS] = "Ignoring Datavant file"
                        logging.info(f'process_folder Datavant IGNORING File: {file_path}')
                    else:
                        process_file_time = time()  # used to time the process
                        logging.info(f'STARTING process_folder PROCESSING File: {file_path}')
                        self.results_info[self.if_name][file][process_duplicates.PD_STATUS] = self.dedup_file(input_folder_path, output_folder_path, file)
                        self.results_info[self.if_name][file][process_duplicates.PD_TIME] = int(time() - process_file_time)
                        logging.info("FINISHED process_folder PROCESSING File: {}, took {}".format(file_path, format(datetime.timedelta(seconds=int(time() - process_file_time)))))
            logging.info("FINISHED process_folder {}, took {}".format(input_folder_path, format(datetime.timedelta(seconds=int(time() - process_folder_time)))))
        except Exception as e:
            log_msg = "ERROR process_folder {}, Error={}".format(input_folder_path, str(e))
            display_msg = str(e)
            self.display_error_message_and_exit(display_msg, log_msg)

    # huge file processing using spark interface
    def dedup_using_spark(self, file_path, output_file_path, file):
        start_time = time()
        try:
            file_summary = "File_Summary_for_" + file
            logging.info("STARTING dedup_using_spark({})".format(file))
            delimiter = self.find_delimeter(file_path)
            table = self.get_table_name(file_path, file)
            if table == "":
                return 'Ignoring file without Unique Keys'             # there are no keys found for this table
            self.results_info[self.if_name][file][process_duplicates.PD_TABLE] = table
            temp_view = "tempdb"
            keys = self.ids_info[table]
            group_keys_str = self.get_group_keys_str(keys)
            test_time = time()
            # get the csv file into a spark dataframe
            logging.info("START dedup_using_spark read CSV FILE {}".format(file_path))
            df_all = self.spark.read.csv(file_path, sep=delimiter, header=True)
            all_rows_cnt = df_all.count()
            logging.info("FINISH dedup_using_spark read CSV FILE ({:,} rows), file_path={}, delimiter={}, took {}".format(all_rows_cnt, file_path, delimiter, format(datetime.timedelta(seconds=int(time() - test_time)))))
            test_time = time()
            # create a view that can be accesses with SQL commands
            logging.info("START dedup_using_spark createOrReplaceTempView")
            df_all.createOrReplaceTempView(temp_view)
            logging.info("FINISH dedup_using_spark createOrReplaceTempView({}), took {}".format(temp_view, format(datetime.timedelta(seconds=int(time() - test_time)))))
            test_time = time()
            # get dataframe with duplicates dropped
            logging.info("START dedup_using_spark dropDuplicates Keys {}".format(keys))
            df_unique = df_all.dropDuplicates(keys)
            unique_rows_cnt = df_unique.count()
            logging.info("FINISH dedup_using_spark dropDuplicates({}), ({:,} rows), took {}".format(keys, unique_rows_cnt, format(datetime.timedelta(seconds=int(time() - test_time)))))
            test_time = time()
            # get list of duplicates with number of times each key is duplicated
            logging.info("START dedup_using_spark Get Duplicate Keys Counts")
            dups_df = self.spark.sql("SELECT {}, COUNT(*) as cnt FROM {} GROUP BY {} HAVING COUNT(*) > 1".format(group_keys_str, temp_view, group_keys_str))
            dups_keys_cnt = dups_df.count()
            duplicate_rows = all_rows_cnt - unique_rows_cnt
            logging.info("FINISH dedup_using_spark Get Duplicate Keys Counts {:,} Duplicate Keys, {:,} Duplicate rows removed, took {}".format(dups_keys_cnt, duplicate_rows, format(datetime.timedelta(seconds=int(time() - test_time)))))
            test_time = time()
            # save the csv file that has the duplicates removed
            logging.info("START dedup_using_spark Save CSV File {}".format(self.temp_generated_file_path))
            df_unique.coalesce(1).write.mode("overwrite").option("header", True).option("delimiter", delimiter).csv(self.temp_generated_file_path)
            self.rename_temp_spark_file(file, self.generated_deduplicates_path)
            logging.info("FINISH dedup_using_spark Save CSV File {}, took {}".format(self.generated_deduplicates_path, format(datetime.timedelta(seconds=int(time() - test_time)))))
            test_time = time()
            # save the csv file that has with number of times each key is duplicated (only if there are duplicates)
            if dups_keys_cnt > 0:       # only make file if there are duplicates
                logging.info("START dedup_using_spark Save CSV File {}".format(self.temp_generated_file_path))
                dups_df.coalesce(1).write.mode("overwrite").option("header", True).option("delimiter", delimiter).csv(self.temp_generated_file_path)
                self.rename_temp_spark_file(file_summary, self.generated_duplicates_path)
                logging.info("FINISH dedup_using_spark Save CSV File {}, took {}".format(self.generated_duplicates_path, format(datetime.timedelta(seconds=int(time() - test_time)))))
                if self.generate_duplicate_detail_file:
                    test_time = time()
                    logging.info("START dedup_using_spark Save DETAIL CSV File {}".format(self.temp_generated_file_path))
                    row_index = 0
                    rows_written = 0
                    max_detail_msg = ''
                    test_dup_time = time()
                    for row in dups_df.rdd.toLocalIterator():
                        where_str = ''
                        for key_index, key_name in enumerate(keys):
                            if row[key_name] is None:
                                continue                # ignore none
                            if where_str != '':
                                where_str += " AND "
                            where_str += " {}='{}'".format(key_name, row[key_name])
                        query = "SELECT * FROM {} WHERE {}".format(temp_view, where_str)
                        if row_index == 0:
                            detail_dups_df = self.spark.sql(query)
                            dup_cnt = detail_dups_df.count()
                            #detail_dups_df.coalesce(1).write.mode("overwrite").option("header", True).option("delimiter", delimiter).csv(self.temp_generated_file_path)
                        else:
                            temp_df = self.spark.sql(query)
                            dup_cnt = temp_df.count()
                            #temp_df.coalesce(1).write.mode("append").option("header", True).option("delimiter", delimiter).csv(self.temp_generated_file_path)
                            detail_dups_df = detail_dups_df.union(temp_df)
                        rows_written += dup_cnt
                        row_index += 1
                        if (row_index % 100) == 0:
                            logging.info("dedup_using_spark processed {} Duplicates to Detail CSV File, Total rows {}, took {}".format(row_index, rows_written, format(datetime.timedelta(seconds=int(time() - test_dup_time)))))
                            test_dup_time = time()
                        if rows_written > self.max_duplicate_detail_rows:
                            max_detail_msg = f"Only showing {rows_written} rows to DETAIL CSV File because (MAX IS {self.max_duplicate_detail_rows})"
                            logging.info(f"{max_detail_msg}")
                            break
                    detail_dups_df.coalesce(1).write.mode("overwrite").option("header", True).option("delimiter", delimiter).csv(self.temp_generated_file_path)
                    self.rename_temp_spark_file(file, self.generated_duplicates_path)
                    if max_detail_msg != '':
                        detail_name = f'{self.generated_duplicates_path}{os.sep}{file}'
                        fh = open(detail_name, 'a')
                        fh.write(f'{max_detail_msg}')          # append max message to end ofCSV file
                        fh.close()
                    logging.info("FINISH dedup_using_spark Dup DETAIL Save CSV File {} with {} rows, took {}".format(self.generated_duplicates_path, rows_written, format(datetime.timedelta(seconds=int(time() - test_time)))))
            #test_time = time()
            # save the detailed csv file with duplicates information
            #df_empty = df_all.limit(0)
            logging.info("FINISHED dedup_using_spark({}), took {}".format(file, datetime.timedelta(seconds=int(time() - start_time))))
            #jim = 1/ 0     # test to force exception
        except Exception as e:
            display_msg = str(e)
            log_msg = "ERROR dedup_using_spark Error={}".format(str(e))
            self.display_error_message_and_exit(display_msg, log_msg)
        return

    # de duplicate the txt/csv file
    def dedup_file(self, input_file_path, output_file_path, file):
        file_path = f'{input_file_path}{os.sep}{file}'
        dest_file_path = f'{output_file_path}{os.sep}{file}'
        return self.dedup_using_spark(file_path, dest_file_path, file)

    # get the table name from the list of tables with key values (by matching the name with part of the filename string)
    def get_table_name(self, file_path, file_name):
        file_name_upper = file_name.upper()

        ret_table = ""
        for table in self.ids_info:
            if table in file_name_upper:
                if len(table) > len(ret_table):
                    ret_table = table
                    print(ret_table)
  

        if ret_table == "":
            log_msg = "ERROR get_table_name for ({}) does not exist in self.ids_info = collections.OrderedDict".format(file_name)
            display_msg = "get_table_name for ({}) does not exist".format(file_name)
            self.display_error_message_and_exit(display_msg, log_msg)
            return self.check_header_id_for_key(file_path, file_name_upper)        # see if the file name has a matching header id
        return ret_table

    # make changes to header to compensate for providers sending ill formatted headers
    def normalize_header(self, raw_header):
        header = raw_header
        try:
            header = [elem.replace('"', '') for elem in header]                             # remove quotes "
            header = [elem.replace("'", '') for elem in header]                             # remove quotes '
            header = [elem.replace("#", '') for elem in header]                             # remove #
            header = [elem.encode('ascii', errors='ignore').decode() for elem in header]    # remove non ascii data
            header = list(map(str.upper, header))                   # make header all upper case
            logging.info("normalize_header from({}) to ({})".format(str(raw_header)[1:-1], str(header)[1:-1]))
        except Exception as e:
            logging.error("ERROR normalize_header Error={}".format(str(e)))
        return header

    # FAST way to count lines in a HUGE file
    def rawincount(self, filename):
        count = 0
        try:
            f = open(filename, 'rb')
            bufgen = takewhile(lambda x: x, (f.raw.read(1024 * 1024) for _ in repeat(None)))
            count = sum(buf.count(b'\n') for buf in bufgen)
        except Exception as e:
            logging.error("rawincount {} Error={}".format(filename, str(e)))
        return count

    # return strinf to display rows per second
    def display_line_time(self, line_display_time, rows):
        secs = int(time() - line_display_time) + 1
        return "took {}, writing {:,} rows per second".format(format(datetime.timedelta(seconds=secs)), int(rows / secs))

    # create de duplicate folders (note we never remove the existing folders, must be done manually)
    def create_dedup_folders(self, folder_path):
        try:
            def actual_create(file):
                # first delete the old temp folders if it exists
                if os.path.isfile(file):
                    logging.info("ERROR create_dedup_folders Error {} already exists and is a file (should be a folder)".format(file))
                    return False
                if os.path.isdir(file):
                    logging.info("create_dedup_folders FOLDER: {} already exists, so no need to create it".format(file))
                    return True
                # now create the folder and sub folders
                logging.info("create_dedup_folders creating FOLDER: {}".format(file))
                os.mkdir(file)

            self.temp_generated_file_path = os.path.join(folder_path, self.temp_generated_file)
            self.generated_duplicates_path = os.path.join(folder_path, self.generated_duplicates)
            self.generated_deduplicates_path = os.path.join(folder_path, self.generated_deduplicates)
            actual_create(folder_path)
            actual_create(self.generated_duplicates_path)
            actual_create(self.generated_deduplicates_path)
            return True
        except Exception as e:
            log_msg = "ERROR create_dedup_folders Error={}".format(str(e))
            display_msg = str(e)
            self.display_error_message_and_exit(display_msg, log_msg)

# main function for executing the duplicates
def main(input_data_folder, output_data_folder, table):
    try:
        main_start_time = time()
        log_name = ""
        if _platform == "linux":
            log_name += 'process_duplicates.log'
        if os.path.exists(log_name):
            os.remove(log_name)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=log_name,
                            filemode='a')
        if input_data_folder == '' or input_data_folder == None or output_data_folder == '' or output_data_folder == None or table == '' or table == None:
            message = "PARAM ERROR '{}', should be '-f input_folder -of output_folder -t table', Exiting program".format(sys.argv)
            logging.error(message)
            exit()
        using_spark = True         # test only
        if using_spark:
            #conf = SparkConf()
            #if 'SPARK_HOME' not in os.environ:
            #    os.environ['SPARK_HOME'] = spark_home
            spark = SparkSession \
                .builder \
                .appName("Process Duplicates") \
                .getOrCreate()
            spark_version = spark.version
        else:
            spark= 0
        pd = process_duplicates(input_data_folder, output_data_folder, table, spark)
        pd.run()
        if using_spark:
            spark.stop()
        logging.info("FINISHED deduplicator.py for Folder {}, took {}".format(input_data_folder, format(datetime.timedelta(seconds=int(time() - main_start_time)))))

    except Exception as e:
        log_msg = "Process Duplicates ERROR Error={}".format(str(e))
        display_msg = str(e)
        self.display_error_message_and_exit(display_msg, log_msg)
        exit()

# program to check duplicates
#command = ["python", "/app/partners/"+partner+"/formatting_scripts/"+formatter, '-f', folder ]
#command = "python process_duplicates.py 20230929"
#subprocess.run(command, shell=True)
#print("done")
#exit()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--data_folder")
parser.add_argument("-of", "--output_folder")
parser.add_argument("-t", "--table", nargs="+")
args = parser.parse_args()
input_data_folder = args.data_folder
output_data_folder = args.output_folder
table = args.table
main(input_data_folder, output_data_folder, table)


