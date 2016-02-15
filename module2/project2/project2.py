"""Breadth-first search implementation."""

from collections import deque
#from test_graphs import *
from module2.app2.helper import copy_graph

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and returns the
    set consisting of all nodes that are visited by a breadth-first search that
    starts at start_node.

    :param ugraph: dict - undirected graph representation.
    :param start_node: int - node.
    :return: set - visited nodes.
    """

    queue = deque()
    visited = {start_node}
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, where each set
     consists of all the nodes (and nothing else) in a connected component, and
     there is exactly one set in the list for each connected component in ugraph
    and nothing else.

    :param ugraph: dict - undirected graph representation
    :return: list of sets
    """
    remaining_nodes = ugraph.keys()
    connected_components = []
    while remaining_nodes:
        node = remaining_nodes.pop()
        visited = bfs_visited(ugraph, node)
        connected_components.append(visited)
        remaining_nodes = list(set(remaining_nodes) - visited)
    return connected_components


def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of the
    largest connected component in ugraph.

    :param ugraph: dict - undirected graph representation
    :return: int
    """
    cc_size = [len(x) for x in cc_visited(ugraph)]
    return max(cc_size) if cc_size else 0

def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and iterates
    through the nodes in attack_order. For each node in the list, the function
    removes the given node and its edges from the graph and then computes the
    size of the largest connected component for the resulting graph.

    :param ugraph: dict - undirected graph representation
    :param attack_order: list - of nodes
    :return: list of int
    """

    results = [largest_cc_size(ugraph)]
    remaining_nodes = copy_graph(ugraph)
    for node in attack_order:
        del remaining_nodes[node]
        for edges in remaining_nodes.itervalues():
            if node in edges:
                edges.remove(node)
        largest_cc = largest_cc_size(remaining_nodes)
        results.append(largest_cc)
    return results


#print bfs_visited(GRAPH0, 1)
#print cc_visited(GRAPH0)
#print largest_cc_size(GRAPH10)
#print compute_resilience(GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])