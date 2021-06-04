import json

class technology:
    def __init__(self, conf, bat):
        self.type = conf["type"]
        self.name = conf[bat]["name"]
        self.upgrade = conf[bat]["next_upgrade"]
        self.unlocked = conf[bat]["researched"]

    def __getitem__(self, item):
        return getattr(self, item)

    def upgradable(self):
        if self.upgrade:
            return True
        return False

    def upgrade_possible(self):
        return self.upgrade

    def research(self):
        self.unlocked = True
        return self.unlocked

    def researched(self):
        return self.unlocked

    def tech_researched(self, conf):
        res = []
        for i in conf:
            if i != "type":
                buff = technology(conf, i)
                if buff.researched():
                    res.append(buff["name"])
        if self.researched():
            res.append(self.name)
        return res

    def tech_researchable(self, conf):
        res = []
        for i in self.tech_researched(conf):
            if i != "type":
                buff = technology(conf, i)
                for j in buff["upgrade"]:
                    if j not in self.tech_researched(conf):
                        res.append(j)
        return res

    def upgrage_request(self,name):
        if name in self.upgrade_possible():
            return True
        return False

with open("../../../config/base_tech.json") as f:
    config = json.load(f)

print(config["batiment"]["ferme"].keys())
test = technology(config["batiment"], "spatioport")
print("researched")
print(test.researched())
print("upgrade")
print(test.research())
print("upgradable")
print(test.upgradable())
print("upgrade possible")
print(test.upgrade_possible())
print("tech_researched")
result = test.tech_researched(config["batiment"])
print(result)
print("tech_researchable")
result2 = test.tech_researchable(config["batiment"])
print(result2)