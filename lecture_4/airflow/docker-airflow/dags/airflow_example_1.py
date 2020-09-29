
#import time
#import logging
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
#from pprint import pprint


# Create the DAG object
args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG('example', default_args=args, schedule_interval=timedelta(seconds=5))

# Define our tasks
def task_1():
    #time.sleep(1)
    #print('foo bar')
    import logging
    
    logging.info("Hello from task 1")
    
def task_2():
    import logging
    logging.info("Hello from task 2")
    
def task_3():
    import logging
    logging.info("Hello from task 3")


## Define the task dependencies (e.g tasks 1 and 2 execute before 3)    
t1 = PythonOperator(task_id='task_1', python_callable=task_1, dag=dag)
t2 = PythonOperator(task_id='task_2', python_callable=task_2, dag=dag)
#t3 = PythonOperator(task_id='task_3', python_callable=task_3, dag=dag)

#t3.set_upstream([t1, t2])
t1 >> t2
