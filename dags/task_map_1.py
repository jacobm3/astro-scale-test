from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import time
from airflow.models import Variable

with DAG('task_map_1', start_date=datetime(2022, 1, 1), schedule='*/30 * * * *', catchup=False,
          max_active_runs=2000, max_active_tasks=2000) as dag:

    @task
    def get_expand_map():
        TASK_MAP_SIZE = int(Variable.get("TASK_MAP_SIZE"))
        return list(range(TASK_MAP_SIZE))

    @task
    def sleep(x: int):
        print(f'I am dynamic task number {x}')
        SLEEP_TIME = int(Variable.get("SLEEP_TIME"))

        time.sleep(SLEEP_TIME)
        return x

    sleep.expand(x=get_expand_map())
