import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt

df = pd.read_csv('books.csv')
features = ['average_rating', 'num_pages', 'ratings_count', 'text_reviews_count']
data = df[features]
data = data.dropna()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# KMeans Clustering
n_clusters_kmeans = 3
print("\nKMeans Clustering")
kmeans = KMeans(n_clusters=n_clusters_kmeans, random_state=42)
kmeans_clusters = kmeans.fit_predict(scaled_data)
silhouette_kmeans = silhouette_score(scaled_data, kmeans_clusters)
davies_bouldin_kmeans = davies_bouldin_score(scaled_data, kmeans_clusters)
print(f"Silhouette Score: {silhouette_kmeans}")
print(f"Davies-Bouldin Score: {davies_bouldin_kmeans}")

df['kmeans_cluster'] = kmeans_clusters
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

plt.figure(figsize=(12, 8))
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans_clusters, cmap='viridis', s=50)
plt.title('KMeans Clustering (PCA Reduced)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar(label='Cluster Label')
plt.show()

print("\nCluster Summaries for KMeans")
print(df.groupby('kmeans_cluster')[features].mean())

print("\nCluster Sizes for KMeans")
print(df['kmeans_cluster'].value_counts())
