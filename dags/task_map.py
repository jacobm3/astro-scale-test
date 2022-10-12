from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import time

with DAG('task_map', start_date=datetime(2022, 1, 1), schedule='*/15 * * * *', catchup=False,
          max_active_runs=1000, max_active_tasks=1000, concurrency=1000) as dag:
    @task
    def sleep(x: int):
        print(f'I am dynamic task number {x}')
        time.sleep(10)
        return x

    result = sleep.expand(x=list(range(500)))
