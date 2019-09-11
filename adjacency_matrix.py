

class AdjacencyMatrix(object):

    def __init__(self, size):
        self.__mtx_adj = [[0] * size for _ in range(size)]

    def insert(self, u, v, cost):
        self.__mtx_adj[u].append((v, cost))

    def p_matrix(self):
        return self.__mtx_adj
