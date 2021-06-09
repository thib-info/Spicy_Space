from sp_motor.game_classes.game import game, save_game, load_game
from sp_motor.game_classes.player import player
from sp_motor.game_classes.unit import unit
from sp_motor.game_classes.building import building as build
from sp_motor.utils import load_conf_f
from copy import deepcopy
from sp_motor.players_interactions.battles import battle,can_battle
from sp_motor.map.create import create_map
from sp_motor.game_classes.map import Map, System_p


g1 = game()
g1.load_conf()
g1.create_player(True)
g1.map = create_map(radius=350,nb_zonnes=(70, 90), zonnes_r=(45, 70), systems=(8, 15), inner_conf=(10, 15) )
g1.create_building("ferme", 1, 1)

print(g1.buildings[0])