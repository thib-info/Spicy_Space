from random import randint

from sp_motor.game_classes.building import building
class systeme:
    lastId = 1
    def __init__(self,name,location,owner):
        self.id = systeme.lastId
        systeme.lastId += 1
        self.name=name
        self.location=location
        self.owner=owner
        self.buildings=[]
        self.max_building=randint(5,10)
        self.population=0
        self.bonus=randint(0,4)

    def add_building(self,type):
        tmp = building(type,self.id,self.owner)
        tmp.aplly_conf()
        self.buildings.append(tmp)

    def add_population(self,n):
        self.population=self.population+n

    def change_owner(self,owner):
        self.owner=owner

    def print_buildings(self):
        for i in self.buildings:
            print("\n")
            print("liste des différents batiments du systeme :")
            print("type: "+str(i.type)+" propriétaire: "+str(i.owner.pid))




