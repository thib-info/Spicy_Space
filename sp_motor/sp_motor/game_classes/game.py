import json

from sp_motor.game_classes.player import player as pl
from sp_motor.game_classes.unit import unit as un
from sp_motor.game_classes.building import building as build
from copy import deepcopy



PLAYER1_NAME = "Toto"

class game():
    def __init__(self):
        self.players = []
        self.list_systems =[] #conf["map"]
        self.turn =[] #conf["turn"]
        self.units = []
        self.models = {}



    def create_player(self,isMJ=False):
        self.players.append(deepcopy(self.models["player"]))
        self.players[-1].set_param(len(self.players)-1, PLAYER1_NAME,isMJ)
    def next_turn(self):
        self.turn += 1

    def load_conf(self):
        with open("config/config_player.json") as f:
            conf_player = json.load(f)
        self.models["player"] = player(conf_player["player"], -1, "NULL")

        with open("config/config_unit.json") as f:
            conf_unit = json.load(f)
        for key,model in conf_unit.items():
            self.models[key] = unit(model,-1,-1)

    def delete_unit(self,id_unit):
        self.units.pop(id_unit)


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