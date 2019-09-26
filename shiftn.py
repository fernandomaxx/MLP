from neighborhoods import Neighborhood

class Shift(Neighborhood):
    def __init__(self, cache, n=1):
        self._cache = cache
        self.n = n

    def execute(self, solution, block_position):
        best = self._cache.compare([(0, len(solution))])
        best_sol = solution
        for i in range(1, len(solution)-1):
            right_lim = len(solution) - i - 1
            left_lim  = len(solution) - right_lim - 1 

            left_size  = 1
            mid_right_size = left_lim - 1

            mid_left_size  = 0
            right_size = right_lim

            right_pos = len(solution) - right_size
            left_pos = 1

            for j in range(len(solution) - 2):
                sol = [(0, left_size),
                        (i+1, mid_left_size),
                        (i,1), # position of the shifted
                        (left_pos, mid_right_size),
                        (right_pos,right_size)]

                if right_size - 1 >= 0 and left_size == left_lim:
                    right_size -= 1; mid_left_size += 1
                    right_pos += 1

                if left_size + 1 <= left_lim:
                    left_size += 1; mid_right_size -= 1
                    left_pos += 1

                aux = self._cache.compare(sol)
                if best.C > aux.C:
                    best = aux
                    best_sol = sol
        sol = []
        for i,j in best_sol:
            if j:
                for k in solution[i:i+j]:
                    sol.append(k)
        return sol

