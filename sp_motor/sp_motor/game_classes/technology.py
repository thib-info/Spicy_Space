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
        print(self.upgrade)
        if self.upgrade:
            return True
        return False

    def research(self):
        print(self.unlocked)
        self.unlocked = True
        print(self.unlocked)

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


with open("../../../config/base_tech.json") as f:
    config = json.load(f)

print(config["batiment"]["ferme"].keys())
test = technology(config["batiment"], "usine tier 3")
print("researched")
print(test.researched())
print("upgrade")
test.research()
print("upgradable")
print(test.upgradable())

result = test.tech_researched(config["batiment"])
print(result)

