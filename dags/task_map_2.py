from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
import time
from airflow.models import Variable

catchup = False
try:
    x = Variable.get("CATCHUP")
    if x == 'True' or x == 'true':
        catchup = True
except Exception as e:
    pass

with DAG('task_map_2', 
          start_date=datetime(2022,10,20,6,10,0), 
          schedule=timedelta(seconds=60),
          catchup=catchup,
          max_active_runs=2005, 
          max_active_tasks=2005) as dag:

    @task
    def get_expand_map():
        TASK_MAP_SIZE = int(Variable.get("TASK_MAP_SIZE"))
        return list(range(TASK_MAP_SIZE))

    @task
    def sleep(x: int):
        print(f'I am dynamic task number {x}')
        SLEEP_TIME = int(Variable.get("SLEEP_TIME"))
        print(f'sleep {SLEEP_TIME}')
        time.sleep(SLEEP_TIME)
        return x

    sleep.expand(x=get_expand_map())
