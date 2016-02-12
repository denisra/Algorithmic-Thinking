"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
import matplotlib.pyplot as plt


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors




from module1.project1.project1 import make_complete_graph, \
    in_degree_distribution, compute_in_degrees


def dpa(n, m):
    """
    :param n: (int) final number of nodes in the graph
    :param m: (int) m <= n, which is the number of existing nodes to which a
    new node is connected during each iteration.
    :return: (dict) directed graph
    """

    graph = make_complete_graph(m)
    print graph
    trial = DPATrial(m)

    for i in range(m, n):
        neighbors = trial.run_trial(m)
        graph[i] = neighbors
    return graph

graph = dpa(28000, 13)

#out_degree = [len(x) for x in graph.itervalues()]
#print 'out degree: ', out_degree
#print sum(out_degree)/len(out_degree)

dist = in_degree_distribution(graph)
print 'dist: ', dist
total = sum(dist.itervalues())
normalized = {key: float(value)/total for key, value in dist.items()}
#print(timeit.default_timer() - start_time)

x = normalized.keys()
y = normalized.values()
print len(y)
plt.loglog(x, y, 'ro')

plt.yscale('log')
plt.xscale('log')
plt.minorticks_off()

plt.xlabel('In-degree distribution')
plt.ylabel('Normalized In-degree distribution')
plt.title('DPA Graph')
plt.grid(True)
plt.savefig('citations-q4.png')
plt.show()