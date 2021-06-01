import json

class unite:
    def __init__(self, conf, owner, position, base_lvl=1):
        self.name = conf["name"]
        self.type = conf["type"]
        self.owner = owner
        self.position = position
        self.tier = base_lvl
        self.scaling= conf["scaling"]
        #Scaling : [pv,pa,speed,cost,maint_cost]
        self.pv = conf["pv"] + (self.tier-1)*self.scaling[0]*conf["pv"]
        self.pa = conf["pa"] + (self.tier-1)*conf["scaling"][1]*conf["pa"]
        self.speed = conf["speed"] + (self.tier-1)*conf["scaling"][2]*conf["speed"]
        self.cost = conf["cost"] + (self.tier-1)*conf["scaling"][3]*conf["cost"]
        self.maint_cost = conf["maint_cost"] + (self.tier-1)*conf["scaling"][4]*conf["maint_cost"]

    def upgrade(self,conf):
        self.pv = self.pv + self.scaling[0] * conf["pv"]
        self.pa = self.pa + self.scaling[1] * conf["pa"]
        self.speed = self.speed + self.scaling[2] * conf["speed"]
        self.cost = self.cost + self.scaling[3] * conf["cost"]
        self.maint_cost = self.maint_cost + self.scaling[4] * conf["maint_cost"]

with open("conf_files/class_attributes/spaceships.json") as f:
    conf = json.load(f)

#print(conf["destroyer"].keys())
#test = unite(conf["destroyer"], 1, [1, 1])
#test.upgrade(conf["destroyer"])
#test.upgrade(conf["destroyer"])
#print(test.pv)
#print(test.maint_cost)

