import numpy as np
# from copy import deepcopy

from sp_motor.utils import calculate_cost



class Syst_obj_constructor():

    def __init__(self, pos):
        
        self.neighbors = []
        self.pos = pos
        

    def add_neighbor(self, indice, distance):
        self.neighbors.append({
            "dest":indice,
            "cost":calculate_cost(distance)
        })

    
class Amas_constructor(Syst_obj_constructor):

    def __init__(self, pos):
        self.children = []
        self.graph = None
        self.indice_start = 0
        Syst_obj_constructor.__init__(self, pos)


    def import_graph(self, graph):
        self.graph = graph

    def import_children(self, children, child_graph):
        self.children = children

        for i in range(child_graph.shape[0]):
            for j in range(child_graph.shape[1]):
                if child_graph[i, j] > 0:
                    self.children[i].add_neighbor(j, child_graph[i, j])
                    self.children[j].add_neighbor(i, child_graph[i, j])



class Map_constructor(Amas_constructor):
    def __init__(self, pos):

        # self.amas = []
        self.systems = []
        Amas_constructor.__init__(self, pos)


    def import_amas(self, amas_coll):
        #on vient ajouter les amas, pour les modifs, mais on les avait déjà inclus une fois avant dans import children
        for i in range(len(amas_coll)):
            list_copy = amas_coll.children[:]
            self.children[i].children = [len(self.systems) + z for z in range(len(list_copy))]
            self.children[i].indice_start = len(self.systems)


            #on vient réindexer les voisins
            for syst in range(len(list_copy)):
                for v in range(len(list_copy[syst].neighbors)):
                    temp_v = list_copy[syst].neighbors[v]
                    temp_v["dest"] += len(self.systems)
                    list_copy[syst].neighbors[v] = temp_v

            self.systems += list_copy


    #permet d'avoir l'id général du système en internal_id position d'un amas
    def get_system_id(self, child_id, internal_id):
        return self.children[child_id].children[internal_id]



    def add_amas_links(self, neigh, contacts):

        for i in range(len(neigh)):
            sys1_id, sys2_id = neigh[i]["sys1"], neigh[i]["sys2"]
            intern1_id, intern2_id, cost = contacts[i]
            
            intern1_id = get_system_id(sys1_id, intern1_id)
            intern2_id = get_system_id(sys2_id, intern2_id)


        self.children[intern1_id].add_neighbor(intern2_id, cost)
        self.children[intern2_id].add_neighbor(intern1_id, cost)


        
            

   

    
    

    