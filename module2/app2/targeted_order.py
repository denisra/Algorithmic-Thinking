"""
Computes the runtime of different implementations of the targeted_order
function.
"""

import timeit
from matplotlib import pyplot as plt

from helper import targeted_order, delete_node, copy_graph
from app2 import upa
#from module2.project2.test_graphs import *


def fast_targeted_order(ugraph):
    """
    fast implementation of the targeted_order function

    :param ugraph: dict
    :return: list
    """

    graph = copy_graph(ugraph)
#    print graph
    size = len(ugraph) #- 1
    degree_sets = [set() for _ in range(size)]
    order = []

    for node, edges in ugraph.iteritems():
        degree = len(edges)
        degree_sets[degree].add(node)
#    print degree_sets

    for k in range(size - 1, -1, -1):
        while degree_sets[k]:
            node = degree_sets[k].pop()
            neighbors = graph[node]
            for neighbor in neighbors:
                degree = len(graph[neighbor])
                degree_sets[degree].remove(neighbor)
                degree_sets[degree - 1].add(neighbor)
            order.append(node)
            delete_node(graph, node)
    return order

#print targeted_order(GRAPH7)
#print fast_targeted_order(GRAPH7)

def main():

    m = 5
    fast_times = []
    targeted_times = []
    x = range(10, 1000, 10)

    for n in x:
        graph = upa(n, m)
        start_time = timeit.default_timer()
        fast_targeted_order(graph)
        end_time = timeit.default_timer() - start_time
        fast_times.append(end_time)

        start_time = timeit.default_timer()
        targeted_order(graph)
        end_time = timeit.default_timer() - start_time
        targeted_times.append(end_time)

    print fast_times
    print targeted_times



    plt.xlabel('Number of Nodes')
    plt.ylabel('Running Time in seconds')
    plt.title('Fast Targeted vs Targeted Order functions runtime (Desktop Python)')
    plt.plot(x, fast_times, '-b', label='Fast Targeted')
    plt.plot(x, targeted_times, '-r', label='Targeted Order')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.savefig('targeted.png')
    plt.show()

if __name__ == '__main__':
    main()