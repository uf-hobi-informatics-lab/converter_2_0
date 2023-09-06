#Get the user's sudo password for chown command - Not necessary if not on the IQ Server
#echo "Please enter your sudo password: "
#sudo -v

START_CLUSTER=$(date +%s)

#Get command line arguments for the python script being passed in
num_args=$#
args="${@:2:$num_args}"

# There are (3) commands as listed in the README.md. They are 'docker compose up', 'docker run' and 'docker compose down'.

#Boot the cluster with 5 worker nodes
docker compose up -d --scale worker=5

START_SUBMIT=$(date +%s)

#Submit the passed in script to the cluster
docker run \
--network=Ali_pyNet \
-v $(pwd):/app \
-v /inbox:/inbox \
--rm cluster-image \
/opt/bitnami/spark/bin/spark-submit \
--conf "spark.pyspark.python=python3" \
--conf "spark.driver.memory=16g" \
--conf "spark.executor.memory=8g" \
--master spark://master:7077 \
--deploy-mode client \
--py-files /app/common/*  \
--jars mssql-jdbc-driver.jar \
--name my_pyspark_job /app/$1 $args

END_SUBMIT=$(date +%s)
#Shut down the cluster
docker compose down

END_CLUSTER=$(date +%s)
#Update permissions of the output directory from demo.py script
#sudo chown -R $(id -u):$(id -g) $(pwd)/output_demographic

RUNTIME_CLUSTER=$((END_CLUSTER-START_CLUSTER))
RUNTIME_SUBMIT=$((END_SUBMIT-START_SUBMIT))

#The two command below merge the output files together into a single file while only keeping a single header row
#head -n 1 output_demographic/part-00000-*.csv > merged_demo.csv    
#find . -name 'output_demographic/part-0000*.csv' -exec tail -n +2 {} \; >> merged_demo.csv 

#output the runtime for development purposes
echo "Script runtime (with Cluster): $RUNTIME_CLUSTER seconds"
echo "Script runtime (without Cluster): $RUNTIME_SUBMIT seconds"
