from greedy_construction import GreddyConstruction
from rvnd import RVND
from tools import f

import numpy as np

class ILS(object):

    def __init__(self, adj_list, adj_matrix, Max, MaxIls):
        self.Max = Max
        self.MaxIls = MaxIls
        self._adj_list = adj_list
        self._adj_matrix = adj_matrix
        self.gd = GreddyConstruction(adj_list,
            len(adj_matrix))

    def procedure(self):
        best_ = np.Inf
        best_sol = []

        for _ in range(self.Max):
            new_sol = []
            self.gd.build(1, new_sol)
            #Entrada que o shift 2 piora
            #new_sol = [0, 2, 4, 1, 3, 0]
            new_ = f(new_sol, self._adj_matrix)
            aux_sol = new_sol
            aux_ = new_

            #debug
            print('\n{}----------------'.format(_))
            print('{}: {}'.format(new_sol, new_))
            
            for iterIls in range(self.MaxIls):
                #debug
                print((new_sol, new_))

                new_sol = RVND(new_sol, self._adj_matrix).execute()
                new_ = f(new_sol, self._adj_matrix)
                #debug
                print((new_sol, new_))
                
                if aux_ > new_:
                    aux_ = new_
                    aux_sol = new_sol
                    iterIls = 0

                #falta a pertubação

            if best_ > aux_:
                best_sol = aux_sol
                best_ = aux_

        return (best_sol, best_)

                
