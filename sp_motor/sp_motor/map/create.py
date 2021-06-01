from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import Delaunay


import matplotlib.pyplot as plt

from sp_motor.map.generate_classes import Spawn_zonne, System



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

    print(vertices.simplices.shape)



map = Spawn_zonne(1000, 1000, 1000)
for i in range(40):
    map.make_spawn(15, 60)

print(map.adja_mat())
print(map.adja_mat().shape)

get_delaunay(map)

# r = minimal_tree(map)
# print(r)