from sp_motor.game_classes.game import game
from sp_motor.map.create import create_map

#creation de la partie
g1=game()
g1.load_conf()

g1.map = create_map(radius=350,nb_zonnes=(70, 90), zonnes_r=(45, 70), systems=(8, 15), inner_conf=(10, 15) )

#ajout des joueurs
g1.create_player()
g1.create_player()

#affichage des joueurs dans la partie
g1.print_players_game()

#creations des buildings
g1.create_building("mine",0,1)
g1.create_building("usine",0,1)

#affichage des buildings dans la partie
g1.print_buildings_game()

#affichage des systemes de la map de la partie
g1.print_systemes_map()

print("---------------------------------------------")
print("TEST DE CHANGEMENT DE PROPRIETAIRE DE SYSTEMS")
print("---------------------------------------------")


g1.change_owner_systeme(0,0)

#affichage des systemes possèder par le premier joueur
g1.print_systeme_player(0)

print("\n-changement de propriétaire-")
g1.change_owner_systeme(0,1)
g1.print_systeme_player(0)
g1.print_systeme_player(1)

print("---------------------------------------------")
print("TEST D'INTERACTION ENTRE JOUEUR")
print("---------------------------------------------")

#g1.create_interraction(0,1,1)#creation d'une demande d'alliance par p1, pour p2



