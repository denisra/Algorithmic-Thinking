"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import timeit

import matplotlib.pyplot as plt

from module1.project1.project1 import compute_in_degrees, in_degree_distribution


# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    neighbors = [line.strip().split(' ') for line in graph_lines]
    answer_graph = {neighbor[0]: set(neighbor[1:]) for neighbor in neighbors}
    return answer_graph


def main():

    citation_graph = load_graph(CITATION_URL)

    print compute_in_degrees(citation_graph)


    start_time = timeit.default_timer()

    dist = in_degree_distribution(citation_graph)
    print 'dist =', dist
    total = sum(dist.itervalues())
    normalized = {key: float(value)/total for key, value in dist.items()}
    print(timeit.default_timer() - start_time)

    x = normalized.keys()
    y = normalized.values()
    print len(y)
    plt.loglog(x, y, 'ro')

    plt.yscale('log')
    plt.xscale('log')
    plt.minorticks_off()

    plt.xlabel('In-degree distribution')
    plt.ylabel('Normalized In-degree distribution')
    plt.title('Graph of Citations')
    plt.grid(True)
    plt.savefig('citations-q1.png')
    plt.show()


if __name__ == '__main__':
    main()