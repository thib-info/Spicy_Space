from sp_motor.utils import load_conf_f
from sp_motor.game_classes.player import player


class technology:
    def __init__(self, conf, bat):
        buff = self.parcours(conf, bat)
        self.name = buff["name"]
        self.cost = buff["cost"]
        self.unlocked = buff["researched"]
        self.upgrade = buff["children"]

    def parcours(self, conf, bat, find=0):
        global buffer
        if find == 0:
            for v in conf.items():
                if isinstance(v, dict):
                    if v["name"] == bat:
                        buffer = v
                        find = 1
                        return buffer
                    else:
                        self.parcours(v["children"], bat, find)
        return buffer

    def __getitem__(self, item):
        return getattr(self, item)

    def upgradable(self):
        if self.upgrade:
            return True
        return False

    def upgrade_possible(self):
        return self.upgrade

    def research(self):
        buff = player.ressources[6]
        if buff >= self.cost:
            player.ressources[6].withdraw(self.cost)
            self.unlocked = True
        return self.unlocked

    def researched(self):
        return self.unlocked

    def tech_researched(self, conf):
        res = []
        for i in conf:
            buff = technology(conf, i)
            if buff.researched():
                res.append(buff["name"])
        if self.researched():
            res.append(self.name)
        return res

    def tech_researchable(self, conf):
        res = []
        for i in self.tech_researched(conf):
            buff = technology(conf, i)
            for j in buff["upgrade"]:
                if j not in self.tech_researched(conf):
                    res.append(j)
        return res

    def upgrage_request(self, name):
        if name in self.upgrade_possible():
            return True
        return False


config = load_conf_f("base_tech")
buffer = []
# print(config["mine"].keys())
test = technology(config, "usine niveau 2")
# print("researched")
# print(test.researched())
# print("upgrade")
# print(test.research())
# print("upgradable")
# print(test.upgradable())
# print("upgrade possible")
# print(test.upgrade_possible())
# print("tech_researched")
# result = test.tech_researched(config)
# print(result)
# print("tech_researchable")
# result2 = test.tech_researchable(config)
# print(result2)
