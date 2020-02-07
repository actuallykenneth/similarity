"""
zel90.py

Zelenka algorithms
"""

import sys
import os
from mcs import maximum_common_induced_subgraph
import networkx as nx


def contraction_distance(G1, G2, verbose=True):
    """returns Zel90 contraction distance"""

    # suppress intermediate results from MCIS function by default
    if verbose is not True:
        sys.stdout = open(os.devnull, 'w')

    if(len(G1) != len(G2)):
        return ("Error: Graphs must be of same size")

    N = len(G1)
    communs = maximum_common_induced_subgraph(G1, G2, 4, False, True)
    K = len(communs[0][0])
    contracDis = N - K

    # re-enable standard output
    sys.stdout = sys.__stdout__

    return contracDis


if __name__ == "__main__":
    
    M = nx.Graph()
    M.add_edges_from([(0,1),
                  (1,2),
                  (1,3),
                  (2,4),
                  (4,3),
                  (0,6),
                  (6,5),
                  (5,0)
                 ])

    M2 = nx.Graph()
    M2.add_edges_from([(0,1),
                  (1,2),
                  (1,3),
                  (2,4),
                  (4,3),
                  (0,6),
                  (5,0)
                 ])

    print(contraction_distance(M, M2, verbose=False))
