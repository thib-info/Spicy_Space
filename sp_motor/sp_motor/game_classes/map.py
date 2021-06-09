import numpy as np
from copy import deepcopy
import json
from random import randint
# from copy import deepcopy
from sp_motor.game_classes.building import building

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

        self.to_peace = 0

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

    def add_building(self,id):
        self.buildings_id.append(id)

    def change_owner(self,owner):
        self.owner_id = owner

    def is_owned(self, pid):
        return self.owner_id == pid
        

    def adjust_pop(self, production):
        if self.to_peace < 1:
            test = True
            for c, v in production.items():
                test = test and v >= self.population

        return test

    ############## gestion des buildings ############
    def can_add_building(self):
        if len(self.buildings_id) < self.max_building:
                return True
        else:
            return False

    def update_buildings_owner(self, p_id):
        for building in self.buildings:
            building.owner = p_id


    def produce(self, model, building):
        local_production = {}
        for c, v in model.items():
            local_production[c] = 0
        
        for building in buildings:
            if building.state:
                build_prod = building.produce()
                local_production[build_prod["ress"]] += self.bonus * build_prod["qt"]


        test_croissance = adjust_pop(local_production)
        if test_croissance:
            local_production["population"] = 1

        return local_production

    ########### fin de gestion des buildings #############

    

class Sectors(Basic_info):
    lastId = 0
    def __init__(self, name, pos):
        self.members = []
        self.id = Sectors.lastId
        Sectors.lastId += 1
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


    def get_system(self, id):
        for i in range(len(self.systems)):
            if self.systems[i].id == id:
                return i
        return -1

    def get_sector(self, id):
        for i in range(len(self.sectors)):
            if self.sectors[i].id == id:
                return i
        return -1

    def get_empty_sectors(self):
        output = []
        for sector in self.sectors:
            test = True
            for sys_id in sector.members:
                if len(self.systems[self.get_system(sys_id)].units_id) != 0:
                    test = False
            if test:
                output.append(sector.id)
        return output


    def get_systems_from_owner(self, owner):
        output = []
        for sys in self.systems:
            if sys.owner_id == owner:
                output.append(sys.id)

        return output

    def send_access_graph(self, ok_sys, no_sys):
        graph = np.array([[0 for i in range(self.graph_cost.shape[0])] for i in range(self.graph_cost.shape[1])])
        for i in range(self.graph_cost.shape[0]):
            if i in ok_sys:
                for j in range(self.graph_cost.shape[1]):
                    if j in ok_sys and i not in no_sys:
                        graph[i, j] = graph_cost[i, j]

        for z in range(3):
            temp_graph = np.array([[0 for i in range(self.graph_cost.shape[0])] for i in range(self.graph_cost.shape[1])])
            for i in range(graph.shape[0]):
                for j in range(graph.shape[1]):
                    temp_graph[i, j] = graph[i, j]
                    for x in range(graph.shape[0]):
                        for y in range(graph.shape[1]):
                            temp_graph[i, j] = min(temp_graph[i, j], graph[x, y])

            graph = deepcopy(temp_graph)


        return graph

            


    
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






        



   

    
    

    