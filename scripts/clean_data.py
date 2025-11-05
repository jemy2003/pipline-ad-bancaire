import pandas as pd
import numpy as np

def clean_data():
    df = pd.read_csv('data/transactions.csv')

    # Supprimer doublons
    df = df.drop_duplicates()

    # Corriger heures invalides
    df = df[df['hour'] <= 24]

    # Remplacer valeurs manquantes
    df['amount'] = df['amount'].fillna(df['amount'].median())
    df['hour'] = df['hour'].fillna(df['hour'].median())
    df['location'] = df['location'].fillna('Unknown')

    df.to_csv('data/cleaned_transactions.csv', index=False)
    print("✅ Données nettoyées : data/cleaned_transactions.csv")
