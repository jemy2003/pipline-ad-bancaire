import pandas as pd
from sklearn.decomposition import PCA

def reduce_data():
    df = pd.read_csv('data/transformed_transactions.csv')

    features = df.select_dtypes(include=['float64', 'int64'])
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(features)

    df['PC1'], df['PC2'] = reduced[:, 0], reduced[:, 1]
    df.to_csv('data/reduced_transactions.csv', index=False)
    print("✅ Réduction de dimension (PCA) terminée : data/reduced_transactions.csv")
