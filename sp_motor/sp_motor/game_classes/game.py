import json
import pickle

from sp_motor.game_classes.player import player 
from sp_motor.game_classes.unit import unit 
from sp_motor.game_classes.building import building as build
from sp_motor.utils import load_conf_f
from copy import deepcopy

PLAYER1_NAME = "Toto"

class game():
    def __init__(self):
        self.players = []
        self.systems =[] #conf["map"]
        self.turn =[] #conf["turn"]
        self.units = []
        self.buildings = []
        self.map = None
        self.models = {}
        self.players_interactions=[]
        self.map = None

    def create_player(self,isMJ=False):
        self.players.append(deepcopy(self.models["player"]))
        self.players[-1].set_param(len(self.players)-1, PLAYER1_NAME,isMJ)

    def get_player(self,pid):
        for i in range(len(self.players)):
            if self.players[i].pid==pid:
                return i
        return -1

    def get_unit(self,id):
        for i in range(len(self.unit)):
            if self.unit[i].id==id:
                return i
        return -1

    def get_systems(self,id):
        for i in range(len(self.map.systems)):
            if self.map.systems[i].id == id:
                return i
        return -1

    def get_buildings(self,id):
        for i in range(len(self.building)):
            if self.buildings.id == id:
                return i
        return -1

    def get_players_interactions(self,id):
        for i in self.players_interractions:
            if i.id==self.pid:
                return i

    def next_turn(self):
        self.turn += 1

    def load_conf(self):
        conf_player = load_conf_f("config_player")
        self.models["player"] = player(conf_player["player"], -1, "NULL")

        conf_unit = load_conf_f("config_unit")
        for key,model in conf_unit.items():
            self.models[key] = unit(model, -1, -1)

        conf_ress = load_conf_f("ressources")
        self.models["ressources"] = {}
        for c, v in conf_unit.items():
            self.models["ressources"][c] = v["value"]

    def delete_unit(self,id_unit):
        self.units.pop(id_unit)

    def create_unit(self, owner_id, position, created_unit, base_lvl=1,):
        self.units.append(deepcopy(self.models[created_unit]))
        self.units[-1].set_param(owner_id, position, base_lvl)
        self.players[owner_id].units_id.append(self.units[-1].id)


    ################## syst de production des ressources #########


    def update_player_ressources(self):
        for player in self.players:

            pl_sys_index = [self.get_systems(id) for id in player.systems_id]
            #partie ajout des productions pour chaques joueurs
            for c in player.ressources:
                player.ressources[c]["qt_t"] = 0


            for sys_id in pl_sys_index:
                local_buildings = [deepcopy(self.buildings[self.get_buildings(id)]) for id in self.systems[sys_id].buildings_id]
                sys_prod = self.systems[sys_id].produce(self.models["ressources"], local_buildings)
                player.update_prod(sys_prod)

            #fin de la partie sur la production

            #partie prend en compte les couts de fonctionnement





   # def discover(self,unit_id):                   #A SUPPR
    #    pos = self.units[unit_id].position
     #   ow = self.units[unit_id].owner
      #  self.players[ow].known_systems += [2] #ajouter les voisins ici

   # def move_unit(self, unit_id, destination):
    #    self.units[unit_id].position = destination
     #   self.discover(unit_id)

    #################
    #syst interactions

    #vient modifier le timer de paix d'un systeme
    def is_syst_in_war(self, sys_id):
        s_id = self.get_systems(sys_id)
        ow_id = self.systems[s_id].owner_id
        sys = deepcopy(self.systems[s_id])

        present_players = []
        for u_id in sys.units_id:
            present_players.append(self.units[self.get_unit(u_id)].owner)

        present_players = list(set(present_players))
        present_players.pop(present_players.index(ow_id))

        for p_id in present_players:
            if p_id in self.players[self.get_player(ow_id)].enemies_id:
                sys.to_peace = 4
        
        self.systems[s_id] = deepcopy(sys)
                
    #################

    #vient tester si un joueur possède un systeme
    def is_proprio(self, p_id, sys_id):
        return p_id == self.systems[self.get_systems(sys_id)].owner_id
    
    

######################################""
def save_game(game, path):
    with open(path, 'wb') as f:
        pickle.dump(game, f)

def load_game(path):
    with open(path, 'rb') as f:
        output = pickle.load(f)
    return output


