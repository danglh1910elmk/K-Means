import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
import numpy as np

img = plt.imread("D:\Projects\AI\K-Means - Data Visualization\main\photosettle\\4.jpg")

width = img.shape[0]
height = img.shape[1]

img = img.reshape(width*height, 3)

kmeans = KMeans(n_clusters = 6).fit(img)
clusters = kmeans.cluster_centers_
labels = kmeans.predict(img)

# 1st way
# img1 = np.zeros_like(img)
# for i in range(len(clusters)):
#     for j in range(len(img)):
#         if labels[j] == i:
#             img1[j] = clusters[i]

# 2nd way
img2 = np.zeros_like(img)
for i in range(len(img)):
    img2[i] = clusters[labels[i]]

img2 = img2.reshape(width,height,3)

plt.imshow(img2)
plt.show()