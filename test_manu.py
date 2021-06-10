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
g1.create_player()
g1.create_player(True)



#print(g1.players[0].name)
#print(g1.players[1].pid)

g1.create_unit(1, 4, "colon")
g1.create_unit(0,4,"destroyer")
#print(g1.units[1].pv)
g1.map = create_map(radius=350,nb_zonnes=(70, 90), zonnes_r=(45, 70), systems=(8, 15), inner_conf=(10, 15) )
#print(g1.get_systems(1))
battle(g1,g1.units[0], g1.units[1])
#print(g1.units[1].pv)
#print(g1.units[0].position)
#g1.move_unit(g1.units[0].id, 2)
#print(g1.units[0].position)
#battle(g1,g1.units[0], g1.units[1])
#g1.discover(1)
#print(g1.players[0].known_systems[0])

print(g1.map.systems[g1.get_systems(1)].owner_id)
print(g1.units[0].owner)



g1.colonize(0)

pos = g1.units[g1.get_unit(0)].position

print(g1.map.systems[g1.get_systems(pos)].owner_id)


#print(g1.systems[3].owner)



#print(g1.units[0].owner)


#save_game(g1, "game_save")
#g2 = game()
#g2 = load_game("game_save")
#print(g2.players[0].name)
#print(g2.players[1].pid)
#print(g2.units[0].name)