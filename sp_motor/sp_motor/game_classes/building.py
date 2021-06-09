import json
from copy import deepcopy
from sp_motor.game_classes.ressources import ressource
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
        self.level_production = 0
        self.cost = 0
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
        if self.typeB == "habitation": #ressources population
            self.owner.ressources[4].value=self.owner.ressources[4].value+self.production_per_turn
        elif self.typeB == "mine": #minerais
            self.owner.ressources[1].value = self.owner.ressources[1].value + self.production_per_turn
        elif self.typeB == "raffinerie":#ingot
            self.owner.ressources[2].value = self.owner.ressources[2].value + self.production_per_turn
        elif self.typeB == "usine":#electrotech
            self.owner.ressources[3].value = self.owner.ressources[3].value + self.production_per_turn
        elif self.typeB == "ferme": #nourriture
            self.owner.ressources[5].value = self.owner.ressources[5].value + self.production_per_turn

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
        if self.typeB == "habitation":
            return ["minerai"]
        elif self.typeB == "mine":
            return ["or"]
        elif self.typeB == "raffinerie":
            return ["or","minerai"]
        elif self.typeB == "usine":
            return ["or","lingot"]
        elif self.typeB == "ferme":
            return ["or","minerai"]




