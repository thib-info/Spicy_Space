import math
import numpy as np

def dist(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)



def calculate_cost(graph):
    mini_val, max_val = graph.min(), graph.max()
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            graph[i, j] = int(1+ (graph[i, j] - mini_val)/(max_val - mini_val) * 6  )

    return graph