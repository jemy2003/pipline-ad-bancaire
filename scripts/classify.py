import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def classify():
    df = pd.read_csv('data/final_transactions.csv')

    # Nettoyer les colonnes non pertinentes
    drop_cols = ['transaction_id', 'client_id', 'location']
    for col in drop_cols:
        if col in df.columns:
            df = df.drop(columns=[col])

    # Encodage des statuts
    df = pd.get_dummies(df, columns=['status'])
    if 'status_Fraud' not in df.columns:
        print("⚠️ Pas de transactions Fraud dans le dataset")
        return

    X = df.drop(columns=['status_Fraud', 'status_Valid', 'status_Rejected'], errors='ignore')
    y = df['status_Fraud']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Modèle entraîné avec précision : {acc:.2f}")
