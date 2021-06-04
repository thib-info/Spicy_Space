from sp_motor.sp_motor.game_classes.unit import unit as un
import random
import json

def hit(attack,defense):
    if random.randint(1,100) >= defense.evasion:
        return True
    else:
        return False

def battle(pUnit1,tar1,tar2=None,tar3=None):
        pUnit1.battling=True
        tar1.battling=True
        if hit(pUnit1,tar1):
            tar1.pv = tar1.pv - pUnit1.pa
            print(f"Tir reussi vous avez inflige  {pUnit1.pa} degats")

            if pUnit1.pa > tar1.pv:
                if tar2 != None :
                    tar2.battling=True
                    if pUnit1.pa >(tar1.pv + tar2.pv):
                        if tar3 != None:
                            tar3.battling=True


with open("../../../config/config_unit.json") as f:
    conf = json.load(f)

id1 = un(conf["destroyer"], 1, [1, 1])
id2 = un(conf["destroyer"], 2, [2, 2])
hit(id1,id2)
print(id1.battling)

battle(id1,id2)
print(id1.battling)


