import json

class building:
    def __init__(self, conf, location):
        self.name = conf["name"]
        self.location = location
        self.level = conf["level"]
        self.cost=conf["cost"]
        self.pv=conf["pv_max"]
        self.maint_cost=conf["maint_cost"]
        self.state=conf["state"]
        self.production_per_turn=conf["production"]

    def take_damage(self, damage):
        if self.pv>damage :
            self.pv=self.pv-damage
        else :
            self.pv=0

    def repare(self, conf, heal):
        if self.pv<conf["pv_max"]:
            self.pv=self.pv+heal
            if self.pv>conf["pv_max"]:
                self.pv=conf["pv_max"]

    def upgrade(self,conf):
        self.pv=self.pv*conf["scaling"][0]
        self.maint_cost = self.maint_cost * conf["scaling"][1]
        self.production_per_turn = self.production_per_turn * conf["scaling"][2]
        self.level=self.level+1

with open("../../../config/config_building.json") as f:
    conf = json.load(f)

print(conf["mine"].keys())
test = building(conf["mine"],[0,0])
#test take_damage()
print("test de take_damage():")
print(test.pv)
print("-5 de damage:")
test.take_damage(5);
print(test.pv)
print("heal +5pv :")
test.repare(conf,5)
print(test.pv)



