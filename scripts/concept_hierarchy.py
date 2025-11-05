import pandas as pd
import pandas.api.types as ptypes

def concept_hierarchy():
    df = pd.read_csv('data/reduced_transactions.csv')

    if 'amount' not in df.columns:
        print("⚠️ Colonne 'amount' absente après PCA, discrétisation ignorée")
        return

    df['amount_category'] = pd.qcut(df['amount'], 5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
    df.to_csv('data/final_transactions.csv', index=False)
    print("✅ Discrétisation terminée : data/final_transactions.csv")
