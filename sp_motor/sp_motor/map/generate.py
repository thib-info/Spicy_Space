from random import uniform, randint
from sp_motor.utils import dist


class Spawn_zonne():
    def __init__(self, x, y, radius):
        self.pos = (x, y)
        self.radius = radius
        self.children = []

    def make_spawn(self, min_radius, max_radius):
        unplaced = True
        i = 0
        while unplaced and i < 2000:
            x = randint(self.pos[0] - self.radius + min_radius, self.pos[0] + self.radius - min_radius)
            y = randint(self.pos[1] - self.radius + min_radius, self.pos[1] + self.radius + min_radius)

            minimal_radius = max_radius
            for child in self.children:
                curr_rad = dist(child.pos, (x, y)) - child.radius
                minimal_radius = min(minimal_radius, curr_rad)

            if minimal_radius >= min_radius:
                print(min(minimal_radius, max_radius))
                radius = uniform(min_radius, min(minimal_radius, max_radius))
                
            self.children.append(Spawn_zonne(x, y, radius))

            unplaced = False
            i += 1


    def print_spawn(self):
        print(f"father   ({self.pos[0]}, {self.pos[1]}), radius  : {self.radius}")
        for child in self.children:
            print(f"child   ({child.pos[0]}, {child.pos[1]}), radius  : {child.radius}")


        