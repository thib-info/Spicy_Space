import json
import pickle

from sp_motor.game_classes.player import player 
from sp_motor.game_classes.unit import unit 
from sp_motor.game_classes.building import building
from sp_motor.utils import load_conf_f

from copy import deepcopy
from sp_motor.game_classes.player import player

PLAYER1_NAME = "Toto"

class game():
    def __init__(self):
        self.players = []
        self.systems =[] #conf["map"]
        self.turn =[] #conf["turn"]
        self.units = []
        self.buildings = []
        self.map = None
        self.models = {}
        self.players_interactions=[]


    def import_map(self, map):
        for i in range(len(map.systems)):
            self.systems.append(map.systems[i].id)
        

    def create_player(self,isMJ=False):
        tmp=deepcopy(self.models["player"])
        tmp.ressources_init_player()
        self.players.append(tmp)
        self.players[-1].set_param(len(self.players)-1, PLAYER1_NAME,isMJ)
        return tmp.pid

    def get_player(self,pid):
        for i in range(len(self.players)):
            if self.players[i].pid==pid:
                return i
        return -1

    def get_unit(self,id):
        for i in range(len(self.units)):
            if self.units[i].id==id:
                return i
        return -1

    def get_systems(self,id):
        for i in range(len(self.map.systems)):
            if self.map.systems[i].id == id:
                return i
        return -1

    def get_buildings(self,id):
        for i in range(len(self.building)):
            if self.buildings.id == id:
                return i
        return -1

    def get_players_interactions(self,id):
        for i in self.players_interractions:
            if i.id==id:
                return i

    def next_turn(self):
        self.turn += 1

    def load_conf(self):
        conf_player = load_conf_f("config_player")
        self.models["player"] = player(conf_player["player"], -1, "NULL")

        conf_unit = load_conf_f("config_unit")

        for key,model in conf_unit.items():
            self.models[key] = unit(model, -1, -1)

        conf_ress = load_conf_f("ressources")
        self.models["ressources"] = {}
        for c, v in conf_unit.items():
            self.models["ressources"][c] = v["value"]

    def delete_unit(self,id_unit):
        self.units.pop(id_unit)

    def create_unit(self, owner_id, position, created_unit, base_lvl=1,):
        self.units.append(deepcopy(self.models[created_unit]))
        self.units[-1].set_param(owner_id, position, base_lvl)
        self.players[owner_id].units_id.append(self.units[-1].id)

 ################## PLAYERS INTERRACTIONS ##################
    def create_interraction(self,pid1,pid2,type):
        interraction=Players_interraction(pid1,pid2,type) #créer l'interraction
        self.players_interactions.append(interraction) #l'ajoute à la liste des interractions de la partie
        pid1.interraction_created_id.append(interraction.id)#ajoute l'id de l'interraction à la liste des interractions créer du joueur

    def send_interraction(self,Player_interraction_id):
        index=self.get_players_interactions(self,Player_interraction_id)#recupere l'index correspondant à l'id de l'interraction
        interraction=self.players_interactions[index] #recuperation de l'interraction
        interraction.is_sended()
        interraction.player2.interraction_request.append(Player_interraction_id) #ajoute l'id de l'interraction à la liste des interractions request du joueur destinataire

    def accept_interraction(self,Player_interraction_id):
        index=self.get_players_interactions(self,Player_interraction_id)#recupere l'index correspondant à l'id de l'interraction
        interraction=self.players_interactions[index] #recuperation de l'interraction
        interraction.is_accepted()
        interraction.execute() #execute l'interraction (A VERIFIER FONCTIONNEMENT)
        interraction.player2.interraction_request.remove(interraction) #supprimer l'interraction de la liste des request du joueur destinataire

    def decline_interraction(self,Player_interraction_id):
        index=self.get_players_interactions(self,Player_interraction_id)#recupere l'index correspondant à l'id de l'interraction
        interraction=self.players_interactions[index] #recuperation de l'interraction
        interraction.is_declined()
        interraction.player2.interraction_request.remove(interraction) #supprimer l'interraction de la liste des request du joueur destinataire

    def read_interraction_request(self,pid):
        index=self.get_player(pid)
        player=self.players[index] #recuperation du joueur concerner
        print("\n")
        for i in player.interraction_request_id:
            interraction=self.players_interactions[i] #recuperation de l'interraction
            print("Requet de type " + str(interraction.type) +", du joueur "+str(interraction.player1))
        print("\n")

    def send_interraction_created(self,pid): #envoi toutes les interractions créer
        index=self.get_player(pid)
        player=self.players[index] #recuperation du joueur concerner
        for i in player.interraction_created:
            player.send_interraction(i)


    ################## syst de production des ressources #########


    def update_player_ressources(self):
        for player in self.players:

            pl_sys_index = [self.get_systems(id) for id in player.systems_id]
            #partie ajout des productions pour chaques joueurs
            for c in player.ressources:
                player.ressources[c]["qt_t"] = 0


            for sys_id in pl_sys_index:
                local_buildings = [deepcopy(self.buildings[self.get_buildings(id)]) for id in self.systems[sys_id].buildings_id]
                sys_prod = self.systems[sys_id].produce(self.models["ressources"], local_buildings)
                player.update_prod(sys_prod)

            #fin de la partie sur la production

            #partie prend en compte les couts de fonctionnement





    def change_owner_systeme(self,systeme_id,owner_id):
        self.list_systems[systeme_id].change_owner(owner_id)


    def create_building(self,type,systeme_id,owner_id):
        #creation du batiment
        tmp = building(type,systeme_id,owner_id)

        #ajout du batiment a la liste des batiments de game
        self.list_buildings.append(tmp)
        #ajout du batiment au systeme concerné
        self.list_systems[systeme_id].add_building(tmp.id)

        return tmp.id



   # def discover(self,unit_id):                   #A SUPPR
    #    pos = self.units[unit_id].position
     #   ow = self.units[unit_id].owner
      #  self.players[ow].known_systems += [2] #ajouter les voisins ici

   # def move_unit(self, unit_id, destination):
    #    self.units[unit_id].position = destination
     #   self.discover(unit_id)

    #################
    #syst interactions

    #vient modifier le timer de paix d'un systeme
    def is_syst_in_war(self, sys_id):
        s_id = self.get_systems(sys_id)
        ow_id = self.systems[s_id].owner_id
        sys = deepcopy(self.systems[s_id])

        present_players = []
        for u_id in sys.units_id:
            present_players.append(self.units[self.get_unit(u_id)].owner)

        present_players = list(set(present_players))
        present_players.pop(present_players.index(ow_id))

        for p_id in present_players:
            if p_id in self.players[self.get_player(ow_id)].enemies_id:
                sys.to_peace = 4
        
        self.systems[s_id] = deepcopy(sys)
                
    #################

    #vient tester si un joueur possède un systeme
    def is_proprio(self, p_id, sys_id):
        return p_id == self.systems[self.get_systems(sys_id)].owner_id

    def colonize(self, unit_id):
        u_id = self.get_unit(unit_id)
        s_id = self.get_systems(self.units[u_id].position)
        if self.units[unit_id].name == "colon":
            if self.map.systems[s_id].owner_id == -1:
                self.map.systems[s_id].change_owner(self.units[u_id].owner)


######################################""
def save_game(game, path):
    with open(path, 'wb') as f:
        pickle.dump(game, f)

def load_game(path):
    with open(path, 'rb') as f:
        output = pickle.load(f)
    return output



# g1 = game()
# g1.load_conf()
# g1.create_player()
# g1.create_player(True)
# print(g1.players[0])
# print(g1.players[1])
# #print(g1.players[0].name)
# #print(g1.players[1].pid)

# with open("../../../config/config_unit.json") as g:
#     conf_unit = json.load(g)


# destroyer = unit(conf_unit["destroyer"], -1, [-1, -1])
# u1=deepcopy(destroyer)
# g1.units.append(u1)
# g1.units.append(u1)
# print(g1.units)
# g1.delete_unit(0)
# print(g1.units)
>>>>>>> coloniser
