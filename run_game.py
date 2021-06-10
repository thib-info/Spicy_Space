import json


from sp_motor.game_classes.game import game
from sp_motor.game_classes.map import Map, System_p
from sp_motor.map.create import create_map
from sp_motor.game_classes.player import player


def big_map():
    return create_map(radius=350,nb_zonnes=(70, 90), zonnes_r=(45, 70), systems=(8, 15), inner_conf=(10, 15) )

def medium_map():
    return create_map(radius=250,nb_zonnes=(15, 20), zonnes_r=(30, 50), systems=(6, 12), inner_conf=(7, 12) )

def test_map():
    map = medium_map()
    # print_graph(map)


    # dico = map.export_info()
    # with open("games/medium_map.json", 'w') as f:
    #     json.dump(dico, f)


def create_game():

    g = game()
    g.load_conf()
    g.import_map(big_map())
    return g


def join_game(g, player_id, player_name, p_quality=False):
    result = g.create_player(player_id, player_name, p_quality)

    return result


super_game = create_game()
print(join_game(super_game, 10, 'coco'))
print(join_game(super_game, 10, 'robert'))
print(join_game(super_game, 11, 'robert'))
print(join_game(super_game, 15, 'merde'))
# print(len(super_game.players), "    ", len(super_game.units))
for unit in super_game.units:
    print(unit.id)
    print(unit.name)
    print(unit.position)
    print(unit.owner)
    print("")



super_game.to_next_turn()
print(super_game.can_unit_move(3, 14))
















