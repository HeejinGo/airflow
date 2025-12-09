import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator #오퍼레이터 : 설계도
import os
from pprint import pprint

from airflow.sdk import DAG, task

from airflow.providers.standard.operators.python import (
    PythonOperator,
)

with DAG (
    dag_id="dags_bash_show_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "bash", "template"],
) as dag:
    # @task(task_id='python_task')
    # def show_templates(**kwargs):
    #     pprint(kwargs)
    
    # show_templates()
    def show_templates(**kwargs):
        pprint(kwargs)
        
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=show_templates
    )
    
    task_1