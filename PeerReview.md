## praneeth review
#### docker 
1. Initially, DAG is created with a schedule of timedelta days equal to 1.
2. Three tasks are created which creates, inserts and run a query in postgres.
3. The first task was named createtable_task which creates a table in postgres.
4. The second task was named insert_rows_task which insert the rows in above created table.
5. The third task was named query_task which runs a query on table. This task validates the entry in postgres.
6. He used  docker compose file to run dags in airflow.

#### kubernetes
1. created a custom docker image for postgres with airflow installed in it.
2. Pushed the postgres image and the custom airflow image in dockerhub for public access.
3. Installed minikube to make a kubernetes cluster.
4. Created the postgres-deployment.yaml file which contains the pod containing postgres container.
5. Created a service of type clusterIP by running postgres-service.yaml to give access to postgres pods inside the cluster.
6. Created persistant volumes dags-storage.yaml to mount dags folder inside airflow container to the local directory.
7. Created a service of type load balancer by running airflow-service.yaml to access airflow webserver from the local system.
8. Accessed the airflow webserver by running the command minikube service airflow.

## chakradhar review
#### docker 
1. Initially, a DAG is created with a schedule interval of 1 day using timedelta.
2. The DAG consists of three tasks that interact with a PostgreSQL database.
3. The first task, called "createtable_task," is responsible for creating a table within the PostgreSQL database.
4. The second task, named "insert_rows_task," is responsible for inserting rows into the previously created table.
6. The third task, known as "query_task," executes a query on the table to validate the entry made in the PostgreSQL database.
7. To orchestrate the execution of these tasks, a docker compose file is used to run the DAGs within the Airflow environment.


#### kubernetes
1. A customized Docker image was created by incorporating both PostgreSQL and Airflow within it.
2. The custom PostgreSQL image, along with the customized Airflow image, was pushed to DockerHub, enabling public access and availability.
3. Minikube was installed to set up a Kubernetes cluster, facilitating container orchestration and management.
4. The configuration file postgres-deployment.yaml was created, specifying the deployment of a pod that includes a PostgreSQL container.
5. To enable internal access to the PostgreSQL pods within the cluster, a clusterIP service was established by executing postgres-service.yaml.
6. Persistent volumes were implemented through the dags-storage.yaml file, allowing the mounting of the dags folder from the Airflow container to a local directory.
7. For external access to the Airflow webserver, a load balancer service was created using airflow-service.yaml.
8. By utilizing the command minikube service airflow, the Airflow webserver was accessed, enabling interaction and management from the local system.
