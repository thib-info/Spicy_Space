from sp_motor.sp_motor.game_classes.unit import unit as un
from sp_motor.sp_motor.game_classes.player import player as pl
from sp_motor.sp_motor.game_classes.game import game
from sp_motor.sp_motor.game_classes.map import System_p


import random
import json
from copy import deepcopy



def hit(defense):
    if random.randint(1, 100) <= defense.precision:
        return True
    else:
        return False

def battle(pUnit1,target):
        pUnit1.battle()
        target.battle()
        if hit(target):
            target.take_damage(pUnit1.pa)
            print(f"Tir reussi vous avez inflige  {pUnit1.pa} degats")
        else:
            print("Tir echoue")
def can_battle(pUnit1,pUnit2,player1,player2):
    if pUnit1.owner != pUnit2.owner and pUnit1.position == pUnit2.position and not player1.is_ally(player2.pid):
        return True
    else :
        return False







#id1 = deepcopy(destroyer)
#id1.set_param(1,(1,1))
#id2 = deepcopy(destroyer)
#id2.set_param(2,(1,1))

#print(id1.battling)
#print(hit(id2))

#battle(id1,id2)
#battle(id1,id2)
#print(id2.pv)

#print(id1.battling)

#changer les battling pour que les unités sur la meme cases passent en battle si une d'entre elle tape ou
#se fait taper
