import json
import pickle
from random import choice, randint
from copy import deepcopy

from sp_motor.game_classes.player import player 
from sp_motor.game_classes.unit import unit
from sp_motor.game_classes.technology import technology
from sp_motor.game_classes.building import building
from sp_motor.utils import load_conf_f
from sp_motor.players_interactions.Players_interraction import Players_interraction




PLAYER1_NAME = "Toto"

class game():
    def __init__(self):
        self.map = None

        self.players = []
        self.units = []
        
        
        self.players_interactions=[]
        self.models = {}
        self.turn = 1 #conf["turn"]

        self.sys_in_war = []
        self.last_id = {
            "unit":0
            }


    ##### etapes de configuration, à faire seulement au deb ################
    def load_conf(self):
        conf_unit = load_conf_f("config_unit")
        for key,model in conf_unit.items():
            self.models[key] = unit(model, -1, -1)

        conf_tech = load_conf_f("base_tech")
        self.models["tech"] = {}
        for c in conf_tech.keys():
            tech = technology(conf_tech, c)
            self.models["tech"][c] = tech



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


    def can_battle(self, u1_id, u2_id):
        u1 = deepcopy(self.units[self.get_unit(u1_id)])
        u2 = deepcopy(self.units[self.get_unit(u2_id)])

        return u1.position == u2.position and u1.owner != u2.owner
        

    def battle_unit(self, u1_id, u2_id):
        
        u1 = deepcopy(self.units[self.get_unit(u1_id)])
        u2 = deepcopy(self.units[self.get_unit(u2_id)])


        if u1.cible == u2.id and u2.cible == u1.id:
            if u1.precision >= randint(1, 100):
                u2.take_damage(u1.pa)
            
            if u2.precision >= randint (1, 100):
                u1.take_damage(u1.pa)

            u1.cible = -1
            u2.cible = -1

        elif u1.cible == u2.id:
            if u1.precision >= randint(1, 100):
                u2.take_damage(u1.pa)

            u1.cible = -1

        elif u2.cible == u1.id:
            if u2.precision >= randint (1, 100):
                u1.take_damage(u1.pa)

            u2.cible = -1

        self.units[u1_id] = u1
        self.units[u2_id] = u2

        pl1 = deepcopy(self.players[self.get_player(u1.owner)])
        pl2 = deepcopy(self.players[self.get_player(u2.owner)])

        if pl1.pid in pl2.allies_id:
            pl2.allies_id.pop(pl2.allies_id.index(pl1.id))

        if pl1.pid not in pl2.enemies_id:
            pl2.enemies_id.append(pl1.id)

        if pl2.pid in pl1.allies_id:
            pl1.allies_id.pop(pl1.allies_id.index(pl2.id))

        if pl2.pid not in pl1.enemies_id:
            pl1.enemies_id.append(pl2.id)

        self.players[self.get_player(u1.owner)] = pl1
        self.players[self.get_player(u2.owner)] = pl2

            
        ### mettre les joueurs en guerre, rompre alliance

   ############## fin de gestion des unités ###################



    ################## configuration des joueurs ################
    def create_player(self, pid, name, isMj=False):
        if len(self.players) == 0 or self.get_player(pid) == -1:
            temp_p = player()
            temp_p.set_param(pid, name, isMj)
            temp_p.ressources_init_player(self.models["ressources"])
            for c, v in self.models["tech"].items():
                temp_p.import_tree(v, c)


            print(temp_p.ressources)


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
        for pl_indice in range(len(self.players)):
            pl = deepcopy(self.players[pl_indice])
            sys_allies = []
            for ally in pl.allies_id:
                sys_allies += self.map.get_systems_from_owner(ally)

            pl.sys_allies = list(set(sys_allies))

            # units = [self.units[self.get_unit(id)].position for id in pl.units]        
            pl.known_systems = list(set(pl.known_systems[:] + [self.units[self.get_unit(id)].position for id in pl.units_id] ))


            temporary_list = pl.known_systems[:]
            pl.available_systems = []
            for sys in temporary_list:
                if sys in neutral_sys :
                    pl.available_systems.append(sys)

            pl.available_systems = list(set(pl.available_systems + pl.sys_allies + self.sys_in_war))


            ok_indices = [self.get_systems(id) for id in pl.available_systems]
            no_indices = [self.get_systems(id) for id in self.sys_in_war]
            pl.access_graph = self.map.send_access_graph(ok_indices, no_indices)

            self.players[pl_indice] = pl

    ################## fin de la partie sur les joueurs ###############




    ######### en rapport avec les systemes ################
    #vient modifier le timer de paix d'un systeme
    def is_syst_in_war(self, sys_id):
        s_id = self.get_systems(sys_id)
        ow_id = self.map.systems[s_id].owner_id
        sys = deepcopy(self.map.systems[s_id])

        present_players = []
        for u_id in sys.units_id:
            present_players.append(self.units[self.get_unit(u_id)].owner)

        present_players = list(set(present_players))
        if ow_id in present_players:
            present_players.pop(present_players.index(ow_id))
            
        else:
            if sys_id in self.players[self.get_player(ow_id)].systems_id:
                self.players[self.get_player(ow_id)].systems_id.pop(self.players[self.get_player(ow_id)].systems_id.index(sys_id))
            sys.owner_id = - 1

        
        for p_id in present_players:
            if p_id in self.players[self.get_player(ow_id)].enemies_id:
                sys.to_peace = 4
        
        if sys.to_peace == 0 and sys.owner_id == -1:
            new_prop = -1
            counter = {}

            for u_id in sys.units_id:
                p_id = self.units[self.get_unit(u_id)].owner
                if p_id in counter.keys():
                    counter[p_id] += 1
                else:
                    counter[p_id] = 1

                new_prop = p_id
            for c, v in counter.items():
                if v > counter[new_prop]:
                    new_prop = c

            sys.owner_id = new_prop
            self.players[self.get_player(new_prop)].systems_id.append(sys_id)



        self.map.systems[s_id] = deepcopy(sys)
                

    #vient tester si un joueur possède un systeme
    def is_proprio(self, p_id, sys_id):
        return p_id == self.map.systems[self.get_systems(sys_id)].owner_id
    ############ fin des systemes ###################




    ############ gestion des buildings ##############
    # def add_building(self, b_type, sys_id):
        #venir ajouter les batiments, là je ne viens meme pas regarder
        #soumed by les costs

    
    ############# fin de gestion des buildings #########







    ################## syst de production des ressources #########
    def update_player_ressources(self):
        for pl in range(len(self.players)):
            player = deepcopy(self.players[pl])

            pl_sys_index = [self.get_systems(id) for id in player.systems_id]
            #partie ajout des productions pour chaques joueurs
            for c in player.ressources.keys():
                player.ressources[c]["qt_t"] = 0


            for sys_id in pl_sys_index:
                sys_prod = self.map.systems[sys_id].produce(self.models["ressources"])
                player.update_prod(sys_prod)

            #fin de la partie sur la production

            #partie prend en compte les couts de fonctionnement

    ############## fin de la gestion des ressources ####################



    ####### fonctions d'export pour un joueur #######################
    def to_front(self, p_id):
        output = {}
        u_id = self.get_player(p_id)

        pl = deepcopy(self.players[u_id])
        output["ressources"] = deepcopy(self.players[u_id].ressources)

        #traitement des alliés et ennemis
        output["allies_id"] = pl.allies_id[:]
        output["enemies_id"] = pl.enemies_id[:]

        #les systemes qu'il peut voir, pour le fog
        temp = [self.map.get_system(id) for id in pl.known_systems]
        envi = []
        for i in temp:
            for j in range(self.map.graph_link.shape[0]):
                if self.map.graph_link[i, j] > 0:
                    envi.append(j)

        output["visible_systs"] = list(set(temp + envi))


        
        #attraper les unités presentes dans ces systemes
        output["units"] = []
        for s_id in output["visible_systs"]:
            concerned_units = [self.get_unit(id) for id in self.map.systems[s_id].units_id]
            output["units"] += [self.units[id].to_front() for id in concerned_units]

        #le detail de ses systemes
        sys_details = {}
        for sys_id in pl.systems_id:
            s_id = self.map.get_system(sys_id)
            sys_details[s_id] = self.map.systems[s_id].export_system_info()

        output["tech"] = {}
        for c, v in pl.tech.items():
            output["tech"][c] = v.to_front()

        output["syst_details"] = sys_details

        # output["tech"] = pl.tech
        

        #les interactions ne sont pas gérées
        return output
        




    ######## fonction de mise à jour de la partie, pour passer au tour suivant ##########
    def to_next_turn(self):
        for sys_id in range(len(self.map.systems)):
            # sys_id = self.get_systems(i)
            self.map.systems[sys_id].to_peace = max(self.map.systems[sys_id].to_peace -1, 0)
            bef = self.map.systems[sys_id].to_peace
            self.is_syst_in_war(sys_id)

            if bef > 0 and self.map.systems[sys_id].to_peace == 0:
                self.sys_in_war.pop(self.sys_in_war.index(sys_id))

            if self.map.systems[sys_id].to_peace > 0 and sys_id not in self.sys_in_war:
                self.sys_in_war.append(sys_id)


        #on applique les combats
        for unit_id in range(len(self.units)):
            if self.units[self.get_unit(unit_id)].cible != -1:
                battle_unit(unit_id, self.units[self.get_unit(unit_id)].cible)

        #on nettoire les cadavres
        new_units = []
        for i in range(len(self.units)):
            if self.units[i].pv > 0:
                new_units.append(deepcopy(self.units[i]))

        self.units = new_units
            

            

        
        #ici la fonction pour savoir qui controle le plus un syst

        self.update_players_syst()
        

        self.update_player_ressources()


        self.turn += 1



        



            




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


