import json
from ressources import ressource
with open("../../../config/ressources.json") as g:
    conf_ress = json.load(g)
class player :
    def __init__(self, conf, pid, name, isMj = False):
        self.name = name
        self.pid = pid
        self.allies = []
        self.enemies=[]
        self.ressources = {}
        self.systems = []
        self.isMj = isMj

    def add_enemy(self,pid):
        if not pid in self.allies and not pid in self.enemies:
            self.enemies.append(pid)
    def add_ally(self,pid):
        if not pid in self.allies and not pid in self.enemies:
            self.allies.append(pid)



with open("../../../config/config_player.json") as f:
    conf = json.load(f)
test = player(conf["player"], 1,"oui")
test.add_ally(4)

print(test.allies)