import numpy as np

class AdjacencyMatrix(object):

    def __init__(self, size):
        self.__mtx_adj = np.zeros((size,size))
        for i in range(size):
            self.__mtx_adj[i, i] = np.Infinity

    def insert(self, u, v, cost):
        self.__mtx_adj[u, v] = cost

    def setGraph(self, mtx_adj):
        self.__mtx_adj = mtx_adj
        for i in range(len(mtx_adj)):
            self.__mtx_adj[i, i] = np.Infinity

    def p_matrix(self):
        return self.__mtx_adj
