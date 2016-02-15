"""
This is a module with a collection of functions to create different types of
undirected graphs.
"""
import random
from matplotlib import pyplot as plt

from helper import load_graph, NETWORK_URL
from upatrial import *
from module2.project2.project2 import compute_resilience

def network_graph():
    """
    Creates an undirected graph representation of a computer network.

    :return: dict
    """

    return load_graph(NETWORK_URL)

#print network_graph()

#ng = network_graph()
#sz = sum([len(x) for x in ng.itervalues()])
#print sz/2


def make_complete_graph(num_nodes):
    """ Takes the number of nodes num_nodes and returns a dictionary
    corresponding to a complete undirected graph with the specified number of
    nodes.
    """

    graph = {0: set([])}
    if num_nodes > 0:
        for node in range(num_nodes):
            edges = []
            for edge in range(num_nodes):
                if node != edge:
                    edges.append(edge)
                    if edge not in graph.keys():
                        graph[edge] = {node}
                    else:
                        graph[edge].add(node)
            graph[node] = set(edges)
    return graph

#print make_complete_graph(5)

def er_graph(num_nodes, probability):
    """
    Generate a random undirected graph with n number of nodes and edges based on
    probability p
    """
    random.seed(0)
    if num_nodes > 0:
        graph = {x: set([]) for x in range(num_nodes)}
        for node in range(num_nodes):
            for edge in range(num_nodes):
                if node != edge:
                    a = random.random()
                    if a < probability:
                        graph[node].add(edge)
                        graph[edge].add(node)
        return graph
    else:
        return {0: set([])}



#print er_graph(10, 0.5)


def upa(n, m):
    """
    :param n: (int) final number of nodes in the graph
    :param m: (int) m <= n, which is the number of existing nodes to which a
    new node is connected during each iteration.
    :return: (dict) directed graph
    """

    graph = make_complete_graph(m)
    #print graph
    trial = UPATrial(m)

    for i in range(m, n):
        neighbors = trial.run_trial(m)
        graph[i] = neighbors
        for neighbor in neighbors:
            if neighbor not in graph.keys():
                graph[neighbor] = {i}
            else:
                graph[neighbor].add(i)
    return graph

#print upa(10, 5)


def random_order(ugraph):
    """
    Takes a graph and returns a list of the nodes in the graph in some random
    order.

    :param ugraph: dict
    :return: list
    """

    nodes = ugraph.keys()
    random.shuffle(nodes)
    return nodes


def calculate_resilience(ugraph):
    """
    Generates a random attack order and calculates the resilience for a given
    graph.

    :param ugraph: dict
    :return: list
    """

    attack_order = random_order(ugraph)
    return compute_resilience(ugraph, attack_order)

def main():

    net_graph = network_graph()
    net_size = sum([len(x) for x in net_graph.itervalues()])
    print net_size/2
    print (net_size/2)/len(net_graph)

    # net_attack = random_order(net_graph)
    net_resilience = calculate_resilience(net_graph)
    print net_resilience

    e_graph = er_graph(1239, 0.0020)
    size = sum([len(x) for x in e_graph.itervalues()])
    print size/2
    print (size/2)/len(e_graph)

    # e_attack = random_order(e_graph)
    e_resilience = calculate_resilience(e_graph)
    print e_resilience

    upa_graph = upa(1239, 3)
    #print upa_graph
    upa_size = sum([len(x) for x in upa_graph.itervalues()])
    print upa_size/2
    print (upa_size/2)/len(upa_graph)

    upa_resilience = calculate_resilience(upa_graph)
    print upa_resilience

    x = list(range(max(len(net_resilience), len(e_resilience),
                       len(upa_resilience))))


    plt.xlabel('Number of nodes removed')
    plt.ylabel('Size of the largest connected component')
    plt.title('Resilience of computer networks under attack')
    plt.plot(x, net_resilience, '-b', label='Network')
    plt.plot(x, e_resilience, '-r', label='ER | p = 0.0020')
    plt.plot(x, upa_resilience, '-y', label='UPA | m = 3')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig('resilience.png')
    plt.show()


if __name__ == '__main__':
    #pass
    main()