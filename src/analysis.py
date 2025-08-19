from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def run_pca(df, n_components=2):
    df_numeric = df.select_dtypes(include="number").dropna()
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df_numeric)
    
    plt.figure(figsize=(8,6))
    plt.scatter(components[:,0], components[:,1], alpha=0.6)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA Visualization")
    plt.show()
    
    return pca.explained_variance_ratio_
