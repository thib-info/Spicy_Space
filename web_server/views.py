from flask import Flask, jsonify, request, render_template, redirect, url_for, session, flash
from functools import wraps

import time
import json
from datetime import datetime, timedelta


from bdd import give_connection
from bdd import add_user, get_user_id, compare_passw

app = Flask(__name__)
app.static_folder = "../web_docs/data"
app.template_folder = "../web_docs/templates"
app.config.from_object('config')


bdd_con = 'dev'

############################
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'connected' in session and session['connected']:
            print(session["user_id"])
            return f(*args, **kwargs)

        else:
            flash('vous devez etre connecté')
            return redirect(url_for('connexion'))
    
    return wrap

############################


@app.route('/')
@login_required
def main():
    session['connected'] = False
    return render_template('indexPyt.html', reload = time.time())


@app.route('/connexion', methods=['GET','POST'])
def connexion():
    
    if request.method == 'POST':
        pseudo = request.form.get('pseudo')
        passwd = request.form.get('password')
        if pseudo == None or passwd == None:
            flash("veuillez remplir le formulaire")
            return render_template('connexion_pyt.html')

        user_id = get_user_id(pseudo, bdd_con)
        if user_id == None:
            add_user(pseudo, passwd, bdd_con)
            session['connected'] = True
            session["user_id"] = get_user_id(pseudo, bdd_con)
            flash('ok !')
            return redirect(url_for('main'))

        if compare_passw(pseudo, passwd, bdd_con):
            session['connected'] = True
            session["user_id"] = get_user_id(pseudo, bdd_con)
            flash('connexion !')
            return redirect(url_for('main'))

        flash('mauvais couple id/password')
        return render_template('connexion_pyt.html')



        

    else:
        return render_template('connexion_pyt.html')



   


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
    pass