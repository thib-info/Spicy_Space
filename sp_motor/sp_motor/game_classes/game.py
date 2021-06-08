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
        self.list_systems =[] #conf["map"]
        self.turn =[] #conf["turn"]
        self.units = []
        self.models = {}
        self.Players_intteractions=[]

    def create_player(self,isMJ=False):
        self.players.append(deepcopy(self.models["player"]))
        self.players[-1].set_param(len(self.players)-1, PLAYER1_NAME,isMJ)

    def get_player(self,pid):
        for i in self.players:
            if i.pid==pid:
                return i

    def get_unit(self,id):
        for i in unit:
            if i.id==id:
                return i

    def get_systems(self,id):
        for i in self.list_systems:
            if i.id==self.pid:
                return i

    def get_PLayers_intteractions(self,id):
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

    def delete_unit(self,id_unit):
        self.units.pop(id_unit)

    def create_unit(self, owner_id, position, created_unit, base_lvl=1,):
        self.units.append(deepcopy(self.models[created_unit]))
        self.units[-1].set_param(owner_id, position, base_lvl)
        self.players[owner_id].units_id.append(self.units[-1].id)

    def move_unit(self, unit_id, destination):
        self.units[unit_id].position = destination


######################################""
def save_game(game, path):
    with open(path, 'wb') as f:
        pickle.dump(game, f)

def load_game(path):
    with open(path, 'rb') as f:
        output = pickle.load(f)
    return output



# g1 = game()
# g1.load_conf()
# g1.create_player()
# g1.create_player(True)
# print(g1.players[0])
# print(g1.players[1])
# #print(g1.players[0].name)
# #print(g1.players[1].pid)

# with open("../../../config/config_unit.json") as g:
#     conf_unit = json.load(g)


# destroyer = unit(conf_unit["destroyer"], -1, [-1, -1])
# u1=deepcopy(destroyer)
# g1.units.append(u1)
# g1.units.append(u1)
# print(g1.units)
# g1.delete_unit(0)
# print(g1.units)