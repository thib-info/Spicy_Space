import numpy as np

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

        self.amas = []
        self.systems = []
        Amas_constructor.__init__(self, pos)


    def import_amas(self, amas_coll):
        for i in range(len(amas_coll)):
            self.amas.append(amas_coll[i].graph.shape[0])

    
        for ama in self.amas:
            for i in range(ama):
                self.systems.append(i)

    def get_system_id(self, child_id, internal_id):
        return sum(self.amas[:child_id]) + internal_id


    def add_amas_links(self, neigh, contacts):

        for i in range(len(neigh)):
            sys1_id, sys2_id = neigh[i]["sys1"], neigh[i]["sys2"]
            intern1_id, intern2_id, cost = contacts[i]

        self.children[sys1_id].children[intern1_id].add_neighbor
            

   

    
    

    