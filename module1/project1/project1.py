""" This is a module that provides a collection of functions for graphic
representation and for computing degree distribution.
"""

EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]),
             4: set([1]), 5: set([2]), 6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]),
             4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """ Takes the number of nodes num_nodes and returns a dictionary
    corresponding to a complete directed graph with the specified number of
    nodes.
    """

    graph = {0: set([])}
    if num_nodes > 0:
        for node in range(num_nodes):
            edges = []
            for head in range(num_nodes):
                if node != head:
                    edges.append(head)
            graph[node] = set(edges)
    return graph

def compute_in_degrees(digraph):
    """ Takes a directed graph digraph (represented as a dictionary) and
    computes the in-degrees for the nodes in the graph. The function should
    return a dictionary with the same set of keys (nodes) as digraph whose
    corresponding values are the number of edges whose head matches a particular
     node.
    """
    degrees = {}
    for node in digraph:
        count = 0
        for head in digraph.itervalues():
            if node in head:
                count += 1
        degrees[node] = count
    return degrees

def in_degree_distribution(digraph):
    """ Takes a directed graph digraph (represented as a dictionary) and
    computes the unnormalized distribution of the in-degrees of the graph. The
    function should return a dictionary whose keys correspond to in-degrees of
    nodes in the graph. The value associated with each particular in-degree is
    the number of nodes with that in-degree. In-degrees with no corresponding
    nodes in the graph are not included in the dictionary.
    """
    degrees = compute_in_degrees(digraph)
    dist = {}
    for degree in degrees.itervalues():
        count = 0
        for value in degrees.itervalues():
            if value == degree:
                count += 1
        dist[degree] = count
    return dist


# print make_complete_graph(2)
# print make_complete_graph(8)
# print make_complete_graph(9)
# print make_complete_graph(0)

GRAPH3 = {0: set([1, 2, 3, 4]),
          1: set([0, 2, 3, 4]),
          2: set([0, 1, 3, 4]),
          3: set([0, 1, 2, 4]),
          4: set([0, 1, 2, 3])}

GRAPH5 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([4, 6, 8]),
          4: set([3, 5, 7]),
          5: set([6, 8]),
          6: set([5, 7]),
          7: set([8]),
          8: set([7])}

# compute_in_degrees(GRAPH3)
# compute_in_degrees(GRAPH5)
# in_degree_distribution(GRAPH3)
# in_degree_distribution(GRAPH5)