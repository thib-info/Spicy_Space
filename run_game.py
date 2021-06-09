# from sp_motor.game_classes.map import Map
# from sp_motor.map.create import create_map
import json
from sp_motor.game_classes.map import Map
from sp_motor.map.create import print_graph, create_map
import sp_motor.game_classes

# import json

# map = create_map(radius=300)

# dico = map.export_info()

# print(dico)



def test_map():

    def big_map():
        return create_map(radius=350,nb_zonnes=(70, 90), zonnes_r=(45, 70), systems=(8, 15), inner_conf=(10, 15) )

    def medium_map():
        return create_map(radius=250,nb_zonnes=(15, 20), zonnes_r=(30, 50), systems=(6, 12), inner_conf=(7, 12) )


    map = medium_map()
    # print_graph(map)


    # dico = map.export_info()
    # with open("games/medium_map.json", 'w') as f:
    #     json.dump(dico, f)


test_map()