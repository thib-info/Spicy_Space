import sqlite3
import json
import os
from bdd import give_connection

from bdd import  add_game, get_game_id, can_join, rm_game, list_game_users
from bdd import add_user, get_user_id, compare_passw, rm_user, list_user_games
from bdd import add_player, change_player_qual, get_player_info, rm_player


config = {
    "gamefiles_path":"../games",
}

def create_game(user_id, name, code, conn):
    path =  name
    if get_game_id(name, conn) != None:
        return 'taken'

    add_game(name, path, code, conn)
    game_id = get_game_id(name, conn)
    if game_id == None:
        return 'error'
    #add game_files arbo
   
    add_player(user_id, 'mj', 0, game_id, conn)

    return 'ok'


def register_user(login, passwd, conn):
    if get_user_id(login, conn) != None:
        return 'taken'

    add_user(login, passwd, conn)
    return 'ok'

def join_game(user_id, game_id, code, conn):
    if can_join(game_id, code, conn):
        player_id = 1
        #player_id = ask_first_slot
        add_player(user_id, 'player', player_id, game_id, conn)
        return 'ok'

    else:
        return 'no'


def give_mj(user_id, login, game_id, conn):
    players = list_game_users(game_id, conn)
    info = get_player_info(user_id, game_id, conn)
    if info[0] == "mj":
        if login in players:
            new_mj = get_user_id(login, conn)
            change_player_qual(user_id, game_id, 'player', conn)
            change_player_qual(new_mj, game_id, 'mj', conn )
            return 'ok'
        else:
            return 'unknow'
    
    elif info[0] == None:
        return 'strange'
    return 'unauthorized'



def connect_user(login, passw, con):
    if compare_passw(login, passw, conn):
        return True
    return False


def list_files(path):
    output = {}
    for filename in os.listdir(path):
        if os.path.isdir(os.path.join(path ,filename)):
            output[filename] = list_files(os.path.join(path ,filename))
        else:
            output[filename] = None

    return output

def find_file(arbo, filename):
    for c, v in arbo.items():
        if v == None:
            if c == filename:
                return c
            
        if v != None:
            temp = find_file(v, filename)
            if temp != None:
                return os.path.join(c, temp)

            
            



    
        
    

    
    