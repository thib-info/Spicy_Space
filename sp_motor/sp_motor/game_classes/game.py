import json
from sp_motor.sp_motor.game_classes.player import player as pl
from sp_motor.sp_motor.game_classes.unit import unit as un
from sp_motor.sp_motor.game_classes.building import building as build
from copy import deepcopy

with open("../../../config/config_player.json") as f:
    conf_player = json.load(f)
player_model = pl(conf_player["player"], -1, "NULL")

PLAYER1_NAME = "Toto"


class game:
    def __init__(self):
        self.players = []
        self.list_systems =[] #conf["map"]
        self.turn =[] #conf["turn"]
        self.units = []



    def create_player(self):
        self.players.append(deepcopy(player_model))
        self.players[-1].set_param(len(self.players)-1, PLAYER1_NAME)
    def next_turn(self):
        self.turn += 1

g1 = game()
g1.create_player()
print(g1.players[0].pid)

