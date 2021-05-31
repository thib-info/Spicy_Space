import sqlite3 as sq
import json



def load_creds(type_conn):
    if type_conn == 'production':
        with open

def give_connection(type_conn):
    if type_conn == 'production':
        return sqlite3.connect('../db/production.db')
    elif type_conn == 'dev':
        return sqlite3.connect('../db/development.db')





