from neighborhoods import Neighborhood
from tools import f, idxToList

class Swap(Neighborhood):
    def __init__(self, cache):
        self._cache = cache

    def execute(self, solution):
        best_ = best = self._cache.compare([(0, len(solution))])
        best_sol = [(0, len(solution))]

        for i in range(1, len(solution) - 1):
            for j in range(i + 1 ,len(solution) - 1):
                
                if (j - i) != 1:
                    sol = [(0, i), (j, 1), (i + 1, (j - i) - 1), 
                        (i, 1), (j + 1, len(solution) - (j + 1))]
                
                else:
                    sol = [(0, i), (j, 1), 
                        (i, 1), (j + 1, len(solution) - (j + 1))]

                aux = self._cache.compare(sol)

                #debug
                print('---------------')
                print('{} {}'.format(best.C, aux.C))
                a = idxToList(best_sol, solution)
                b = idxToList(sol, solution)
                mtx = self._cache.getG()
                print('{} {}'.format(f(a, mtx), f(b, mtx)))
                print('---------------')

                if best.C > aux.C:
                    best = aux
                    best_sol = sol

        sol = []

        if best_.C > best.C:
            for i,j in best_sol:
                if j:
                    for k in solution[i:i+j]:
                        sol.append(k)
            solution[:] = sol[:]
            self._cache.update(solution)
            return True

        return False