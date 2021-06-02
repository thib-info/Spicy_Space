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
    return render_template('index.html', reload = time.time())


@app.route('/api/user')
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

@app.route('/api/rendu', methods=['GET', 'POST'])
def rendu():
    a = int(request.args.get('a'))
    print(a)
    return jsonify({'resp':a})

@app.route("/connexion", methods=["GET", "POST"])
def login_page():
    # traitement de la requete ajax
    pass