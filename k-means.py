import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('iris.csv')
print(data.head())

x = data.iloc[:, :4]
print(x.head())

km = KMeans(n_clusters=3)
km.fit(x)

y = km.predict(x)
print(y)

centroid = km.cluster_centers_
print(centroid)
