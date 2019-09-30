from random import randint
from adjacency_list import AdjacencyList


class GreddyConstruction(object):

    def __init__(self, adj_matrix, size):
        self.size = size
        self.adj_list = AdjacencyList(size)
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                aux = adj_matrix[i][j]
                self.adj_list.insert(i, j, aux)
                self.adj_list.insert(j,i,aux)
        self.adj_list = self.adj_list.p_list()

    def build(self, alfa, solution, origin=0):
        processed = [False for i in range(self.size)]
        pq = [(0, origin)]

        while pq:
            index = randint(0, int(alfa * len(pq))) - 1
            u = pq[0 if index < 0 else index][1]
            solution.append(u)
            processed[u] = True
            pq.clear()

            for i in range(0, len(self.adj_list[u])):
                v = self.adj_list[u][i][0]
                if not processed[v]:
                    cost = self.adj_list[u][i][1]
                    pq.append((cost, v))
            
            pq.sort()

        solution.append(0)
