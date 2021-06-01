from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import Delaunay
import numpy as np

from random import randint, choice

import matplotlib.pyplot as plt

from sp_motor.map.generate_classes import Spawn_zonne, System
from sp_motor.utils import dist
from sp_motor.game_classes.map import Map


####global var###############
default_system_radius = 2


#############################


def minimal_tree(system_zonne):
    X = csr_matrix(system_zonne.adja_mat())
    Tcsr = minimum_spanning_tree(X)
    return Tcsr.toarray().astype(float)
    

def get_delaunay(system_zonne):
    points = system_zonne.get_points()
    vertices = Delaunay(points)

    triangles = points[vertices.simplices]
    simplexes = np.array([[0 for i in range(points.shape[0])] for i in range(points.shape[0])])

    for t in range(triangles.shape[0]):
        for p in range(triangles.shape[1]):
            coord1 = (triangles[t, p, 0], triangles[t, p, 1])
            coord2 = (triangles[t, (p + 1) % triangles.shape[1], 0], triangles[t, (p + 1) % triangles.shape[1], 1])
            p1 = system_zonne.get_child(coord1)
            p2 = system_zonne.get_child(coord2)
            simplexes[p1, p2] = dist(system_zonne.children[p1].pos, system_zonne.children[p2].pos)

    return simplexes

    
def treat_delaunay(simplexes):
    output = np.array([[0 for i in range(simplexes.shape[0])] for i in range(simplexes.shape[1])])
    for i in range(simplexes.shape[0]):
        for j in range(simplexes.shape[1]):
            if simplexes[i, j]:
                output[i, j] = 1

    return output

def prune_graph(delaunay, m_tree, min_add=0, max_add=1):
    n = delaunay.shape[0]
    new_graph = np.array([[0 for i in range(n)] for i in range(n)])

    possible_add = delaunay - m_tree
    for i in range(n):
        friends = list(possible_add[i])
        max_f = randint(min_add, max_add)

        for step in range(max_f):
            poss_val = list(set(friends))
            if len(poss_val) != 0:
                indice = friends.index(choice(poss_val))

                new_graph[i, indice] = friends[indice]

                poss_val.pop(poss_val.index(friends[indice]))

    return new_graph + m_tree



def id_neighbors(graph):
    output = []
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph[i, j] > 0:

                output.append({
                    "sys1":i,
                    "sys2":j,
                })

    return output




def find_contact(system_1, system_2, max_radius):
    minimal, id1, id2 = max_radius, 0, 0
    for i in range(len(system_1.children)):
        for j in range(len(system_2.children)):
            distance = dist(system_1.children[i].pos, system_2.children[j].pos)
            if distance < minimal:
                minimal = distance
                id1 = i
                id2 = j

    return (id1, id2, minimal)




def create_map(radius=600, nb_zonnes=(10, 14), zonnes_r=(40, 80), systems=(10, 20)):
    #creer la zonne de la map
    map = Spawn_zonne(1000, 1000, 1000)

    #trouver un nombre d'amas d'étoiles à créer
    nb_z = randint(nb_zonnes[0], nb_zonnes[1])

    for i in range(nb_z):
        #les créer
        map.make_spawn(zonnes_r[0], zonnes_r[1])
    
    #on calcule le graph reliant les amas
    adja_max = get_delaunay(map)
    r = minimal_tree(map)
    amas_graph = prune_graph(adja_max, r)

    #pr chaque amas, on vient créer ses systèmes, et on en fait le graphe
    for i in range(len(map.children)):
        nb_s = randint(systems[0], systems[1])
        for j in range(nb_s):
            map.children
            map.children[i].make_spawn(default_system_radius, default_system_radius)

        adja_max = get_delaunay(map.children[i])
        r = minimal_tree(map.children[i])
        map.children[i].graph = prune_graph(adja_max, r)


    nb_total_syst = 0
    for child in map.children:
        nb_total_syst += child.graph.shape[0]


    #on vient ajouter dans le graphe général de la map les liens locaux
    map.graph = np.array([[0 for i in range(nb_total_syst)] for i in range(nb_total_syst)])
    for child in range(len(map.children)):
        for i in range(map.children[child].graph.shape[0]):
            for j in range(map.children[child].graph.shape[1]):
                map.graph[child +i, child+j] = map.children[child].graph[i, j]



    #on vient ajouter les liens entre les amas stellaires dans le graphe gen
    neighbors = id_neighbors(amas_graph)

    for link in neighbors:
        contact = find_contact(map.children[link["sys1"]], map.children[link["sys2"]], radius)

        map.graph[link["sys1"] + contact[0], link["sys2"] + contact[1]] = contact[2]


    return map
    



create_map()






