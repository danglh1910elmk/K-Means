import numpy as np
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

clusters = []
points = np.array([[1,1],[1,1.3],[1.3,1],[4,4.8],[4.2,4.8],[4.1,4.5],[8,4.8],[8,5.2],[8.1,5],[8,5.4]])

# draw points
x, y = zip(*points)
plt.plot(x, y, 'ro')

# use library
kmeans = KMeans(n_clusters=3).fit(points)
clusters = kmeans.cluster_centers_
print(clusters)

# draw clusters 
x, y = zip(*clusters)
plt.plot(x, y, 'b*')
plt.show()