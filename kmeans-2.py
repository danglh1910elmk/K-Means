import numpy as np
import matplotlib.pyplot as plt 

clusters = []
labels = []
points = np.array([[1,1],[1,1.3],[1.3,1],[4,4.8],[4.2,4.8],[4.1,4.5],[8,4.8],[8,5.2],[8.1,5],[8,5.4]])

x, y = zip(*points)
plt.plot(x, y, 'ro')

k = 3

# create random clusters
for i in range(k):
    clusters.append([np.random.randint(0,10), np.random.randint(0,10)])

running = True
while running:
    labels = []
    clusters_copy = clusters.copy()

    # determine label of each point
    for p in points:
        # distance from points to clusters
        distances_to_cluster = []
        for c in clusters:
            distances_to_cluster.append(np.linalg.norm(np.array(p)-np.array(c), 2))
        min_distance = min(distances_to_cluster)
        labels.append(distances_to_cluster.index(min_distance))

    stop = 0
    # update clusters location
    for i in range(len(clusters)):
        sum_x, sum_y, count = 0, 0, 0
        for j in range(len(points)):
            if labels[j] == i:
                count += 1
                sum_x += points[j][0]
                sum_y += points[j][1]
        if count != 0:
            clusters[i][0] = sum_x/count
            clusters[i][1] = sum_y/count

        # distance from old clusters to new clusters
        error = np.linalg.norm(np.array(clusters[i])-np.array(clusters_copy[i]), 2)
        if error < 1e-5:
            stop += 1
    if stop == k:
        running = False

print(np.array(clusters))
x, y = zip(*clusters)
plt.plot(x,y,'b*')
plt.show()