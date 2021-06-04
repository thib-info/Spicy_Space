import json
#from ressources import ressource
from sp_motor.game_classes.ressources import ressource
from sp_motor.players_interactions.Players_interraction import Players_interraction
from sp_motor.game_classes.systeme import systeme

with open("config/ressources.json") as g:
    conf_ress = json.load(g)
class player :
    def __init__(self, conf, pid, name, isMj=False):
        self.name = name
        self.pid = pid
        self.allies = []
        self.enemies=[]
        self.ressources = []
        self.systems = []
        self.isMj = isMj
        self.interraction_request=[]
        self.interraction_create=[]
<<<<<<< HEAD
        self.unit=[]
=======
        self.units_id = []
>>>>>>> origin/war

    def get_isMJ(self):
        return self.isMj
    def affiche(self):
        print(f"{self.name},{self.isMj}")

    def add_enemy(self,pid):
        if not pid in self.allies and not pid in self.enemies:
            self.enemies.append(pid)
    def add_ally(self,pid):
        if not pid in self.allies and not pid in self.enemies:
            self.allies.append(pid)

    #LES CINQ FONCTIONS CI DESSOUS N'ONT PAS ETE TESTER
    def remove_enemy(self,pid):
        if pid in self.enemies:
            self.enemies.remove(pid)
    def remove_ally(self,pid):
        if pid in self.allies:
            self.allies.remove(pid)

    def send_interraction(self,Player_interraction):
        Player_interraction.is_sended()
        Player_interraction.player2.interraction_request.append(Player_interraction) #AJOUTE LA REQUET A LA LISTE DES REQUETS DU DESTINATAIRE

    def accept_interraction(self,Player_interraction):
        Player_interraction.is_accepted()
        Player_interraction.execute()
        self.interraction_request.remove(Player_interraction) #SUPPRIME LA REQUET DE LA LISTE DES REQUETS RECUES

    def decline_interraction(self,Player_interraction):
        Player_interraction.is_declined()
        self.interraction_request.remove(Player_interraction) #SUPPRIME LA REQUET DE LA LISTE DES REQUETS RECUES

    def read_interraction_request(self):
        print("\n")
        for i in self.interraction_request:
            print("Requet de type " + str(i.type) +", du joueur "+str(i.player1.pid))
        print("\n")

    def send_interraction_created(self):
        for i in self.interraction_create:
            self.send_interraction(i)

    def set_param(self,pid, name,isMJ= False):
        self.pid = pid
        self.name = name
        self.isMj = isMJ

    def is_ally(self, pid):
        for i in self.allies:
            if pid == self.allies[i]:
                return True
            else:
                return False

    def is_enemy(self, pid):
        for i in self.enemies:
            if pid == self.enemies[i]:
                return True
            else:
                return False

    #fonction pour test
    def print_ally(self):
        for i in self.allies:
            print(i.pid)
    #fonction pour test
    def print_enemies(self):
        for i in self.enemies:
            print(i.pid)

    def create_interraction(self,p2,type):
        interraction=Players_interraction(self,p2,type)
        self.interraction_create.append(interraction)

    def add_systeme(self,systeme):
        self.systems.append(systeme)

    def remove_systeme(self,systeme):
        self.systems.remove(systeme)

    def ressources_init_player(self):
        temp = ressource("or")
        temp.apply_conf()
        self.ressources=temp.total_ressources()

    def print_ressources(self):
        for i in self.ressources:
            print("player id= "+str(self.pid)+ " ressources: "+str(i.type)+" : "+str(i.value))

    def recolte_production(self):
        for i in self.systems:
            for j in i.buildings:
                j.produce2()




with open("config/config_player.json") as f:
    conf = json.load(f)
#test = player(conf["player"], 1,"oui")
#test.add_ally(4)

#print(test.allies)

#TEST DES INTERRACTIONS

# p1 = player(conf["player"],1,"oui")
# p2 = player(conf["player"],2,"oui")
# p3 = player(conf["player"],3,"oui")

# p1.create_interraction(p2,2)
# p1.create_interraction(p2,4)

# print("Etat initial de l'interraction: "+ str(p1.interraction_create[0].state))
# p1.send_interraction_created()
# print("Etat de l'interraction après envoi: "+ str(p1.interraction_create[0].state))
# print("\nlecture des requets reçu par p2:")
# p2.read_interraction_request()
# print("P2 enemmies avant:")
# p1.print_enemies()
# print("P1 enemmies avant:")
# p2.print_enemies()

# p2.accept_interraction(p2.interraction_request[0])
# print("P2 enemmies après:")
# p1.print_enemies()

# print("P2 enemmies après:")
# p2.print_enemies()


# p2.decline_interraction(p2.interraction_request[0])
# print("P2 enemmies après:")
# p1.print_enemies()

# print("P2 enemmies après:")
# p2.print_enemies()



# print("Etat de l'interraction après acceptation: "+ str(p1.interraction_create[0].state))


# print("\n")
# print("test ressources")
# #p1.print_ressources()
# p1.ressources_init_player()
# p1.print_ressources()

# systeme_test=systeme("dasysteme","dalocation")
# systeme_test.add_building()
# systeme_test.buildings[0].change_owner(p1)
# #print("le owner:"+str(systeme_test.buildings[0].owner))
# systeme_test.print_buildings()
# p1.add_systeme(systeme_test)
# print("\n")
# #p1.recolte_production()
# #p1.print_ressources()

# #print(p1.ressources[0])