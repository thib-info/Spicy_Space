from flask import Flask, request, render_template, redirect, url_for, session
from functools import wraps


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
        return f(*args, **kwargs)

        else:
            print("on redirige vers l'accueil")
    
    return wrap

############################


@app.route("/connexion", methods=["GET", "POST"])
def login_page():
    # traitement de la requete ajax