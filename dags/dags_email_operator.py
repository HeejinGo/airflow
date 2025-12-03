from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator 
from airflow.providers.smtp.operators.smtp import EmailOperator
# 버전마다 위 선언이 다른 것 같다 airflow example  과 동일하게 선언하지 않아서 airflow  에 안 떴음 !

import pendulum


with DAG (
    dag_id="dags_email_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "email"],
) as dag:
    
    send_email = EmailOperator(
        task_id="send_email",
        conn_id="smtp_gmail",
        to="heejin8273@gmail.com",
        subject="airflow email send success!",
        html_content="success! good!"
    )
    send_email