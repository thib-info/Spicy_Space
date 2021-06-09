from sp_motor.game_classes.game import game
from sp_motor.game_classes.map import System_p

#creation de la partie
g1=game()
g1.load_conf()

#ajout des joueurs
p1_id=g1.create_player()
p2_id=g1.create_player()

#creation d'un systeme
s1_id=g1.create_systeme("dasysteme","daposition")

#changement du propriétaire
g1.change_owner_systeme(s1_id,p1_id)

#creation d'un batiment
g1.create_building("mine",s1_id,p1_id)






