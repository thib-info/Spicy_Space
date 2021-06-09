import json
import pickle
from random import choice
from copy import deepcopy

from sp_motor.game_classes.player import player 
from sp_motor.game_classes.unit import unit 
from sp_motor.game_classes.building import building
from sp_motor.utils import load_conf_f
from sp_motor.players_interactions.Players_interraction import Players_interraction




PLAYER1_NAME = "Toto"

class game():
    def __init__(self):
        self.map = None

        self.players = []
        self.units = []
        self.buildings = []
        
        
        self.players_interactions=[]
        self.models = {}
        self.turn =[] #conf["turn"]

        self.sys_in_war = []
        self.last_id = {
            "unit":0
            }


    ##### etapes de configuration, à faire seulement au deb ################
    def load_conf(self):
        conf_unit = load_conf_f("config_unit")
        for key,model in conf_unit.items():
            self.models[key] = unit(model, -1, -1)


        conf_ress = load_conf_f("ressources")
        self.models["ressources"] = {}
        for c, v in conf_ress.items():
            self.models["ressources"][c] = v["value"]

    def import_map(self, map):
        self.map = deepcopy(map)
        
        
    ##################### fin des étapes uniques ################


    ############ trouver les bons index ######################
    def get_player(self,pid):
        for i in range(len(self.players)):
            if self.players[i].pid == pid:
                return i
        return -1

    def get_buildings(self,id):
        for i in range(len(self.building)):
            if self.buildings.id == id:
                return i
        return -1

    def get_unit(self,id):
        for i in range(len(self.units)):
            if self.units[i].id==id:
                return i
        return -1
    
    def get_players_interactions(self,id):
        for i in self.players_interractions:
            if i.id==id:
                return i
        return -1

    def get_systems(self,id):
        for i in range(len(self.map.systems)):
            if self.map.systems[i].id == id:
                return i
        return -1
    ################# fin des fonctions d'index #################



    ############### gestion des unités #########################
    def delete_unit(self,id_unit):
        su = deepcopy(self.units[self.get_unit(id_unit)])
        self.players[self.get_player(su.owner)].units_id.pop(self.players[self.get_player(su.owner)].units_id.index(su.id))
        self.map.systems[self.map.get_system(su.position)].units_id.pop(self.map.systems[self.map.get_system(su.position)].units_id.index(id_unit))

        self.units.pop(self.get_unit(id_unit))


    def create_unit(self, owner_id, position, created_unit, base_lvl=1):
        temp_unit = deepcopy(self.models[created_unit])
        temp_unit.id = self.last_id["unit"]
        self.last_id["unit"] += 1
        temp_unit.set_param(owner_id, position, base_lvl)
        tu_id = temp_unit.id

        self.units.append(temp_unit)
        self.players[self.get_player(owner_id)].units_id.append(tu_id)
        self.map.systems[self.map.get_system(position)].units_id.append(tu_id)


    def can_unit_move(self, u_id, dest_id):
        u = deepcopy(self.units[self.get_unit(u_id)])

        i_d, i_a = self.map.get_system(u.position), self.map.get_system(dest_id)

        pm_restants = u.pm - self.players[self.get_player(u.owner)].access_graph[i_d, i_a]

        return pm_restants

        


    def move_unit(self, u_id, dest_id):
        new_pm = self.can_unit_move(u_id, dest_id)
        if new_pm >= 0:
            u = deepcopy(self.units[self.get_unit(u_id)])
            u_pos = self.map.get_system(u.position)
            self.map.systems[u_pos].units.pop(self.map.systems[u_pos].unit.index(u_pos))
            
            self.units[self.get_unit(u_id)].position = dest_id
            self.units[self.get_unit(u_id)].pm = new_pm

            new_pos = self.map.get_system(dest_id)
            self.map.systems[new_pos].units.append(u_id)

   ############## fin de gestion des unités ###################



    ################## configuration des joueurs ################
    def create_player(self, pid, name, isMj=False):
        if len(self.players) == 0 or self.get_player(pid) == -1:
            temp_p = player()
            temp_p.set_param(pid, name, isMj)
            temp_p.ressources_init_player(self.models["ressources"])
            #ajouter un arbre technologique
            

            #on cherche un secteur vide pour faire spawn le joueur
            ava_sect = self.map.get_empty_sectors()
            if len(ava_sect) == 0:
                #partie pleine
                return False
            
            spawn_sec_id = choice(ava_sect)
            poss_spawn_sys = self.map.sectors[self.map.get_sector(spawn_sec_id)].members[:]
            spawn_sys_id = choice(poss_spawn_sys)

            sys_id = self.map.get_system(spawn_sys_id)

            # on ajoute le joueur
            self.players.append(deepcopy(temp_p))
            
            #on lui donne 2 vaisseaux
            self.create_unit(pid, sys_id, "colon")
            self.create_unit(pid, sys_id, "scout")

            #on renvoie true pour dire que c'est réussi
            return True
        
        return False

    def update_players_syst(self):
        neutral_sys = self.map.get_systems_from_owner(-1)

        for pl in self.players:

            sys_allies = []
            for ally in pl.allies_id:
                sys_allies += self.map.get_systems_from_owner(ally)

            pl.sys_allies = list(set(sys_allies))

        
            temporary_list = pl.known_systems[:]
            pl.available_systems = []
            for sys in temporary_list:
                if sys in neutral_sys :
                    pl.available_systems.append(sys)

            pl.available_systems = list(set(pl.available_systems + pl.sys_allies + self.sys_in_war))


            ok_indices = [self.get_systems(id) for id in pl.available_systems]
            no_indices = [self.get_systems(id) for id in self.sys_in_war]
            pl.access_graph = self.map.send_access_graph(ok_indices, no_indices)


            



    ################## fin de la partie sur les joueurs ###############



    

    
    
    ######### en rapport avec les systemes ################
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
                

    #vient tester si un joueur possède un systeme
    def is_proprio(self, p_id, sys_id):
        return p_id == self.systems[self.get_systems(sys_id)].owner_id

    def colonize(self, unit_id):
        u_id = self.get_unit(unit_id)
        s_id = self.get_systems(self.units[u_id].position)
        if self.units[unit_id].name == "colon":
            if self.map.systems[s_id].owner_id == -1:
                self.map.systems[s_id].change_owner(self.units[u_id].owner)

    ############ fin des systemes ###################




    ############ gestion des buildings ##############
    def create_building(self,type,systeme_id,owner_id):
        #creation du batiment
        tmp = building(type,systeme_id,owner_id)

        #ajout du batiment a la liste des batiments de game
        self.buildings.append(tmp)

        #ajout du batiment au systeme concerné
        player = self.get_player(owner_id)

        return tmp.id
    ############# fin de gestion des buildings #########




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

    ############## fin de la gestion des ressources ####################




#########################" fin de la classe "####################
#################################################################
#################################################################






################# fonctions de sauvegarde  #####################
def save_game(game, path):
    with open(path, 'wb') as f:
        pickle.dump(game, f)

def load_game(path):
    with open(path, 'rb') as f:
        output = pickle.load(f)
    return output
############### fin des fonctions de sauvegarde #####################


