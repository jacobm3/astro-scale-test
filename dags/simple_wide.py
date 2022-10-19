from datetime import datetime

from airflow import DAG

from airflow.operators.bash import BashOperator


with DAG(
    "simple_wide",
    schedule_interval=None,
    start_date=datetime(2021, 8, 1),
    catchup=False,
    max_active_tasks=2000,
    concurrency=2000,
):

    for i in range(500):
        t = BashOperator(task_id=f"out_{i}", bash_command="sleep 180")
