import math
import numpy as np
import json
from copy import deepcopy

def dist(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def calculate_cost(graph):
    temp_graph = deepcopy(graph)
    mini_val, max_val = graph.min(), graph.max()
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph[i, j] >0:
                temp_graph[i, j] = int(1+ (graph[i, j] - mini_val)/(max_val - mini_val) * 6  )
            # print(temp_graph[i, j], "    ", graph[i, j])

    return graph


def load_conf_f(conf_file):
    with open(f"config/{conf_file}.json") as f:
        config = json.load(f)

    return config

