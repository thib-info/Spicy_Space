from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import Delaunay
import numpy as np

import matplotlib.pyplot as plt

from sp_motor.map.generate_classes import Spawn_zonne, System
from sp_motor.utils import dist


def minimal_tree(system_zonne):
    X = csr_matrix(system_zonne.adja_mat())
    Tcsr = minimum_spanning_tree(X)
    return Tcsr.toarray().astype(float)
    

def get_delaunay(system_zonne):
    points = system_zonne.get_points()
    vertices = Delaunay(points)

    # print(vertices.simplices)
    # plt.triplot(points[:,0], points[:,1], vertices.simplices)
    # plt.plot(points[:,0], points[:,1], 'o')
    # plt.show()

    triangles = points[vertices.simplices]
    simplexes = np.array([[0 for i in range(points.shape[0])] for i in range(points.shape[0])])

    for t in range(triangles.shape[0]):
        for p in range(triangles.shape[1]):
            coord1 = (triangles[t, p, 0], triangles[t, p, 1])
            coord2 = (triangles[t, (p + 1) % triangles.shape[1], 0], triangles[t, (p + 1) % triangles.shape[1], 1])
            p1 = system_zonne.get_child(coord1)
            p2 = system_zonne.get_child(coord2)
            print(p1, "lol")
            simplexes[p1, p2] = dist(system_zonne.children[p1].pos, system_zonne.children[p2].pos)

    return simplexes

    
def treat_delaunay(simplexes):
    output = np.array([[0 for i in range(simplexes.shape[0])] for i in range(simplexes.shape[1])])
    for i in range(simplexes.shape[0]):
        for j in range(simplexes.shape[1]):
            if simplexes[i, j]:
                output[i, j] = 1

    output = list(output)
    for i in range(len(output)):
        output[i] = list(output[i])
    return output

    

    # print(vertices.simplices)
    # print(vertices.simplices.shape)



map = Spawn_zonne(1000, 1000, 1000)
for i in range(6):
    map.make_spawn(15, 60)

print(map.adja_mat())
print(map.adja_mat().shape)

adja_max = get_delaunay(map)

print(adja_max)
print(treat_delaunay(adja_max))

# r = minimal_tree(map)
# print(r)