from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'ThanhBinh',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 23),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(hours=1)
}

dag = DAG(
    'sgx_crawler',
    default_args=default_args,
    description='SGX Crawler',
    schedule_interval='0 18 * * 1-5', # Run at 10am every weekday - Singapore time, or
)

t1 = SSHOperator(
    task_id='run_script',
    ssh_conn_id='sshwsl',
    command='cd /home/tb24/projects/dytechlab && source venv/bin/activate && python -m crawler.auto_job',
    dag=dag,
)