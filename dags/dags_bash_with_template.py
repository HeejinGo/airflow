import datetime
import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator #오퍼레이터 : 설계도
import os



with DAG (
    dag_id="dags_bash_with_template",
    schedule="0 1 * * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "bash", "template"],
) as dag:
    bash_t1 = BashOperator( 
        task_id="bash_t1",
        bash_command="echo "data_interval_start : {{ data_interval_start }}"',
    )
    bash_t2 = BashOperator( 
        task_id="bash_t2",
        env={
            'start_date':'{{data_interval_start | ds}}',
            'end_date':'{{data_interval_end | ds}}'
        }
        bash_command="echo $start_date && echo $end_date',
    )

    bash_t1 >> bash_t2