
import argparse
import sys
import numpy as np

from adjacency_matrix import AdjacencyMatrix
from greedy_construction import GreddyConstruction
from adjacency_list import AdjacencyList
from ils import ILS
from cache import Cache
from tools import f
from shiftn import Shift
from tsplib95 import tsplib95
from networkx import to_numpy_array

parser = argparse.ArgumentParser()

parser.add_argument("matrix_path", 
        help='Show where is the problem.')
parser.add_argument('-g', "--greedyness", 
        help='The alpha for indicate the greedyness of the solution construction',
        default=1,
        type=float)

args = parser.parse_args()

def load_problem(path):                                                          
    aux = to_numpy_array(tsplib95.load_problem(path).get_graph())                
    return aux  

adj_matrix = load_problem(args.matrix_path)
ils = ILS(adj_matrix, 10, 5, greedyness=args.greedyness)
x = ils.procedure()
print(x)


