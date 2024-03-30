import numpy as np
from scipy.sparse.csgraph import dijkstra

graph = np.array([[0, 1, 2, 0], [0, 0, 0, 3], [0, 0, 0, 1], [0, 0, 0, 0]])
dist_matrix, predecessors = dijkstra(graph, return_predecessors=True)
start_node = 0
end_node = 3
path = []
while end_node != start_node:
    path.append(end_node)
    end_node = predecessors[start_node, end_node]
path.append(start_node)
path = path[::-1]
print(f"El camino más corto entre el nodo {start_node} y el nodo {end_node} es: {path}")