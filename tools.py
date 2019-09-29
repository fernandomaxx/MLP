
def f(solution, adj_matrix):
    cost = 0
    lat_ant = 0
    for i in range(1, len(solution)):
        weight = adj_matrix[solution[i-1]][solution[i]]
        cost = cost + (weight + lat_ant)
        lat_ant += weight
        #print("{}{}".format(solution[i-1], solution[i]))

    return cost

def idxToList(sigmas, solution):
    sol = []
    for i,j in sigmas:
        if j:
            for k in solution[i:i+j]:
                sol.append(k)

    return sol