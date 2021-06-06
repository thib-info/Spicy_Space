from random import uniform, randint
import numpy as np

from sp_motor.utils import dist

class System():
    def __init__(self, x, y):
        self.pos = (x, y)
        self.graph = None


class Spawn_zonne(System):
    def __init__(self, x, y, radius):
        self.radius = radius
        self.children = []

        System.__init__(self, x, y)

    def make_spawn(self, min_radius, max_radius):
        unplaced = True
        i = 0
        while unplaced and i < 2000:
            x = randint(self.pos[0] - self.radius + min_radius, self.pos[0] + self.radius - min_radius)
            y = randint(self.pos[1] - self.radius + min_radius, self.pos[1] + self.radius - min_radius)

            minimal_radius = max_radius
            for child in self.children:
                curr_rad = dist(child.pos, (x, y)) - child.radius
                minimal_radius = min(minimal_radius, curr_rad)

            if minimal_radius >= min_radius:
                radius = uniform(min_radius, min(minimal_radius, max_radius))
                
                self.children.append(Spawn_zonne(x, y, int(radius)))
            unplaced = False
            i += 1

    def adja_mat(self):
        adja = np.array([[i for i in range(len(self.children))] for i in range(len(self.children))])
        for i in range(adja.shape[0]):
            for j in range(adja.shape[1]):
                adja[i, j] = dist(self.children[i].pos, self.children[j].pos)

        return adja

    def get_points(self):
        points = []
        for child in self.children:
            points.append([child.pos[0], child.pos[1]])

        return np.array(points)

    def get_child(self, pos):
        for i in range(len(self.children)):
            if self.children[i].pos == pos:
                return i

        return None

    def fill_child_neig(self, array_like):
        for i in range(len(self.children)):
            self.children[i] = array_like[i]

    

    


    def print_spawn(self):
        print(f"father   ({self.pos[0]}, {self.pos[1]}), radius  : {self.radius}")
        for child in self.children:
            print(f"child   ({child.pos[0]}, {child.pos[1]}), radius  : {child.radius}")





