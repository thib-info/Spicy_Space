import sqlite3 as sq
import json



def give_connection(type_conn):
    if type_conn == 'production':
        return sq.connect('db/production.db')
    elif type_conn == 'dev':
        return sq.connect('db/development.db')

#############################################
#############################################

def add_game(name, path, code, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"INSERT INTO game (name, path, code) VALUES ('{name}', '{path}', '{code}')"
    cur.execute(sql)
    conn.commit()
    cur.close()

def list_game_users(game_id, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"select u.login from game as g inner join player as p on p.game_id = g.id inner join user as u on u.id = p.user_id where g.id = {game_id}"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    if result != None:
        output = [i[0] for i in result]
        if len(output) == 0:
            return None
        return list(set(output))
    return result


def get_game_id(name, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"SELECT id FROM game WHERE name = '{name}'"
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    if result != None:
        return result[0]
    return result

def can_join(id, passw, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"SELECT code FROM game WHERE id = {id}"
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    if result != None:
        return result[0] == passw
    return False

def rm_game(id, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"delete from game where id = {id}"
    cur.execute(sql)
    conn.commit()
    cur.close()


###########################################################
###########################################################

def add_user(login, password, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"insert into user (login, password) values ('{login}', '{password}')"
    cur.execute(sql)
    conn.commit()
    cur.close()

def get_user_id(login, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"SELECT id FROM user WHERE login = '{login}'"
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    if result != None:
        return result[0]
    return result

def compare_passw(login, password, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"SELECT password FROM user WHERE login = '{login}'"
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    if result != None:
        return result[0] == password
    return False

def list_user_games(u_id, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"select g.name from game as g inner join player as p on p.game_id = g.id inner join user as u on u.id = p.user_id where u.id = {u_id}"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    if result != None:
        output = [i[0] for i in result]
        if len(output) == 0:
            return None
        return list(set(output))
    return result


def rm_user(user_id, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"delete from user where id = {user_id}"
    cur.execute(sql)
    conn.commit()
    cur.close()

###########################################
###########################################


def add_player(user_id, quality, player_id, game_id, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"insert into player (user_id, game_id, quality, player_id) values ({user_id}, {game_id}, '{quality}', {player_id})"
    cur.execute(sql)
    conn.commit()
    cur.close()

def change_player_qual(user_id, game_id, quality, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"update player set quality = '{quality}' where user_id = {user_id} and game_id = {game_id}"
    cur.execute(sql)
    conn.commit()
    cur.close()

def get_player_info(user_id, game_id, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"SELECT quality, player_id FROM player WHERE user_id = {user_id} and game_id = {game_id}"
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    if result != None:
        return result
    return result


def rm_player(user_id, game_id, conn_t):
    conn = give_connection(conn_t)
    cur = conn.cursor()
    sql = f"delete from player where user_id = {user_id} and game_id = {game_id}"
    cur.execute(sql)
    conn.commit()
    cur.close()

##############################################################
##############################################################


# conn = give_connection("dev")

# print(get_player_info(1, 4, conn_t))


# conn.close()


