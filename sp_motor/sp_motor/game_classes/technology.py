import json

class technology:
    def __init__(self, conf,bat):
        self.type = conf["type"]
        self.name = conf[bat]["name"]
        self.upgrade = conf[bat]["next_upgrade"]
        self.unlocked = conf[bat]["researched"]

    

    def upgradable(self):
        print(self.upgrade)
        if self.upgrade != []:
            return True
        return False

    def research(self):
        print(self.unlocked)
        self.unlocked = True
        print(self.unlocked)

    def researched(self,bat):
        res = []
        for i in range(1,len(bat)):
            print(bat["type"])
            #if bat["researched"] == "True":
             #   res.append(bat["name"])
        return res




with open("../../../config/base_tech.json") as f:
    conf = json.load(f)

print(conf["batiment"].keys())
test = technology(conf["batiment"],"usine tier 3")
print("upgrade")
test.research()
print("upgradable")
print(test.upgradable())
res = []
res = test.researched(conf["batiment"])
print(res)