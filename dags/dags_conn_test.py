import datetime
import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator #오퍼레이터 : 설계도

from airflow.operators import EmptyOperator

with DAG(
    dag_id="dags_conn_test", #파이썬 파일명과 상관없이 화면에서 보이는 값, 하지만 dag 파일명과 dag_id는 일치시키면 직관적이다
    schedule=None, #주기(분 시 일 월 요일)
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"), #dag 언제부터 돌건지
    catchup=False, #현재 3/1, start_date = 1/1이라면 해당 dag를 올렸을 때 1/1~3/1 사이의 누락된 날짜 구간까지 돌릴건지 말건지 결정하는 변수 (근데 차례대로 안돌아 가고 두달치가 한번에 돌아감)
 ) as dag:
    t1 = EmptyOperator(
        task_id="t1"
    )
    t2 = EmptyOperator(
        task_id="t2"
    )
    t3 = EmptyOperator(
        task_id="t3"
    )
    t4 = EmptyOperator(
        task_id="t4"
    )
    t5 = EmptyOperator(
        task_id="t5"
    )
    t6 = EmptyOperator(
        task_id="t6"
    )
    t7 = EmptyOperator(
        task_id="t7"
    )
    t8 = EmptyOperator(
        task_id="t8"
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8
    
    