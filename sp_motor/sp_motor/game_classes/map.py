import numpy as np
from copy import deepcopy
import json
from random import randint
# from copy import deepcopy
from sp_motor.game_classes.building import building

from sp_motor.utils import calculate_cost
import sp_motor.game_classes.game



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

    def export_min_info(self):
        return {
            "name":self.name,
            "pos":self.pos,
        }
    


class System_p(Basic_info):
    lastId = 0
    def __init__(self, name, pos):
        self.sector_id = 0
        self.id = System_p.lastId
        System_p.lastId += 1
        self.owner_id = -1

        self.units_id = []
        self.max_building=randint(5,10)
        self.buildings=[]
        self.population=0
        self.bonus=randint(0,4)
        Basic_info.__init__(self, name, pos)

    def set_sector(self, sector_id):
        self.sector_id = sector_id
    
    def get_sector_id(self):
        return self.sector_id

    def export_system_info(self):
        pass

    def add_building(self,building_id):
        if len(self.buildings) < self.max_building:
            self.buildings.append(building_id)
            return True
        else:
            return False

    def add_population(self,n):
        self.population=self.population+n

    def change_owner(self,owner):
        self.owner_id = owner

    def print_buildings(self):
        print("\nliste des différents batiments du systeme :")
        for i in self.buildings:
            print("type: "+str(i.typeB)+" propriétaire: "+str(i.owner))

    def print_buildings_stat(self,building_id):
        print("\nSTATISTIQUES DU BATIMENT ID: "+str(building_id))
        b=self.buildings[building_id]
        print("level_tier: "+str(b.level_tier))
        print("level_production: " + str(b.level_production))
        print("maint_cost: " + str(b.maint_cost))
        print("state: " + str(b.state))
        print("production_per_turn: " + str(b.production_per_turn))



    

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
        self.size = 2*pos[0]

        Basic_info.__init__(self, name, pos)

    
    def import_sectors(self, sectors):
        self.sectors = deepcopy(sectors)


    def import_systems(self, systems):
        self.systems = deepcopy(systems)

    def import_graph_cost(self, graph):
        self.graph_cost = calculate_cost(graph)
        # self.graph_cost = graph


        self.graph_cost = deepcopy(graph)

    def import_graph_link(self, graph):
        self.graph_link = deepcopy(graph)

    def export_info(self):
        output = {
            "systems":[],
            "sectors":[],
            "links":[],
        }

        for sector in self.sectors:
            output["sectors"].append(sector.export_min_info())

        for system in self.systems:
            output["systems"].append(system.export_min_info())

        for i in range(self.graph_link.shape[0]):
            for j in range(self.graph_link.shape[1]):
                if self.graph_link[i, j] == 1:
                    output["links"].append({
                        "start":self.systems[i].get_pos(),
                        "end":self.systems[j].get_pos()
                    })


        output["map_size"] = self.size

        return output


        
            

   

    
    

    