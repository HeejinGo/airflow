from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator #오퍼레이터 : 설계도
# 버전마다 위 선언이 다른 것 같다 airflow example  과 동일하게 선언하지 않아서 airflow  에 안 떴음 !

import pendulum


with DAG (
    dag_id="dags_test",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "bash"],
) as dag:
    
    run_1 = BashOperator(
        task_id="run_1",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh Orange"
    )
    run_2 = BashOperator(
        task_id="run_2",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh strawberry"
    )

    run_1 >> run_2