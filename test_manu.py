from sp_motor.game_classes.game import game, save_game, load_game
from sp_motor.game_classes.player import player 
from sp_motor.game_classes.unit import unit 
from sp_motor.game_classes.building import building as build
from sp_motor.utils import load_conf_f
from copy import deepcopy



g1 = game()
g1.load_conf()
g1.create_player()
g1.create_player(True)



print(g1.players[0].name)
print(g1.players[1].pid)

conf_unit = load_conf_f("config_unit")


destroyer = unit(conf_unit["destroyer"], -1, [-1, -1])
u1=deepcopy(destroyer)
g1.units.append(u1)
g1.units.append(u1)
print(g1.units[0].name)


save_game(g1, "game_save")
g2 = game()
g2 = load_game("game_save")
print(g2.players[0].name)
print(g2.players[1].pid)
print(g2.units[0].name)