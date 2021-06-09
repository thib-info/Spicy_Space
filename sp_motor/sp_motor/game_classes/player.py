import json
#from ressources import ressource
from sp_motor.game_classes.ressources import ressource
from sp_motor.players_interactions.Players_interraction import Players_interraction
#from sp_motor.game_classes.systeme import systeme
from sp_motor.utils import load_conf_f
import sp_motor.game_classes.game

#conf_ress = load_conf_f("ressources")
class player :
    def __init__(self, conf, pid, name, isMj = False):
        self.name = name
        self.pid = pid
        self.allies_id = []
        self.enemies_id = []
        self.ressources = {}
        self.systems_id = []
        self.isMj = isMj
        self.interraction_requested_id = []
        self.interraction_created_id = []
        self.units_id = []
        self.known_systems = []


    def get_isMJ(self):
        return self.isMj
    def affiche(self):
        print(f"{self.name},{self.isMj}")

    def add_enemy(self,pid):
        if not pid in self.allies_id and not pid in self.enemies_id:
            self.enemies_id.append(pid)
    def add_ally(self,pid):
        if not pid in self.allies_id and not pid in self.enemies_id:
            self.allies_id.append(pid)

    #LES CINQ FONCTIONS CI DESSOUS N'ONT PAS ETE TESTER
    def remove_enemy(self,pid):
        if pid in self.enemies_id:
            self.enemies_id.remove(pid)
    def remove_ally(self,pid):
        if pid in self.allies_id:
            self.allies_id.remove(pid)

    def send_interraction(self,Player_interraction_id):
        Liste_interraction=deepcopy(game.Players_intteractions)
        interraction=Liste_interraction[Player_interraction_id]
        interraction.is_sended()
        interraction.player2.interraction_request.append(Player_interraction_id) #AJOUTE LA REQUET A LA LISTE DES REQUETS DU DESTINATAIRE
        game.Players_intteractions[Player_interraction_id]=interaction

    def accept_interraction(self,Player_interraction_id):
        Liste_interraction=deepcopy(game.Players_intteractions)
        interraction=Liste_interraction[Player_interraction_id]
        interraction.is_accepted()
        interraction.execute()
        self.interraction_request.remove(interraction) #SUPPRIME LA REQUET DE LA LISTE DES REQUETS RECUES

    def decline_interraction(self,Player_interraction_id):
        Liste_interraction=deepcopy(game.Players_intteractions)
        interraction=Liste_interraction[Player_interraction_id]
        interraction.is_declined()
        self.interraction_request.remove(interraction) #SUPPRIME LA REQUET DE LA LISTE DES REQUETS RECUES

    def read_interraction_request(self):
        print("\n")
        for i in self.interraction_request_id:
            print("Requet de type " + str(i.type) +", du joueur "+str(i.player1.pid))
        print("\n")

    def send_interraction_created(self):
        for i in self.interraction_created:
            self.send_interraction(i)

    def set_param(self,pid, name,isMJ= False):
        self.pid = pid
        self.name = name
        self.isMj = isMJ

    def is_ally(self, pid):
        for i in self.allies_id:
            if pid == self.allies_id[i]:
                return True
            else:
                return False

    def is_enemy(self, pid):
        for i in self.enemies_id:
            if pid == self.enemies_id[i]:
                return True
            else:
                return False

    #fonction pour test
    def print_ally(self):
        for i in self.allies_id:
            print(i.pid)
    #fonction pour test
    def print_enemies(self):
        for i in self.enemies_id:
            print(i.pid)

    def create_interraction(self,p2,type):
        interraction=Players_interraction(self,p2,type)
        self.interraction_create.append(interraction)

    def add_systeme(self,systeme_id):
        #systeme.change_owner(self)
        self.systems_id.append(systeme_id)

    def remove_systeme(self,systeme_id):
        self.systems_id.remove(systeme_id)

    def ressources_init_player(self):
        temp = ressource("or")
        temp.apply_conf()
        self.ressources=temp.total_ressources()

    def print_ressources(self):
        for i in self.ressources:
            print("player id= "+str(self.pid)+ " ressources: "+str(i.type)+" : "+str(i.value))

    def recolte_production(self):
        for i in self.systems_id:
            for j in i.buildings:
                j.produce()

    def add_known_systems(self):
        self.known_systems.append()#ajouter les neighbor

#if __name__ == '__main__':
    #with open("../../../config/config_player.json") as f:
    #    conf = json.load(f)
    #test = player(conf["player"], 1,"oui")
    #test.add_ally(4)

    #print(test.allies)

    # TEST DES INTERRACTIONS

    #p1 = player(conf["player"],1,"oui")
    #p2 = player(conf["player"],2,"oui")
    #p3 = player(conf["player"],3,"oui")

    #p1.create_interraction(p2,2)
    #p1.create_interraction(p2,4)

    #print("Etat initial de l'interraction: "+ str(p1.interraction_create[0].state))
    #p1.send_interraction_created()
    #print("Etat de l'interraction après envoi: "+ str(p1.interraction_create[0].state))
    #print("\nlecture des requets reçu par p2:")
    #p2.read_interraction_request()
    #print("P2 enemmies avant:")
    #p1.print_enemies()
    #print("P1 enemmies avant:")
    #p2.print_enemies()

    #p2.accept_interraction(p2.interraction_request[0])
    #print("P2 enemmies après:")
    #p1.print_enemies()

    #print("P2 enemmies après:")
    #p2.print_enemies()


    #p2.decline_interraction(p2.interraction_request[0])
    #print("P2 enemmies après:")
    #p1.print_enemies()

    #print("P2 enemmies après:")
    #p2.print_enemies()



    #print("Etat de l'interraction après acceptation: "+ str(p1.interraction_create[0].state))


    #print("\n")
    #print("test ressources")
    #p1.print_ressources()
    #p1.ressources_init_player()
    #p1.print_ressources()


    #systeme_test=systeme("dasysteme","dalocation",p1)
    #systeme_test.add_building("mine")
    #systeme_test.add_building("usine")
    #systeme_test.print_buildings()
    #p1.add_systeme(systeme_test)
    #print("\n")
    #p1.recolte_production()
    #p1.print_ressources()


    #print(p1.ressources[0])