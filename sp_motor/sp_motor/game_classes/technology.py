from sp_motor.utils import load_conf_f
from sp_motor.game_classes.player import player

def parcours(conf, bat):
    for c, v in conf.items():
        if c == bat:
            return v
        else:
            for child in v["children"]:
                buffer = parcours(child, bat)
                if buffer != None:
                    return buffer
    return None

def path(conf, bat):
    buff = []
    for c, v in conf.items():
        if c == bat:
            return buff
        else:
            for child in v["children"]:
                buff.append(v)
                buffer = parcours(child, bat)
                if buffer != None:
                    return buff
    return buff

class technology:
    def __init__(self, conf, bat):
        buff = parcours(conf, bat)
        self.name = buff["name"]
        self.cost = buff["cost"]
        self.unlocked = buff["researched"]
        self.upgrade = buff["children"]



    def __getitem__(self, item):
        return getattr(self, item)

    def upgradable(self):
        if self.upgrade:
            return True
        return False

    def upgrade_possible(self):
        buffer = []
        for i in self.upgrade[0]:
            buffer.append(i)
        return buffer

    def research(self):
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
            for j in buff["upgrade"][0]:
                if j not in self.tech_researched(conf):
                    res.append(j)
        return res

    def upgrage_request(self, name):
        if name in self.upgrade_possible():
            return True
        return False

    def yol(self, conf, bat):
        path(conf, bat)
