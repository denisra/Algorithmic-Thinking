"""
Calculates the resilience of different graphs using the fast_targeted_order
function to generate the attack order.
"""

from matplotlib import pyplot as plt
import numpy as np

from app2 import network_graph, er_graph, upa
from targeted_order import fast_targeted_order
from helper import targeted_order
from module2.project2.project2 import compute_resilience


def calculate_resilience(ugraph):
    """
    Generates a random attack order and calculates the resilience for a given
    graph.

    :param ugraph: dict
    :return: list
    """

    attack_order = fast_targeted_order(ugraph)
    #attack_order = targeted_order(ugraph)
    return compute_resilience(ugraph, attack_order)


def main():

    net_graph = network_graph()
    net_size = sum([len(x) for x in net_graph.itervalues()])
    print net_size/2

    # net_attack = random_order(net_graph)
    net_resilience = np.array(calculate_resilience(net_graph))
    print 'net: ', sum([len(x) for x in net_graph.itervalues()])/len(net_graph)

    e_graph = er_graph(1239, 0.0020)
    size = sum([len(x) for x in e_graph.itervalues()])
    print size/2
    print e_graph

    # e_attack = random_order(e_graph)
    e_resilience = np.array(calculate_resilience(e_graph))
    print 'e: ', sum([len(x) for x in e_graph.itervalues()])/len(e_graph)

    upa_graph = upa(1239, 3)
    #print upa_graph
    upa_size = sum([len(x) for x in upa_graph.itervalues()])
    print upa_size/2

    upa_resilience = np.array(calculate_resilience(upa_graph))
    print 'upa: ', sum([len(x) for x in upa_graph.itervalues()])/len(upa_graph)

    x = np.array(range(max(len(net_resilience), len(e_resilience),
                       len(upa_resilience))))

    plt.xlabel('Number of nodes removed')
    plt.ylabel('Size of the largest connected component')
    plt.title('Resilience of computer networks under attack')
    plt.plot(x, net_resilience, '-b', label='Network')
    plt.plot(x, e_resilience, '-r', label='ER | p = 0.0020')
    plt.plot(x, upa_resilience, '-y', label='UPA | m = 3')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig('question4.png')
    plt.show()


if __name__ == '__main__':
    #pass
    main()