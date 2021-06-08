import math
import json

def dist(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)



def calculate_cost(dist):
    return int(dist)


def load_conf_f(conf_file):
    with open(f"config/{conf_file}.json") as f:
        config = json.load(f)

    return config