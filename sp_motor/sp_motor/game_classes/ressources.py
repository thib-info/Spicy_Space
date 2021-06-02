import json

class ressource:
    def __init__(self, conf):
        self.value = conf["value"]
        self.type = conf["type"]

    def add(self, amount):
        self.value += amount

    def withdraw(self, amount):
        self.value -= amount



with open("../../../config/ressources.json") as f:
    conf = json.load(f)

print(conf["population"].keys())
test = ressource(conf["population"])
print(test.value)
print(test.type)
test.add(5)
print(test.value)
test.withdraw(10)
print(test.value)
