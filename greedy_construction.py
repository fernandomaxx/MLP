from heapq import heapify, heappop, heappush
from random import randrange


class GreddyConstruction(object):

    def __init__(self, adj_list, size):
        self.size = size
        self.adj_list = adj_list

    def build(self, alfa, solution, origin=0):
        processed = [False for i in range(self.size)]
        pq = [(0, origin)]
        heapify(pq)

        while pq:
            print(pq)
            index = randrange(0, alfa * (len(pq) - 1) + 1)
            u = pq[index][1]
            solution.append(u)
            processed[u] = True
            pq.clear()

            for i in range(0, len(self.adj_list[u])):
                v = self.adj_list[u][i][0]
                if not processed[v]:
                    cost = self.adj_list[u][i][1]
                    heappush(pq, (cost, v))

        solution.append(self.size)
