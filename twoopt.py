from neighborhoods import Neighborhood
from tools import f, idxToList

class TwoOpt(Neighborhood):
    def __init__(self, cache):
        self._cache = cache

    def execute(self, solution):
        best_ = best = self._cache.compare([(0, len(solution))])
        best_sol = [(0, len(solution))]

        for i in range(1 , len(solution) - 2):
            for j in range(i , len(solution) - i):

                sol = [(0, i)]

#                sol.append((i, -j))
                for k in range(j, i - 1, -1):
                    sol.append((k, 1))

                sol.append((j + 1, len(solution) - (j + 1)))

                #debug
#                print(sol)
                
                a = self._cache.compare(best_sol)
                aux = self._cache.compare(sol)

                #debug
#                print('---------------')
#                print('{} {}'.format(best.C, aux.C))
#                a = idxToList(best_sol, solution)
#                b = idxToList(sol, solution)
#                mtx = self._cache.getG()
#                print('{} {}'.format(f(a, mtx), f(b, mtx)))
#                print('---------------')

                if best.C > aux.C:
                    best = aux
                    best_sol = sol

        sol = []

        if best_.C > best.C:
            for i,j in best_sol:
                if j:
                    j = abs(j)
                    for k in solution[i:i+j]:
                        sol.append(k)
            solution[:] = sol[:]
            self._cache.update(solution)
            return True

        return False
