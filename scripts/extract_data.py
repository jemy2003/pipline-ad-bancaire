import pandas as pd
import numpy as np
import random
import os

def extract_data():
    np.random.seed(42)
    n = 1000

    data = {
        'transaction_id': range(1, n + 1),
        'client_id': [f"C{random.randint(100,999)}" for _ in range(n)],
        'amount': np.random.uniform(5, 5000, n),
        'transaction_type': np.random.choice(['Online', 'ATM', 'POS', 'Mobile'], n),
        'device': np.random.choice(['Card', 'App', 'Web'], n),
        'location': np.random.choice(['Paris', 'Casablanca', 'Madrid', 'Rome'], n),
        'hour': np.random.randint(0, 24, n),
        'weekday': np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], n),
        'status': np.random.choice(['Valid', 'Fraud', 'Rejected'], n, p=[0.8, 0.1, 0.1])
    }

    df = pd.DataFrame(data)

    os.makedirs('data', exist_ok=True)
    df.to_csv('data/transactions.csv', index=False)
    print("✅ Extraction terminée : data/transactions.csv créé")
