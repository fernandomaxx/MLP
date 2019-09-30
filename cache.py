import numpy as np

T = 0
C = 1
W = 2

class Cache(object):

    def __init__(self, adj_matrix):
        '''
            Object that store and manage an solution helper.
            n: Size of the problem
        '''
        self._adj_matrix = adj_matrix
        self._n = len(adj_matrix) + 1
        self._table = []

    def update(self, solution):
        '''
            updates the state to a given solution
            solution: a list with a path
        '''
        self._table = []

        for i in range(self._n):
            self._table.append(
                    [SubSolution(i, 1, self._adj_matrix, solution)]
                    )

        for i in range(self._n - 1):
            for j in range(i+1, self._n):
                self._table[i].append(self._table[i][-1] + self._table[j][0])

    def compare(self, sigmas):
        '''
            Calculates the new Solution in the cost of the parts that were moved
            sigmas: a list of tuples, where each tuple contains a position in solution and the size of the solution
        '''
        i,j = sigmas[0]
        new_sol = self._table[i][j-1]
        for i,j in sigmas[1:]:
            if j:
                new_sol += self._table[i][j-1]
        return new_sol

    #temp
    def getG(self):
        return self._adj_matrix

class SubSolution(object):
    def __init__(self, start, size, adj_matrix, solution, T=0, C=0, W=1):
        self.start = start
        self.size = size
        self.T = T
        self.C = C
        self.W = W if start else 0

        self.last = self.start

        self._adj_matrix = adj_matrix
        self._solution = solution

    def __add__(self, other):
        sub_solution = SubSolution(self.start, 
                self.size + other.size,
                self._adj_matrix, 
                self._solution)

        i = self._solution[self.last]
        j = self._solution[other.start]
        t = self._adj_matrix[i, j]

        sub_solution.T = self.T + t + other.T
        sub_solution.C = self.C + other.W * (self.T + t) + other.C
        sub_solution.W = self.W + other.W

        sub_solution.last = other.last

        return sub_solution

    def __str__(self):
        return "T={} C={} W={}".format(self.T, self.C, self.W)

