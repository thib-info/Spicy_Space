from flask import Flask, jsonify, request, render_template, redirect, url_for, session, flash, send_file, g
from functools import wraps

import time
import json
from datetime import datetime, timedelta
import os


from bdd import give_connection
from bdd import add_user, get_user_id, compare_passw


from game_utils import game, create_game, join_game


from backend import list_files, find_file

app = Flask(__name__)
app.static_folder = "../web_docs/data"
app.template_folder = "../web_docs/templates"
app.config.from_object('config')


sg_a = create_game()



bdd_con = 'dev'

############################
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'connected' in session and session['connected']:
            return f(*args, **kwargs)

        else:
            flash('vous devez etre connecté')
            return redirect(url_for('connexion'))
    
    return wrap

############################


@app.route('/')
@login_required
def main():
    if sg_a.get_player(session["user_id"]) == -1:
        join_game(sg_a, session["user_id"], session["pseudo"])
    return render_template('indexPyt.html', reload = time.time())



@app.route('/regen')
@login_required
def regen():
    global sg_a
    sg_a = create_game()
    return redirect(url_for('main'))

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
            session["pseudo"] = pseudo
            flash('ok !')
            return redirect(url_for('main'))

        if compare_passw(pseudo, passwd, bdd_con):
            session['connected'] = True
            session["user_id"] = get_user_id(pseudo, bdd_con)
            session["pseudo"] = pseudo
            flash('connexion !')
            return redirect(url_for('main'))

        flash('mauvais couple id/password')
        return render_template('connexion_pyt.html')
    else:
        return render_template('connexion_pyt.html')


@app.route('/deco')
@login_required
def deco():
    session['connected'] = False
    session['user_id'] = - 1

    return redirect(url_for('main'))
    



@app.route("/map", methods=[ "POST"])
def mapSend():
    return jsonify(sg_a.map.export_info())


@app.route("/player_info", methods=["GET", "POST"])
def send_p_info():
    return jsonify(sg_a.to_front(session["user_id"]))

@app.route("/treeTech", methods=["POST"])
def treeTechSend():
    idTech = request.form.get('idTech')
    if(idTech != None):
        return True
    else:
        with open("../config/base_tech.json") as f:
            treeTech=json.load(f)
        return jsonify(treeTech)




@app.route("/get_img/<name>")
def give_img(name):
    path = os.path.join(app.static_folder, find_file(list_files(app.static_folder), name))
    print(path)

    if path != None:
        if os.path.isfile(path):
            return send_file(path, mimetype='image/gif')

    return send_file(app.static_folder + "/images/error.jpg" , mimetype='image/gif')

@app.route('/api/user', methods=['POST'])
def api_user():
    return jsonify({})
