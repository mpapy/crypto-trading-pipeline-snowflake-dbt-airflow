from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from include.loaders.load_binance_to_snowflake import main

default_args = {
    "owner": "marek",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="load_binance_data",
    default_args=default_args,
    description='Loads recent Binance crypto data to Snowflake Bronze layer',
    start_date=datetime(2024, 1, 1),
    schedule_interval="* * * * *", # every minute
    catchup=False,
    tags=["crypto", "data_loading"]
) as dag:

    load_binance_data = PythonOperator(
        task_id="load_binance_data",
        python_callable=main
    )

    load_binance_data