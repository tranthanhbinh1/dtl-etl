from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(hours=1)
}

dag = DAG(
    'your_dag_id',
    default_args=default_args,
    description='Your DAG description',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='run_script',
    bash_command='python /path/to/your/script.py',
    dag=dag,
)