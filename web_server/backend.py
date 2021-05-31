import sqlite3
import json

from bdd import give_connection

from bdd import  add_game, get_game_id, can_join, rm_game
from bdd import add_user, get_user_id, compare_passw, rm_user
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


def register_player(login, passwd, conn):
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
    pass



conn = give_connection('dev')

# print(register_player("user2", "test", conn))
# print(create_game(1, "game2", "naze", conn))

print(join_game(2, 4, "naze", conn))




conn.close()