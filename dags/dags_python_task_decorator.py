
from __future__ import annotations

import logging
import sys
import time
from pprint import pprint

import pendulum

from airflow.sdk import DAG, task

from airflow.providers.standard.operators.python import (
    PythonOperator,
)

log = logging.getLogger(__name__)

PATH_TO_PYTHON_BINARY = sys.executable


with DAG (
    dag_id="dags_python_task_decorator",
    schedule="0 1 * * *",
    start_date=pendulum.datetime(2025,1,1,tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "python"],
) as dag:
    
    @task(task_id="python_task_1")
    def print_context(input_text):
        print(input_text)
    
    python_task_1 = print_context("exec python decorator!")
    
    # def example_python_decorator():
    #     # [START howto_operator_python]
    #     @task(task_id="print_the_context")
    #     def print_context(ds=None, **kwargs):
    #         """Print the Airflow context and ds variable from the context."""
    #         pprint(kwargs)
    #         print(ds)
    #         return "Whatever you return gets printed in the logs"

    #     run_this = print_context()
    # # [END howto_operator_python]

    # # [START howto_operator_python_render_sql]
    # @task(task_id="log_sql_query", templates_dict={"query": "sql/sample.sql"}, templates_exts=[".sql"])
    # def log_sql(**kwargs):
    #     log.info("Python task decorator query: %s", str(kwargs["templates_dict"]["query"]))

    # log_the_sql = log_sql()
    # # [END howto_operator_python_render_sql]