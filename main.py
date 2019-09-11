import sys
from adjacency_matrix import AdjacencyMatrix
from greedy_construction import GreddyConstruction
from adjacency_list import AdjacencyList

adj_list = AdjacencyList(5)

sys.stdin = open("input", "r")

for i in range(0, 10):
    line = input()
    adj_list.insert(int(line[0]), int(line[2]), int(line[4]))
    adj_list.insert(int(line[2]), int(line[0]), int(line[4]))

solution = []

gd = GreddyConstruction(adj_list.p_list(), 5)
gd.build(0, solution)
print(solution)
