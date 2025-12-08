import pendulum

from airflow.providers.standard.operators.python import (
    PythonOperator,
)
from airflow.sdk import DAG

from utils.get_fruit import select_fruit
from utils.common.common_func import get_sftp

import os


import random

rand_int = random.randint(0,3)

with DAG (
    dag_id="dags_python_operator",
    schedule="0 1 * * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "python"],
) as dag:
    
    python_task_1 = PythonOperator(
        task_id='python_task_1',
        python_callable=select_fruit
    )

    python_task_2 = PythonOperator(
        task_id='python_task_2',
        python_callable=get_sftp
    )

    python_task_1 >> python_task_2