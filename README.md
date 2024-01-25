

Author: Ali Nouina <br>
Contact: abdelali@ufl.edu<br>
Secondary contributor: Jason Glover <br>
Contact: jasonglover@ufl.edu<br>
Last Updated: 12/6/2023 <br>

#Requirements

This script requires the use of a PySpark cluster. Before running the script, make sure you have set up a PySpark cluster environment.

## Setting Up a PySpark Cluster

The Onefl_cluster info/repository can be found in this link: 
                        https://bitbucket.org/bmi-ufl/onefl_cluster/src/master/

# Running the formatters, the mappers, and the uploaders scripts

## Before running your scripts:

1. Rename your /data_example subfolder to /data

        cp -r partners/[site_name]/data_example  partners/[site_name]/data


2. Rename secrets_example.py to secrets.py

        cp common/secrets_example.py  common/secrets.py


3. In secrets.py, assign OneFlorida encryption key value to SEED

        SEED = "Change me"

        
4. Change to permission all the folders and the files in the repository to 777 by simply go to the upper folder and run the following command:

        chmod -R 777 .


## To run the individual formatter/ or multiple formatters:

        cluster run -d /path/to/data/parent/folder/ -a --  onefl_converter.py      -p [partner_name]     -f [folder_name1 folder_name_2 ... ]     -t [table_name_1 table_name_1 ... ]     -j format

                e.g.   cluster run -d /data/processing/ -a --  onefl_converter.py      -p partnerA     -f q2_2023     -t demographic     -j format

## To run the individual mapper/ or multiple mappers:

        cluster run  -a --  onefl_converter.py      -p [partner_name]     -f [folder_name1 folder_name_2 ... ]     -t [table_name_1 table_name_1 ... ]     -j map

                e.g.   cluster run -a --  onefl_converter.py      -p partnerA     -f q2_2023     -t demographic     -j map


## To run the individual uploader/ or multiple uploaders:

        cluster run -a --  onefl_converter.py      -p [partner_name]     -f [folder_name1 folder_name_2 ... ]     -t [table_name_1 table_name_1 ... ]     -j upload -s [server_name] -db [db_name]

                e.g.   cluster run -a --  onefl_converter.py      -p partnerA     -f q2_2023     -t demographic     -j upload -s data_server@foo.edu -db partnerA_db



## to run the all the jobs on all the tables at once:
        cluster run -d /path/to/data/parent/folder/ -a --  onefl_converter.py      -p [partner_name]     -f [folder_name1 folder_name_2 ... ]     -t all     -j all -s [server_name] -db [db_name]

                e.g.   cluster run -d /data/processing/ -a --  onefl_converter.py      -p partnerA     -f q2_2023     -t all     -j all -s data_server@foo.edu -db partnerA_db

## The parameters definitions:

                    -j:  the running job and the options are: all, formatter,  mapper, or upload
                    -p:  the partner or site. Used to pull the partner/site custom dictionaries. e.g. usf, uab, etc
                    -t:  the table name to run the job on and the options are all, demographic, encounter, etc 
                    -f:  the folder of where the input raw data resides
                    -d:  the path to the data parent folder
                    -a:  some custom configurations
                    -s:  mssql server address
                    -db: database name
                    
