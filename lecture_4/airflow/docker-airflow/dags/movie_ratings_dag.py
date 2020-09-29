
import logging
import airflow
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Create the DAG object
args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG('movie_ratings',
          default_args=args,
          schedule_interval=None,
          max_active_runs=1)

# Define our tasks
def download_ratings():
    response = requests.get('http://192.168.1.23:5000/movie_ratings')
    data = response.json()
    return data    
    
def print_ratings(**context):
    data = context['task_instance'].xcom_pull(task_ids='download_ratings')
    logging.info(data)
    counts_by_rating = {}
    for row in data:
        if row['rating'] not in counts_by_rating:
            counts_by_rating[row['rating']] = 0
        counts_by_rating[row['rating']] += 1

    
    for rating, count in counts_by_rating.items():
        logging.info("%s\t%d" % (rating, count))
    

## Define the task dependencies (e.g tasks 1 and 2 execute before 3)    
t1 = PythonOperator(
    task_id='download_ratings',
    python_callable=download_ratings,
    dag=dag
)
t2 = PythonOperator(
    task_id='print_ratings',
    python_callable=print_ratings,
    dag=dag,
    provide_context=True
)

t1 >> t2
