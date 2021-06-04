# from sp_motor.game_classes.map import Map
# from sp_motor.map.create import create_map

from sp_motor.game_classes.map import Map
from sp_motor.map.create import create_map

# import json

# map = create_map(radius=300)

# dico = map.export_info()

# print(dico)


import json

map = create_map(radius=300)

dico = map.export_info()

with open("game_data/map.json", 'w') as f:
    json.dump(dico, f)
