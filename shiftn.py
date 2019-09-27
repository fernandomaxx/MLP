from neighborhoods import Neighborhood

class Shift(Neighborhood):
    def __init__(self, cache, n=1):
        assert n > 0
        self._cache = cache
        self.n = n

    def execute(self, solution):
        best = self._cache.compare([(0, len(solution))])
        best_sol = solution
        for i in range(1, len(solution)-self.n):
            right_lim = len(solution) - i - self.n
            left_lim  = len(solution) - right_lim - self.n 

            left_size  = 1
            mid_right_size = left_lim - 1

            mid_left_size  = 0
            right_size = right_lim

            right_pos = len(solution) - right_size
            left_pos = 1

            for j in range(len(solution) - 1 - self.n):
                sol = [(0, left_size),
                        (i+self.n, mid_left_size),
                        (i,self.n), # position of the shifted
                        (left_pos, mid_right_size),
                        (right_pos,right_size)]
                print(sol)

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
            print()
        sol = []
        for i,j in best_sol:
            if j:
                for k in solution[i:i+j]:
                    sol.append(k)
        return best_sol
