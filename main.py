import argparse
import sys

from adjacency_matrix import AdjacencyMatrix
from greedy_construction import GreddyConstruction
from adjacency_list import AdjacencyList
from ils import ILS
from cache import Cache
from tools import f
from shiftn import Shift
from tsplib95 import tsplib95
from networkx import to_numpy_array

adj_list = AdjacencyList(5)
adj_matrix = AdjacencyMatrix(5)

sys.stdin = open("input", "r")

def load_problem(path):                                                          
    aux = to_numpy_array(tsplib95.load_problem(path).get_graph())                
    for i in range(len(aux)):                                                    
        aux[i][i] = np.Infinity                                                  
    return aux  

for i in range(0, 10):
    line = input()
    adj_list.insert(int(line[0]), int(line[2]), int(line[4]))
    adj_list.insert(int(line[2]), int(line[0]), int(line[4]))
    adj_matrix.insert(int(line[0]), int(line[2]), int(line[4]))
    adj_matrix.insert(int(line[2]), int(line[0]), int(line[4]))

print(adj_matrix.p_matrix())
ils = ILS(adj_matrix.p_matrix(), 1, 2)
print(ils.procedure())
