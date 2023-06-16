# Docker-Kubernetes-assignment

## Docker Assignment
1. Wrote a python script to create a DAG that has tasks to add execution time to a postgres table. <br\>
* ##### Made docker compose file for airflow containers and postgres database 
2. The DAG ran successfully.

<img width="853" alt="Screenshot 2023-06-15 at 5 17 30 PM" src="https://github.com/rahulsigmoid07/DockerAndKubernetes/assets/123542137/27104b49-e2fa-4828-84a6-e572b0dc15f5">

3. Verified the result by viewing the table.
<img width="327" alt="Screenshot 2023-06-15 at 5 02 30 PM" src="https://github.com/rahulsigmoid07/DockerAndKubernetes/assets/123542137/a4aa5967-f7ce-4f36-8556-670d544fda25">


3. To get the above results, follow the below steps:
* Download the folder ```DockerAndKubernetes``` Change directory to get inside this folder.
* Run ``` docker compose up -d ``` to build the required containers.

## Kubernetes Assignment
1. Made a custom docker image for postgres with airflow installed in it. The container made from this image will be used as a database for airflow and also to store dag execution data in a table. The following dockerfile was used for creating the image.python
``` python
# USING LATEST POSTGRES IMAGE
FROM postgres:latest 

# SWITCH TO ROOT USER
USER root

# STEPS TO BUILD PYTHON VERSION 3.7
RUN apt-get -y update
RUN apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget 
RUN wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
RUN tar -xf Python-3.7.12.tgz
WORKDIR /Python-3.7.12
RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall

# STEPS TO INSTALL AIRFLOW VERSION 2.5.0
RUN apt-get install libpq-dev
RUN pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"2. This image and the custom airflow image were pushed in dockerhub for public access.
```

2. Installed minikube to make a kubernetes cluster using the following commands.
``` bash
brew install minikube
 minikube start 
```

3. Using the ```postgres-deployment.yaml```file the pod containing postgres container was made. The following command was used,
```bash
kubectl apply -f postgres-deployment.yaml
```
4. The postgres container has airflow installed in it. But it was not initialised as the database for airflow. I tried to do it automatically by writing commands in yaml file, but some error always popped up. So, I entered the postgres docker container using,
``` bash
kubectl exec -it your-pod-name -- /bin/bash #Then ran the following command to initialise the database and make a user.bash
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@localhost:5432/airflow

airflow db init

airflow users create -u airflow -p airflow -f rahul -l kumar -e xyz@gmail.com -r Admin
```
5. Then created a service of type clusterIP by running ```postgres-service.yaml``` to give access to postgres pods inside the cluster. The following command was used.
``` bash
kubectl apply -f postgres-service.yaml
```
6.  Entered the airflow scheduler container as root user using the following commands,
``` bash
minikube ssh #To login inside minikube cluster
docker exec -it -u root your-airflow-scheduler-container-id /bin/bash #To get inside scheduler container
cd /opt/airflow/dags #Changed directory to dags folder

#Installed vim
apt-get update
apt-get install vim
vim postgress_db.py #Made this file and copied my code inside it
```
7. Created a service of type load balancer by running ``` airflow-service.yaml ```to access airflow webserver from my local system using the following command,
 ``` bash
kubectl apply -f airflow-service.yaml
```
8. Accessed the airflow webserver by running the command ```minikube service airflow ```. Upon logging in, the dag was visible and it ran successfully.
<img width="853" alt="Screenshot 2023-06-15 at 5 17 30 PM" src="https://github.com/rahulsigmoid07/DockerAndKubernetes/assets/123542137/27104b49-e2fa-4828-84a6-e572b0dc15f5">

9. Verified this by logging into the postgres container and viewing the table.
<img width="466" alt="Screenshot 2023-06-15 at 5 28 14 PM" src="https://github.com/rahulsigmoid07/DockerAndKubernetes/assets/123542137/6ad8876d-9040-4dcb-a819-debf8f9f2eeb">


