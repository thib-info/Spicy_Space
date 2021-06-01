import json

class unit:
    def __init__(self, conf, owner, position, base_lvl=1,battling = False):
        self.name = conf["name"]
        self.type = conf["type"]
        self.owner = owner
        self.position = position
        self.tier = base_lvl
        self.scaling= conf["scaling"]
        #Scaling : [pv_max,pa,speed,cost,maint_cost]
        self.pv_max = conf["pv_max"] + (self.tier-1)*self.scaling[0]*conf["pv_max"]
        self.pa = conf["pa"] + (self.tier-1)*conf["scaling"][1]*conf["pa"]
        self.speed = conf["speed"] + (self.tier-1)*conf["scaling"][2]*conf["speed"]
        self.cost = conf["cost"] + (self.tier-1)*conf["scaling"][3]*conf["cost"]
        self.maint_cost = conf["maint_cost"] + (self.tier-1)*conf["scaling"][4]*conf["maint_cost"]
        self.pv = self.pv_max
        self.battling = battling

    def upgrade(self,conf):
        self.pv_max = self.pv_max + self.scaling[0] * conf["pv_max"]
        self.pa = self.pa + self.scaling[1] * conf["pa"]
        self.speed = self.speed + self.scaling[2] * conf["speed"]
        self.cost = self.cost + self.scaling[3] * conf["cost"]
        self.maint_cost = self.maint_cost + self.scaling[4] * conf["maint_cost"]
        self.pv = self.pv_max

    def take_damage(self, damage_taken):
        self.pv = self.pv - damage_taken

    def heal_damage(self, damage_healed):
        if not self.battling:
            self.pv = self.pv + damage_healed
            if self.pv > self.pv_max:
                self.pv = self.pv_max
    def battle(self):
        self.battling = True
    def end_battle(self):
        self.battling= False


with open("../../../config/config_unit.json") as f:
    conf = json.load(f)

print(conf["destroyer"].keys())
test = unit(conf["destroyer"], 1, [1, 1])
test.upgrade(conf["destroyer"])
test.upgrade(conf["destroyer"])
print(test.pv)
print(test.pv_max)
test.battle()
test.take_damage(12)
test.heal_damage(34)

print(test.pv)
print(test.pv_max)
print(test.maint_cost)

