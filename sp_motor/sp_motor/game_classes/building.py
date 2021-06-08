import json
from copy import deepcopy
from sp_motor.game_classes.ressources import ressource
from sp_motor.game_classes.unit import unit
#JSON SCALING
#[0] = PV
#[1] = MAINT_COST
#[2] = PRODUCTION

class building:
    lastId = 1

    def __init__(self, type, location,owner):
        self.id = building.lastId
        building.lastId += 1
        self.type = type
        self.location = location
        self.level_tier = 0
        self.level_production = 0
        self.cost = 0
        self.pv = 0
        self.pv_max = 0
        self.maint_cost = 0
        self.state = 0
        self.production_per_turn = 0
        self.scaling = 0
        self.owner = owner

    def aplly_conf(self):
        with open("../../../config/config_building.json") as f:
            conf = json.load(f)

        actual_conf = conf[self.type]

        self.type = actual_conf["type"]
        self.level_tier = actual_conf["level_tier"]
        self.level_production = actual_conf["level_production"]
        self.cost = actual_conf["cost"]
        self.pv_max = actual_conf["pv"]
        self.maint_cost = actual_conf["maint_cost"]
        self.state = actual_conf["state"]
        self.production_per_turn = actual_conf["production"]
        self.scaling = actual_conf["scaling"]


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

    def produce(self):
        if self.type == "habitation": #ressources population
            self.owner.ressources[4].value=self.owner.ressources[4].value+self.production_per_turn
        elif self.type == "mine": #minerais
            self.owner.ressources[1].value = self.owner.ressources[1].value + self.production_per_turn
        elif self.type == "raffinerie":#ingot
            self.owner.ressources[2].value = self.owner.ressources[2].value + self.production_per_turn
        elif self.type == "usine":#electrotech
            self.owner.ressources[3].value = self.owner.ressources[3].value + self.production_per_turn
        elif self.type == "ferme": #nourriture
            self.owner.ressources[5].value = self.owner.ressources[5].value + self.production_per_turn

    def link_ress(self,type):
        if self.type == "habitation":
            return "or"
        elif self.type == "mine":
            return "minerai"
        elif self.type == "raffinerie":
            return "lingot"
        elif self.type == "usine":
            return "electronique"
        elif self.type == "ferme":
            return "nourriture"


    def change_owner(self,owner):
        self.owner=owner



    def produce_unit(self, name,game):
        if self.type == "spatioport":
            if name in game.models.keys():
                created = deepcopy(game.models[name])
                game.units.append(created)
                id_created = len(game.units)-1
                game.players[self.owner].units_id.append(id_created)
                game.map.systems[self.location].units_id.append(id_created)





#print(conf["mine"].keys())
# test = building("ferme",[0,0])
# test.aplly_conf()
# test2 = building("ferme",[0,0])
# test2.aplly_conf()


# print("test id")
# print("id1="+str(test.id))
# print("id2="+str(test2.id))
# print("\n")

# print("test de take_damage():")
# print("PV="+str(test.pv))
# print("-5 de damage:")
# test.take_damage(5)
# print("PV="+str(test.pv))
# print("heal +5pv :")
# test.repare(5)
# print("PV="+str(test.pv))
# print("\n")

# print("test de upgrade_tier():")
# print("PV="+str(test.pv))
# print("maint_cost="+str(test.maint_cost))
# print("production_per_turn="+str(test.production_per_turn))
# print("level="+str(test.level_tier))
# print("---upgrade_tier---")
# test.upgrade_tier()
# print("PV="+str(test.pv))
# print("maint_cost="+str(test.maint_cost))
# print("production_per_turn="+str(test.production_per_turn))
# print("level="+str(test.level_tier))

# print("\ntest upgrade_prod")
# print("production_per_turn="+str(test.production_per_turn))
# test.upgrade_prod()
# print("production_per_turn="+str(test.production_per_turn))

# print("\ntest produce")
# print(test.produce(test.link_ress(test.type))[0])
# print(test.produce(test.link_ress(test.type))[1])

