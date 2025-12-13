import datetime
import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator #오퍼레이터 : 설계도

from dateutil import relativedelta

with DAG (
    dag_id="dags_bash_macro",
    schedule="0 9 L * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "python"],
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        env={
            'start_date':'{{ data_interval_start.in_timezone("Asia/Seoul") | ds}}',
            'end_date':'{{ data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1) | ds}}'
        }
        bash_command='echo $start_date && $end_date'
    )
    
    bash_t1