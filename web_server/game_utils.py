import json


from sp_motor.game_classes.game import game
from sp_motor.game_classes.map import Map, System_p
from sp_motor.map.create import create_map
from sp_motor.game_classes.player import player


def big_map():
    return create_map(radius=350,nb_zonnes=(70, 90), zonnes_r=(45, 70), systems=(8, 15), inner_conf=(10, 15) )

def medium_map():
    return create_map(radius=250,nb_zonnes=(15, 20), zonnes_r=(30, 50), systems=(6, 12), inner_conf=(7, 12) )



def create_game():

    g = game()
    g.load_conf()
    test = True
    while test:
        try:
            g.import_map(big_map())
            test = False
        except :
            pass
            
    return g


def join_game(g, player_id, player_name, p_quality=False):
    result = g.create_player(player_id, player_name, p_quality)

    return result


def test_joining():
    join_game(super_game, 10, 'coco')
    join_game(super_game, 10, 'robert')
    join_game(super_game, 11, 'robert')
    join_game(super_game, 15, 'merde')