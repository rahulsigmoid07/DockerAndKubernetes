from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.providers.http.sensors.http import HttpSensor

with DAG('database_postgres',start_date=datetime(2022,1,1),schedule_interval='@daily',catchup=False) as dag:
   
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='SQL/create_table.sql'
    )
    insert_into_table =PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='postgres',
         sql='SQL/insert_into_table.sql'
    )
    
    create_table >> insert_into_table