import datetime
import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator #오퍼레이터 : 설계도


with DAG(
    dag_id="dags_bash_operator", #파이썬 파일명과 상관없이 화면에서 보이는 값, 하지만 dag 파일명과 dag_id는 일치시키면 직관적이다
    schedule="0 0 * * *", #주기(분 시 일 월 요일)
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"), #dag 언제부터 돌건지
    catchup=False, #현재 3/1, start_date = 1/1이라면 해당 dag를 올렸을 때 1/1~3/1 사이의 누락된 날짜 구간까지 돌릴건지 말건지 결정하는 변수 (근데 차례대로 안돌아 가고 두달치가 한번에 돌아감)
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"], #화면에서 보이는 태그 값
    # params={"example_key": "example_value"}, #task에 공통적으로 넘겨줄 파라미터
) as dag:
    
    bash_t1 = BashOperator( #오퍼레이터를 통해서 만드는 건 태스크 (bash_t1 = 태스크 객체명)
        task_id="bash_t1",
        bash_command="echo whoami", #어떤 쉘 스크립트를 수행할거냐
    )
    bash_t2 = BashOperator( #오퍼레이터를 통해서 만드는 건 태스크 (bash_t1 = 태스크 객체명)
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2