from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from functools import wraps

import time
import json
from datetime import datetime, timedelta


from bdd import give_connection


app = Flask(__name__)
app.static_folder = "../web_docs/data"
app.template_folder = "../web_docs/templates"
app.config.from_object('config')

############################
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if True:
            return f(*args, **kwargs)

        else:
            print("on redirige vers l'accueil")
    
    return wrap

############################


@app.route('/')
def main():
    return render_template('indexPyt.html', reload = time.time())


@app.route('/api/user', methods=['POST'])
def api_user():
    info = {
        "username":"test1",
        "games":{
            "test1":{
                "activated":True,
                "last_played":'2020-12-01',
            },
            "test2":{
                "activated":False,
                "last_played":'2020-12-01',
            },
        },
        "info_nulle":["naze", 1]
    }

    return jsonify(info)

@app.route('/api/rendu', methods=['POST'])
def rendu():
    a = int(request.form.get('a'))
    print(a)
    return jsonify({'resp':a})

@app.route("/connexion", methods=["GET", "POST"])
def login_page():
    # traitement de la requete ajax
    pass

@app.route("/map", methods=["POST"])
def mapSend():
    with open("../game_data/map.json") as f:
        map=json.load(f)
    return jsonify(map)

@app.route("/treeTech", methods=["POST"])
def treeTechSend():
    idTech = request.form.get('idTech')
    if(idTech != None):
        return True
    else:
        with open("../config/base_tech.json") as f:
            treeTech=json.load(f)
        return jsonify(treeTech)