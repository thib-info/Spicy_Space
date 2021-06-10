import json
from copy import deepcopy
import numpy as np

from sp_motor.players_interactions.Players_interraction import Players_interraction
from sp_motor.utils import load_conf_f



class player :
    def __init__(self):
        self.name = ""
        self.pid = -1
        self.isMj = False

        self.units_id = []
        self.known_systems = []
        self.ressources = {}

        self.allies_id = []
        self.enemies_id = []
        self.systems_id = []
        
        self.sys_allies = []
        self.available_systems = []

        self.access_graph = None
        
        
        self.interraction_requested_id = []
        self.interraction_created_id = []
        
    ################## configuration du joueur #########
    def set_param(self, pid, name, isMJ=False):
        self.pid = pid
        self.name = name
        self.isMj = isMJ
    ####################################################




    ##################### FONCTION DES INTERACTIONS ######
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

    # def send_interraction(self,Player_interraction_id):
    #     Liste_interraction=deepcopy(game.Players_intteractions)
    #     interraction=Liste_interraction[Player_interraction_id]
    #     interraction.is_sended()
    #     interraction.player2.interraction_request.append(Player_interraction_id) #AJOUTE LA REQUET A LA LISTE DES REQUETS DU DESTINATAIRE
    #     game.Players_intteractions[Player_interraction_id]=interaction

    # def accept_interraction(self,Player_interraction_id):
    #     Liste_interraction=deepcopy(game.Players_intteractions)
    #     interraction=Liste_interraction[Player_interraction_id]
    #     interraction.is_accepted()
    #     interraction.execute()
    #     self.interraction_request.remove(interraction) #SUPPRIME LA REQUET DE LA LISTE DES REQUETS RECUES

    # def decline_interraction(self,Player_interraction_id):
    #     Liste_interraction=deepcopy(game.Players_intteractions)
    #     interraction=Liste_interraction[Player_interraction_id]
    #     interraction.is_declined()
    #     self.interraction_request.remove(interraction) #SUPPRIME LA REQUET DE LA LISTE DES REQUETS RECUES

    # def read_interraction_request(self):
    #     print("\n")
    #     for i in self.interraction_request_id:
    #         print("Requet de type " + str(i.type) +", du joueur "+str(i.player1.pid))
    #     print("\n")

    # def send_interraction_created(self):
    #     for i in self.interraction_created:
    #         self.send_interraction(i)

    



    ##########fonctions en sursis, pourraient etres deplacées dans games ##############""
    def is_ally(self, pid):
        for i in self.allies_id:
            if pid == self.allies_id[i]:
                return True
            else:
                return False

    def is_enemy(self, pid):
        for i in self.enemies_id:
            if pid in self.enemies_id[i]:
                return True
            else:
                return False
    ################## fin du sursis #####################

    def create_interraction(self,p2,type):
        interraction=Players_interraction(self,p2,type)
        self.interraction_create.append(interraction)

    ######################### FIN DES INTERACTION ##########

    def add_systeme(self,systeme_id):
        #systeme.change_owner(self)
        self.systems_id.append(systeme_id)

    def remove_systeme(self,systeme_id):
        self.systems_id.remove(systeme_id)


    def add_known_systems(self):
        self.known_systems.append()#ajouter les neighbor

    ##################### systeme de ressources ##############

    def ressources_init_player(self, model):
        self.ressources = deepcopy(model)
        for c in self.ressources.keys():
            self.ressources[c] = {
                "qt":self.ressources[c],
                "qt_t":0,
            }

    
    def update_prod(self, prod):
        for c, v in prod.items():
            self.ressources[c] = {
                "qt":v["qt"] + self.ressources[c]["qt"],
                "qt_t":v["qt"] + self.ressources[c]["qt_t"],  #production par tour affichée avec un mois de délai
            }

    def can_afford(self, cost):
        for c, v in cost.items():
            if self.ressources[c] < v:
                return False
        return True

    # ajouter une mth pour déduire les frais de fct
    
    ####################### fin des systemes de ressources #########
    
