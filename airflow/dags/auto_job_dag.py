from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow import DAG
from crawler import auto_job

args = {
    'owner': 'Thanh Binh',
    'start_date': days_ago(1) # make start date in the past
}

dag = DAG(
    dag_id='crawler-dag',
    default_args=args,
    schedule_interval='@daily' #to make this workflow happen every day
)