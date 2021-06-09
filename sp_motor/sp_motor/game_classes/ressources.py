import json
from sp_motor.utils import load_conf_f

class ressource:
    def __init__(self, typeR):
        self.value = 0
        self.typeR = typeR

    def apply_conf(self):
        config = load_conf_f("ressources")
        actual_conf = config[self.typeR]
        self.value = actual_conf["value"]
        self.type = actual_conf["type"]

    def add(self, amount):
        self.value += amount

    def withdraw(self, amount):
        self.value -= amount
    def get_ress(self):
        return self.value

    def pop_growth(self, conf):
        nour = ressource(conf["nourriture"])
        pop = ressource(conf["population"])
        if nour.value>pop.value*100:
            pop.add(1)
            print("pop growth")
            return pop.value
        elif nour.value<pop.value*50:
            pop.withdraw(1)
            if pop <= 0:
                pop.add(1)
            print("pop decline")
            return pop.value
        print("no pop change")
        return pop.value

    def total_ressources(self):
        conf = load_conf_f("ressources")
        res = []
        for i in conf:
            buff = ressource(i)
            buff.apply_conf()
            res.append(buff)
        return res

    def order_ressources(self,conf):
        res = []
        for i in conf:
            buff = ressource(i)
            buff.apply_conf()
            res.append(buff.type)
        return res

    def to_front(self):
        dic = {
        "typeR":self.typeR,
        "value":self.value,
        }
        return dic


# with open("config/ressources.json") as f:
#     config = json.load(f)

# print(config["population"].keys())
# test = ressource("or")
# test.apply_conf()
# print(test.value)
# print(test.type)
# test.add(100)
# print(test.value)
# test.withdraw(300)
# print(test.value)
# test.pop_growth(config)
# print(test.total_ressources())
# print(test.order_ressources(config))
