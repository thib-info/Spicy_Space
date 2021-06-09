import json

class unit:

    lastId = 0

    def __init__(self, conf, owner, position, base_lvl=1):
        self.id = unit.lastId
        unit.lastId += 1
        self.name = conf["name"]
        self.owner = owner
        self.precision = conf["precision"]
        self.position = position
        self.tier = base_lvl
        self.tier_max = 3
        self.scaling = conf["scaling"]
        #Scaling : [pv_max,pa,pm,cost,maint_cost]
        self.pv_max = conf["pv_max"] + (self.tier-1)*self.scaling[0]*conf["pv_max"]
        self.pa = conf["pa"] + (self.tier-1)*conf["scaling"][1]*conf["pa"]
        self.pm = conf["pm"] + (self.tier-1)*conf["scaling"][2]*conf["pm"]
        self.cost = conf["cost"]
        self.maint_cost = conf["maint_cost"] + (self.tier-1)*conf["scaling"][4]*conf["maint_cost"]
        self.pv = self.pv_max

    def set_param(self, owner, position, base_lvl=1):
        self.owner = owner
        self.position = position
        self.tier = base_lvl




    def upgrade(self,conf):
        self.pv_max = self.pv_max + self.scaling[0] * conf["pv_max"]
        self.pa = self.pa + self.scaling[1] * conf["pa"]
        self.pm = self.pm + self.scaling[2] * conf["pm"]
        self.maint_cost = self.maint_cost + self.scaling[3] * conf["maint_cost"]
        self.pv = self.pv_max
        self.tier += 1


    def take_damage(self, damage_taken):
        self.pv = self.pv - damage_taken

    def heal_damage(self, damage_healed):
            self.pv = self.pv + damage_healed
            if self.pv > self.pv_max:
                self.pv = self.pv_max

   

    def move_unit(self,destination):
        self.position = destination

    def to_front(self):
        dic = {"id":self.id,
               "id_system": self.position,
               "ship_t": self.name,
               "pv_max": self.pv_max,
               "pv": self.pv,
               "at": self.pa,
               "mp": self.pm,
               "cost": self.cost[self.tier-1],
               "maint_cost": self.maint_cost,
               "owner": self.owner,
               "tier": self.tier,
               "precision": self.precision,
               }
        return dic




# with open("../../../config/config_unit.json") as f:
#     conf = json.load(f)

# #print(conf["destroyer"].keys())
# test = unit(conf["destroyer"], 1, [1, 1])
# #test.upgrade(conf["destroyer"])
# #test.upgrade(conf["destroyer"])
# #print(test.pv)
# #print(test.pv_max)
# #test.battle()
# #test.take_damage(12)
# #test.heal_damage(34)

# #print(test.pv)
# #print(test.pv_max)
# #print(test.maint_cost)
# test.recruit("destroyer",[1, 1])

