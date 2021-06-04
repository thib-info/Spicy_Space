import numpy as np
from copy import deepcopy
# from copy import deepcopy

from sp_motor.utils import calculate_cost




class Basic_info():

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    def get_pos(self):
        return self.pos[:]

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

class System_p(Basic_info):

    def __init__(self, name, pos):
        self.sector_id = 0
        self.ressources_slots = []
        self.units_id = []
        self.ressources_qt = {}
        Basic_info.__init__(self, name, pos)



    def set_sector(self, sector_id):
        self.sector_id = sector_id
    
    def get_sector_id(self):
        return self.sector_id

class Sectors(Basic_info):

    def __init__(self, name, pos):
        self.members = []

        Basic_info.__init__(self, name, pos)

    
    def set_systems_indices(self, syst_indices):
        self.members = syst_indices[:]
         



class Map(Basic_info):

    def __init__(self, name, pos):
        self.systems = []
        self.sectors = []
        self.graph_cost = None
        self.graph_link = None

        Basic_info.__init__(self, name, pos)

    
    def import_sectors(self, sectors):
        self.sectors = deepcopy(sectors)


    def import_systems(self, systems):
        self.systems = deepcopy(systems)

    def import_graph_cost(self, graph):
        self.graph_cost = deepcopy(graph)

    def import_graph_link(self, graph):
        self.graph_link = deepcopy(graph)


        
            

   

    
    

    