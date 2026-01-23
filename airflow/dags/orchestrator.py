from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append(r'/home/charis/Desktop/Projects/Airflow Project/repos')  

from repos.insert_records import main

def safe_main_callable():
    return main()

default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2026, 1, 23),
    'catchup': False
}

dag = DAG(
    dag_id='stocks_api_orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id='example',
        python_callable=safe_main_callable
    )
