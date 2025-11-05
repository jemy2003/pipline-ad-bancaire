import pandas as pd
from sklearn.preprocessing import StandardScaler

def transform_data():
    df = pd.read_csv('data/cleaned_transactions.csv')

    # Variables additionnelles
    df['is_night'] = df['hour'].apply(lambda x: 1 if 0 <= x <= 6 else 0)
    q3 = df['amount'].quantile(0.75)
    df['high_amount_flag'] = df['amount'].apply(lambda x: 1 if x > q3 else 0)

    # One-Hot encoding
    df = pd.get_dummies(df, columns=['transaction_type', 'device', 'weekday'])

    # Standardisation
    scaler = StandardScaler()
    df[['amount', 'hour']] = scaler.fit_transform(df[['amount', 'hour']])

    df.to_csv('data/transformed_transactions.csv', index=False)
    print("✅ Transformation terminée : data/transformed_transactions.csv")
