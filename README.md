# Working with the Cluster
Developmental implementation of the PySpark Cluster for the OneFL Converter. This cluster should be used for testing scripts. Please do not push changes to the cluster files (`Dockerfile`, `requirements.txt`, `run_cluster.sh`, `docker-compose.yml`).

Author: Jason Glover <br>
Contact: jasonglover@ufl.edu <br>
Last Updated: 8/3/2023 <br>

## Running the Cluster
1. Clone the repo onto your machine.
2. In the parent directory of the repo, update the directory permissions to allow for scripts to write output by running the following command:

        sudo chmod 777 docker_container
3. Ensure that you are on the `dev` branch.

        git status
        
4. In the repo directory, paste the following command into your command line to build the image:

        docker build -t cluster-image .
> **Note**: If planning to run this cluster on the IQ Server, then you may skip step 4 as the image is already installed there.
5. (For running on the IQ Server) User must rename the repo directory and modify two files to avoid conflicts with other devs. Update the repo directory name by going up a level from the repo's root and running `mv docker_container/ [NEW_NAME]/`. Next, use a text editor to open the `docker-compose.yml` file. In the last line of the file, update `pyNet` to a unique name, such as your gatorlink ID. Save the changes, then open `run_cluster.sh`. In the `docker run` command, modify the `--network` flag to reflect the updated network name that you set in `docker-compose.yml`.
6. Once the image has been built, you can paste the following command into your command line to run the cluster, convert the sample file, and then shut down the cluster:

        sh run_cluster.sh verify_cluster.py
7. Alternatively, you can run the individual commands from the `run_cluster.sh` script in the terminal yourself to boot the cluster. There are comments in the file explaining what each command does. First, call the `docker compose up` command to boot the cluster. Once finished booting, call the `docker run` command. When passing the `docker run` command through the command line, replace the `$1` at the end of the command with the name of the script you want to test (e.g. `verify_cluster.py`). If your file takes command line arguments, replace `$args` with the neccesary arguments. If your file doesn't take command line arguments, remove `$args`. Finally, shut down the cluster by calling the `docker compose down`.

> **Note**: When passing the commands yourself, ensure that you shut down the cluster before trying to boot another instance of the cluster. In its current state, the cluster can only be instantiated once at a time on a machine.

> **Note**: As of 5/16/2023, the `run_cluster.sh` script has been updated to accept command line arguments for the python script being passed in. Simply add the arguments to the end of the `sh run_cluster.sh` command. Ex: `sh run_cluster.sh foo.py arg1 arg2 arg3`

8. The test script, `verify_cluster.py` has run correctly if the ouput contains the message `"Cluster is running as expected."`

## Expected Output

The `demo.py` script has run correctly if a directory called `output_demographic` has been created and contains a variable number of .csv files which are named like `part-00000-95819a38-1814-4600-b64c-defddd66352f-c000.csv`. The reason a variable number is created is that it is dependent upon the cluster and partition size. Each file name will be incremental.

For example:
- The first file will have `part-0000-*.csv`
- The second will be `part-0001-*.csv`

## Configuring the Cluster

### Number of Nodes

The number of worker nodes to create is set when booting the cluster with the `docker-compose up -d --scale worker=5` command. Replace the `5` with your desired number of worker nodes.

> **Note**: The number of worker nodes you can have on the cluster is bound by your machine's resources. If you have an 8-core CPU on your machine and each worker is given 1 core, then your cluster will crash when trying to build more than 7 worker nodes (since the master node also takes a core).

### Worker Hardware Allocation

You can configure the amount of RAM and number of CPU cores each worker node has in the `docker-compose.yml` file. In the `worker` section, the flags `SPARK_WORKER_MEMORY` and `SPARK_WORKER_CORES` allocate the RAM and number of CPU cores, respectively, for a single node.

In order to take advantage of the full amount of RAM each node has been allocated, the `docker run` command in the `run_cluster.sh` file must be modified. Modify the following flag in the `docker run` command to have the same value as given to the `SPARK_WORKER_MEMORY` parameter in the `docker-compose.yml`:

        --conf "spark.executor.memory=1g"

## Developing for the Cluster

For any operations involving the Spark environment, the script must include a call to the `SparkSession.builder`, to create the Spark session. Here is where the master node location will be set. In order to submit the script to the cluster, you must pass `spark://master:7077` to the master parameter. Examples of this can be found in `demo.py` and `ad_merger_test.py`.

## Extra Notes

1. To monitor the status of your cluster, simply paste the following URL into your browser and refresh the page as necessary:

        http://localhost:8080/ 
> **Note**: This does not work for the IQ Server.


2. If running the `demo.py` file multiple times, run the following command in between runs:

        rm -r output_demographic/

    Otherwise, the script will throw an error saying the directory already exists.

3. If attempting to run `ad_merge_test.py`, then the user will need to pull the necessary dependencies of the ad-merger (the directories in the ad_merger repo) into their directory. 

4. In its current state, this cluster can only view the files within the repo directory. Attempting to read files that are not in the repo or a subdirectory will throw a File not Found error.

5. When developing programs to run against the cluster, keep the following in mind. Since the python script being submitted to the cluster is run in a Docker container, hardcoded directories on your host machine will throw an error. The `/app` directory in the container is mounted to the repo on the host machine, this is where output or input should be written to. For example: I want to write the output `result` from the cluster. My repo is located at `/Users/jason/code/cluster` on my host machine. Thus, `/app` is mounted to `/Users/jason/code/cluster`. In my python script, I would write the output to `/app/result`, not `/Users/jason/code/cluster/result`.



# Running the formatter and the mapper scripts


## Before running your scripts:

1. Rename your /data_example subfolder to /data

        cp -r partners/[site_name]/data_example  partners/[site_name]/data


2. Rename secrets_example.py to secrets.py

        cp common/secrets_example.py  common/secrets.py


3. In secrets.py, assign OneFlorida encryption key value to SEED

        SEED = "Change me"


4. Copy your input files to your partner data folder

        cp [partner file] partners/[site_name]/data/input/
        
5. Change to permission all the folders and the files in the repository to 777 by simply go to the upper folder and run the following command:

        chmod -R 777 .


## To run the individual formatter:

        sh run_cluster.sh partners/[site_name]/formatting_scripts/[table_name]_formatter.py


## To run the individual mapper:

        sh run_cluster.sh mapping_scripts/[table_name]_mapper.py -p [partner_name]


## to run the onefl-convert:
        sh run_cluster.sh onefl_converter.py -j [job_type] -p [table_name] -t [table_name]

                -j: all, formatter, or mapper
                -p: pcornet_partner_1, omop_partner_1, etc
                -t: all, demographic, encounter etc 
