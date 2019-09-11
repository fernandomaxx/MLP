

class AdjacencyList():

    def __init__(self, size):
        self.__list_adj = [[] for _ in range(size)]

    def insert(self, u, v, cost):
        self.__list_adj[u].append((v, cost))

    def p_list(self):
        return self.__list_adj
