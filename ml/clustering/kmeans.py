import numpy as np

# generate a random list of points in a 2-D space
points = tuple([(a, b) for a, b
                in zip(np.random.randn(5), np.random.randn(5))])
print(points)

def kmeans(points, centroids, n=100):
    # randomly assist the centroids
    clusters = {}
    for point in points:
        distances = euclidean_distance(point, centroids)
        clusters[point] = assign_point(distances)
    # recompute centroids
    new_centroids = compute_centroids(clusters)
    # check if stopping criteria is met
    if should_stop(centroids, new_centroids):
        return new_centroids
    else:
        n -= 1
        kmeans(points, new_centroids, n)

centroids = tuple([(a, b) for a, b
                   in zip(np.random.randn(5), np.random.randn(5))])
kmeans(points, centroids)

