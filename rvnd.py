from cache import Cache
from shiftn import Shift
from twoopt import TwoOpt
from swap import Swap
from random import randrange

class RVND(object):
    def __init__(self, solution, adj_matrix):
        self._cache = Cache(adj_matrix)
        self._cache.update(solution)
        self.best_ = self._cache.compare([(0, len(solution))])
        self.best_sol = [(0, len(solution))]
        self.solution = solution
    
    def execute(self):
        #debug
        print(self.solution)
        N = [Shift(self._cache), Shift(self._cache, 2), 
            Shift(self._cache, 3),Swap(self._cache), TwoOpt(self._cache)]

        while N:
            #debug
            print(N, end=' ')
            i = randrange(0, len(N))
            print(i)
            
            if N[i].execute(self.solution):
                N = [Swap(self._cache), TwoOpt(self._cache)]
            else:
                del N[i]

        print(self.solution)
        return self.solution
