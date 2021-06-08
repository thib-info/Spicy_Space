from sp_motor.game_classes.game import game, save_game, load_game
from sp_motor.game_classes.player import player 
from sp_motor.game_classes.unit import unit 
from sp_motor.game_classes.building import building as build
from sp_motor.utils import load_conf_f
from copy import deepcopy
from sp_motor.players_interactions.battles import battle,can_battle



g1 = game()
g1.load_conf()
g1.create_player()
g1.create_player(True)



print(g1.players[0].name)
print(g1.players[1].pid)

g1.create_unit(1, 4, "destroyer")
g1.create_unit(0,4,"tardigrade")
print(g1.units[1].pv)


battle(g1,g1.units[0], g1.units[1])
print(g1.units[1].pv)
print(g1.units[0].position)
g1.move_unit(g1.units[0].id, 2)
print(g1.units[0].position)
battle(g1,g1.units[0], g1.units[1])



print(g1.units[0].owner)


#save_game(g1, "game_save")
#g2 = game()
#g2 = load_game("game_save")
#print(g2.players[0].name)
#print(g2.players[1].pid)
#print(g2.units[0].name)