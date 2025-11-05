from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract_data import extract_data
from scripts.clean_data import clean_data
from scripts.transform_data import transform_data
from scripts.reduce_data import reduce_data
from scripts.concept_hierarchy import concept_hierarchy
from scripts.classify import classify

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='fraud_detection_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Pipeline complet de détection de fraude bancaire'
) as dag:

    t1 = PythonOperator(task_id='extract_data', python_callable=extract_data)
    t2 = PythonOperator(task_id='clean_data', python_callable=clean_data)
    t3 = PythonOperator(task_id='transform_data', python_callable=transform_data)
    t4 = PythonOperator(task_id='reduce_data', python_callable=reduce_data)
    t5 = PythonOperator(task_id='concept_hierarchy', python_callable=concept_hierarchy)
    t6 = PythonOperator(task_id='classify', python_callable=classify)

    t1 >> t2 >> t3 >> t4 >> t5 >> t6
