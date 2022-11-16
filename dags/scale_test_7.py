from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def _sleep_pyop(secs):
    from time import sleep
    print(f"sleeping for {secs} seconds.")
    sleep(secs)

with DAG(
        dag_id=f"scale_test_5",
        schedule_interval=timedelta(seconds=1),
        start_date=datetime(2022, 10, 20),
        catchup=False,
        max_active_runs=9999, 
        max_active_tasks=9999
    ) as dag:
        sleep = PythonOperator(
            task_id="sleep_1",
            python_callable=_sleep_pyop,
            op_kwargs= {
                "secs": 3600
                }
            )
