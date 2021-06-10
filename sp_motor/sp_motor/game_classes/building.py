import json
from copy import deepcopy
from sp_motor.game_classes.unit import unit
from sp_motor.utils import load_conf_f

#JSON SCALING
#[0] = PV
#[1] = MAINT_COST
#[2] = PRODUCTION

class building:
    lastId = 1

    def __init__(self, typeB, location,owner):
        self.id = building.lastId
        building.lastId += 1
        self.typeB = typeB
        self.location = location
        self.level_tier = 0
        self.level_tier_max = 3
        self.level_production = 0
        self.cost = {}
        self.cost2 = {}
        self.cost3 = {}
        self.maint_cost = 0
        self.state = 0
        self.production_per_turn = 0
        self.scaling = 0
        self.owner = owner

    def aplly_conf(self):
        conf = load_conf_f("config_building")
        actual_conf = conf[self.typeB]
        self.typeB = actual_conf["type"]
        self.level_tier = actual_conf["level_tier"]
        self.level_production = actual_conf["level_production"]
        self.cost = actual_conf["cost"]
        self.maint_cost = actual_conf["maint_cost"]
        self.state = actual_conf["state"]
        self.production_per_turn = actual_conf["production"]
        self.scaling = actual_conf["scaling"]

    def upgrade_tier(self):
        self.maint_cost = round(self.maint_cost * self.scaling[1])
        self.production_per_turn = round(self.production_per_turn * self.scaling[2])
        self.level_tier += 1

    def upgrade_prod(self):
        if self.level_production < self.level_tier_max:
            self.production_per_turn = round(self.production_per_turn * self.scaling[2])
            self.level_production = self.level_production+1


    def link_ress(self):
        if self.typeB == "habitation":
            return "or"
        elif self.typeB == "mine":
            return "minerai"
        elif self.typeB == "raffinerie":
            return "lingot"
        elif self.typeB == "usine":
            return "electronique"
        elif self.typeB == "ferme":
            return "nourriture"

            

    def produce(self):
       ress=self.link_ress()
       return {
           "ress":ress,
           "qt":self.production_per_turn,
       }

    def to_front(self):
        dic = {
            "id": self.id,
            "id_system": self.location,
            "build_t": self.typeB,
            "cost": self.cost[self.level_tier-1],
            "maint_cost": self.maint_cost,
            "owner": self.owner,
            "tier": self.level_tier,
            "state": self.state,
            "prod_turn": self.production_per_turn,

        }
        return dic


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

    def ressources_needed(self):
        return self.cost[self.level_tier]





