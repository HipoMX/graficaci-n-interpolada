import numpy as np
from scipy.spatial import ConvexHull

points = np.array([[0, 0], [1, 1], [1, 0], [0, 1], [0.5, 0.5]])
hull = ConvexHull(points)
print(f"Los vértices del conjunto convexo son: {hull.vertices}")