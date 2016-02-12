"""
Random graph generator module.
"""

import random
from matplotlib import pyplot as plt

from module1.project1.project1 import compute_in_degrees, in_degree_distribution

def er_graph(num_nodes, probability):
    """
    Generate a random directed graph with n number of nodes and edges based on
    probability p
    """
    graph = {0: set([])}
    if num_nodes > 0:
        for node in range(num_nodes):
            edges = []
            for head in range(num_nodes):
                if node != head:
                    a = random.random()
                    if a < probability:
                        edges.append(head)
            graph[node] = set(edges)
    return graph


graph = er_graph(2777, 0.05)
print graph
degrees = compute_in_degrees(graph)
print degrees
dist = in_degree_distribution(graph)
print dist

total = sum(dist.itervalues())
normalized = {key: float(value)/total for key, value in dist.items()}
#print(timeit.default_timer() - start_time)
print sum(normalized.itervalues())
#print dist
print normalized


x = normalized.keys()
y = normalized.values()

print len(y)
plt.loglog(x, y, 'bo')
plt.minorticks_off()

plt.xlabel('In-degree distribution')
plt.ylabel('Normalized In-degree distribution')
plt.title('Random directed graph')
plt.legend(['n = 2777 | p = 0.05'], loc=2)

plt.grid(True)
plt.savefig('citations-q2.png')
plt.show()
