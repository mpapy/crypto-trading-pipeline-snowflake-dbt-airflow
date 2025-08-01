from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="dbt_trading_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # žádné opakování (ručně spouštěný DAG)
    catchup=False,
    tags=["crypto", "dbt"]
) as dag:

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="dbt run --project-dir ./dbt/crypto_trading"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="dbt test --project-dir ./dbt/crypto_trading"
    )

    dbt_run >> dbt_test
