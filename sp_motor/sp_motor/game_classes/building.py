import json
#JSON SCALING
#[0] = PV
#[1] = MAINT_COST
#[2] = PRODUCTION

class building:
    lastId = 1
    def __init__(self, conf, location):
        self.id = building.lastId
        building.lastId += 1
        self.type = conf["type"]
        self.location = location
        self.level_tier = conf["level_tier"]
        self.level_production = conf["level_production"]
        self.cost=conf["cost"]
        self.pv=conf["pv"]
        self.pv_max=conf["pv"]
        self.maint_cost=conf["maint_cost"]
        self.state=conf["state"]
        self.production_per_turn=conf["production"]
        self.scaling=conf["scaling"]

    def take_damage(self, damage):
        if damage>0:
            if self.pv>damage :
                self.pv=self.pv-damage
            else :
                self.pv=0

    def repare(self, heal):
        if heal>0:
            if self.pv<self.pv_max:
                self.pv=self.pv+heal
                if self.pv>self.pv_max:
                    self.pv=self.pv_max

    def upgrade_tier(self):
        if self.level_tier<3:
            self.pv=round(self.pv*self.scaling[0])
            self.maint_cost = round(self.maint_cost * self.scaling[1])
            self.production_per_turn = round(self.production_per_turn * self.scaling[2])
            self.level_tier=self.level_tier+1
        else:
            print("\nbatiment améliorer au max\n")

    def upgrade_prod(self):
        if self.level_production<3:
            self.production_per_turn = round(self.production_per_turn * self.scaling[2])
            self.level_production=self.level_production+1

with open("../../../config/config_building.json") as f:
    conf = json.load(f)

#print(conf["mine"].keys())
test = building(conf["mine"],[0,0])
test2 = building(conf["mine"],[0,0])

print("test id")
print("id1="+str(test.id))
print("id2="+str(test2.id))
print("\n")

print("test de take_damage():")
print("PV="+str(test.pv))
print("-5 de damage:")
test.take_damage(5)
print("PV="+str(test.pv))
print("heal +5pv :")
test.repare(5)
print("PV="+str(test.pv))
print("\n")

print("test de upgrade_tier():")
print("PV="+str(test.pv))
print("maint_cost="+str(test.maint_cost))
print("production_per_turn="+str(test.production_per_turn))
print("level="+str(test.level_tier))
print("---upgrade_tier---")
test.upgrade_tier()
print("PV="+str(test.pv))
print("maint_cost="+str(test.maint_cost))
print("production_per_turn="+str(test.production_per_turn))
print("level="+str(test.level_tier))

print("\ntest upgrade_prod")
print("production_per_turn="+str(test.production_per_turn))
test.upgrade_prod()
print("production_per_turn="+str(test.production_per_turn))
