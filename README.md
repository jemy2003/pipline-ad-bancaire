🏦 Bank Transaction Data Analysis Pipeline
Description
Ce projet est une application Python orchestrée par Apache Airflow qui :
Génère des transactions bancaires simulées au format CSV.
Effectue le nettoyage, la transformation et la standardisation des données.
Réduit la dimension via PCA pour la visualisation.
Discrétise les montants pour créer des niveaux de risque.
Entraîne un modèle RandomForest pour la classification des transactions suspectes.
Technologies
Python 3.x
Apache Airflow
Pandas, NumPy
Scikit-learn
Matplotlib (optionnel)
Prérequis
Python ≥ 3.8
Apache Airflow installé et configuré (pip install apache-airflow)
Environnement virtuel activé (optionnel mais recommandé)
Installation et exécution
Cloner le dépôt :
git clone https://github.com/ton-username/fraud-detection-pipeline.git
cd fraud-detection-pipeline

Installer les dépendances :
pip install -r requirements.txt

Lancer Airflow :
airflow db init
airflow webserver -p 8080
airflow scheduler
Depuis l’interface web Airflow : activer le DAG fraud_detection_pipeline puis exécuter le pipeline.
