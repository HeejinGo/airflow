import pendulum

from airflow.sdk import DAG, task

from airflow.providers.standard.operators.python import (
    PythonOperator,
)

with DAG (
    dag_id="dags_python_template",
    schedule="0 1 * * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "python"],
) as dag:
    
    def python_func1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
        
    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_func1,
        op_kwargs={
            'start_date':'{{data_interval_start}}',
            'end_date':'{{data_interval_end | ds}}'
        }
    )
    
    @task(task_id='python_func2')
    def python_func2(**kwargs):
        print(kwargs)
        print('ti' + str(kwargs['ti']))
        print('ds' + str(kwargs['ds']))
        print('data_interval_start' + str(kwargs['data_interval_start']))
        print('data_interval_end' + str(kwargs['data_interval_end']))
        
    python_t1 
    python_func2()
    
    