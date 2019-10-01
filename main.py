
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
from verbosity import Verbosity

parser = argparse.ArgumentParser()

parser.add_argument("matrix_path", 
        help='Show where is the problem.')
parser.add_argument('-g', "--greedyness", 
        help='The alpha for indicate the greedyness of the solution construction',
        default=1,
        type=float)
parser.add_argument('-v', '--verbosity', 
        help='If the program will print during the execution',
        action='store_true')
parser.add_argument('-i','--iterations', 
        help='quantity of iterations',
        default=10,
        type=int)
parser.add_argument('-l','--ilsiterations', 
        help='quantity of iterations',
        default=10,
        type=int)

args = parser.parse_args()

Verbosity.verbo = args.verbosity 

def load_problem(path):                                                          
    aux = to_numpy_array(tsplib95.load_problem(path).get_graph())                
    return aux  

adj_matrix = load_problem(args.matrix_path)
ils = ILS(adj_matrix,
        args.iterations,
        args.ilsiterations,
        greedyness=args.greedyness)
x = ils.procedure()
print(x)


