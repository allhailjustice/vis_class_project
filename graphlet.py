import numpy as np


def sort(x, y):
    return min(x,y),max(x,y)


def RW(matrix):
    type_dic = {(1,1,1,2,3): 'g10', (1,1,1,1,4): 'g11', (1,1,2,3,3): 'g12', (1,1,2,2,4): 'g14',
                (2,2,2,2,2): 'g15', (1,2,2,3,4): 'g17', (2,2,2,2,4): 'g18', (1,2,3,3,3): 'g19',
                (2,2,2,4,4): 'g22', (1,3,3,3,4): 'g23', (2,2,3,3,4): 'g24', (2,3,3,3,3): 'g25', (2,3,3,4,4): 'g26',
                (3,3,3,3,4): 'g27', (3,3,4,4,4): 'g28', (4,4,4,4,4): 'g29', (1,1,2,2,2): 'g9'}
    count_dic = {'g10': 0, 'g11': 0, 'g12': 0, 'g13': 0, 'g14': 0, 'g15': 0, 'g16': 0, 'g17': 0, 'g18': 0, 'g19': 0,
                 'g20': 0, 'g21': 0, 'g22': 0, 'g23': 0, 'g24': 0, 'g25': 0, 'g26': 0, 'g27': 0, 'g28': 0, 'g29': 0,
                 'g9': 0}
    coe_dic = {'g10': 2, 'g11': 12, 'g12': 5, 'g13': 4, 'g14': 16, 'g15': 5, 'g16': 6, 'g17': 24, 'g18': 24, 'g19': 12,
               'g20': 18, 'g21': 15, 'g22': 54, 'g23': 36, 'g24': 42, 'g25': 34, 'g26': 82, 'g27': 76, 'g28': 144,
               'g29': 240, 'g9': 1}
    d2_graph = {}
    X = []

    def add2graph(coord):
        if coord not in list(d2_graph.keys()):
            d2_graph[coord] = add_neighbours(coord)

    def add_neighbours(coord):
        neighbours = [sort(i, coord[0]) for i in np.arange(matrix.shape[0])[matrix[coord[0]] > 0]
                      if sort(i, coord[0]) != coord]
        neighbours.extend([sort(i, coord[1]) for i in np.arange(matrix.shape[0])[matrix[coord[1]] > 0]
                           if sort(i, coord[1]) != coord])
        return neighbours

    def sample(X):
        if len(X) < 4:
            return
        points = np.unique(X[-4:])
        if len(points) < 5:
            return
        submatrix = matrix[np.ix_(points, points)]
        degrees = tuple(np.sort(np.sum(submatrix, axis=1)))
        if degrees == (1,2,2,2,3):
            d1 = submatrix[np.sum(submatrix, axis=1) == 1][0]
            d1n = submatrix[d1 == 1]
            if np.sum(d1n) == 2:
                graphlet_type = 'g13'
            else:
                graphlet_type = 'g16'
        elif degrees == (2,2,2,3,3):
            i, j = np.argwhere(submatrix[np.sum(submatrix, axis=1) == 3])[0]
            if submatrix[i,j] == 1:
                graphlet_type = 'g21'
            else:
                graphlet_type = 'g20'
        else:
            graphlet_type = type_dic[degrees]
        coe = 1
        for cox in X[-3:-1]:
            coe *= len(d2_graph[cox])
        count_dic[graphlet_type] += 1*coe/coe_dic[graphlet_type]
        # count_dic[graphlet_type] += 1

    init_x = np.random.choice(np.arange(matrix.shape[0])[np.sum(matrix,axis=0) > 0], 1)[0]
    init_y = np.random.choice(np.arange(matrix.shape[0])[matrix[init_x] > 0], 1)[0]
    coord = [init_x, init_y]
    coord.sort()
    coord = tuple(coord)

    for i in range(100):
        add2graph(coord)
        X.append(coord)
        sample(X)
        coord = d2_graph[coord][np.random.choice(len(d2_graph[coord]), 1)[0]]
    return np.array(list(count_dic.values()))


def create_matrix(nv,ne):
    matrix = np.zeros((nv, nv))
    i, j = np.random.choice(nv, 2, replace=False)
    matrix[i, j] = 1
    matrix[j, i] = 1
    for _ in range(ne):
        i = j
        while True:
            j = np.random.choice(nv, 1)[0]
            if j != i:
                break
        matrix[i, j] = 1
        matrix[j, i] = 1
    return matrix

