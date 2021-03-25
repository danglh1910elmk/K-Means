import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
import numpy as np

img = plt.imread('building.jpg')
# print(img.shape)

width = img.shape[0]
height = img.shape[1]

img = img.reshape(width*height, 3)

kmeans = KMeans(n_clusters = 3).fit(img)

clusters = kmeans.cluster_centers_
labels = kmeans.predict(img)

img1 = np.zeros((width, height, 3), dtype=np.uint8)

# cach 1: mine
for i in range(width): # cao, dai`
    for j in range(height): # ngang, RỘNG
        img1[i][j] = clusters[labels[i*height + j]]

# cach 2: anh Dũng
index = 0
for i in range(width):
    for j in range(height):
        label_of_pixel = labels[index]
        img1[i][j] = clusters[label_of_pixel]
        index += 1

plt.imshow(img1)
plt.show()