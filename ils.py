from greedy_construction import GreddyConstruction
from rvnd import RVND
from tools import f
from shiftn import Shift
from cache import Cache
from verbosity import Verbosity
from random import shuffle, choice

import numpy as np

class ILS(object):

    def __init__(self, adj_matrix, Max, MaxIls, greedyness):
        self.Max = Max
        self.MaxIls = MaxIls
        self._adj_matrix = adj_matrix

        self.cache = Cache(self._adj_matrix)

        self.gd = GreddyConstruction(adj_matrix, len(adj_matrix))
        self.greedyness = greedyness

    def procedure(self):
        best_ = np.Inf
        best_sol = []

        self.gd.build(self.greedyness, best_sol)
        best_ = f(best_sol, self._adj_matrix)

        for iter in range(self.Max):
            new_sol = []
            self.gd.build(self.greedyness, new_sol)
            #Entrada que o shift 2 piora
            #new_sol = [0, 2, 4, 1, 3, 0]
            new_ = f(new_sol, self._adj_matrix)
            aux_sol = [i for i in new_sol]
            aux_ = new_
            print('s=',aux_)

            iterIls = 0
            while iterIls < self.MaxIls:
                #debug
                #print((new_sol, new_))

                new_sol = RVND(new_sol, self._adj_matrix, self.cache).execute()
                new_ = f(new_sol, self._adj_matrix)
                #debug
                #print((new_sol, new_))
                
                if aux_ > new_:
                    aux_ = new_
                    aux_sol = [i for i in new_sol]
                    iterIls = 0

                #falta a pertubação
                n = 5
                x = (len(aux_sol)) // n
                s = [aux_sol[1:x],aux_sol[(n-1)*x:len(aux_sol) - 1]]
                for i in range(1,n-1):
                    a = choice([-1,1])
                    s.append(aux_sol[i*x:(i+1)*x][::a])
                shuffle(new_sol)
                a = []
                for e in s:
                    a += e
                new_sol =  [0] + a + [0]
                new_ = f(new_sol, self._adj_matrix)
                print("p =", new_)

                iterIls += 1

            if best_ > aux_:
                best_sol = aux_sol
                best_ = aux_

            Verbosity.show(
                "{}/{} b={} a={}".format(iter + 1,
                                  self.Max,
                                  best_,
                                  aux_)
            )
        return (best_sol, best_)

                
