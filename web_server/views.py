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
    map={"systems": [{"name": "syst_nul", "pos": [1491, 204]}, {"name": "syst_nul", "pos": [1492, 231]}, {"name": "syst_nul", "pos": [1411, 303]}, {"name": "syst_nul", "pos": [1405, 225]}, {"name": "syst_nul", "pos": [1450, 227]}, {"name": "syst_nul", "pos": [1527, 331]}, {"name": "syst_nul", "pos": [1433, 266]}, {"name": "syst_nul", "pos": [1452, 245]}, {"name": "syst_nul", "pos": [1517, 246]}, {"name": "syst_nul", "pos": [1524, 295]}, {"name": "syst_nul", "pos": [1423, 247]}, {"name": "syst_nul", "pos": [1486, 223]}, {"name": "syst_nul", "pos": [1480, 249]}, {"name": "syst_nul", "pos": [1425, 287]}, {"name": "syst_nul", "pos": [1459, 295]}, {"name": "syst_nul", "pos": [1467, 237]}, {"name": "syst_nul", "pos": [1457, 256]}, {"name": "syst_nul", "pos": [1412, 229]}, {"name": "syst_nul", "pos": [1454, 304]}, {"name": "syst_nul", "pos": [1419, 291]}, {"name": "syst_nul", "pos": [962, 88]}, {"name": "syst_nul", "pos": [974, 90]}, {"name": "syst_nul", "pos": [933, 103]}, {"name": "syst_nul", "pos": [954, 73]}, {"name": "syst_nul", "pos": [1005, 73]}, {"name": "syst_nul", "pos": [920, 101]}, {"name": "syst_nul", "pos": [910, 40]}, {"name": "syst_nul", "pos": [969, 57]}, {"name": "syst_nul", "pos": [910, 139]}, {"name": "syst_nul", "pos": [933, 84]}, {"name": "syst_nul", "pos": [1027, 1256]}, {"name": "syst_nul", "pos": [1028, 1247]}, {"name": "syst_nul", "pos": [1032, 1145]}, {"name": "syst_nul", "pos": [974, 1186]}, {"name": "syst_nul", "pos": [1034, 1150]}, {"name": "syst_nul", "pos": [1001, 1176]}, {"name": "syst_nul", "pos": [1063, 1229]}, {"name": "syst_nul", "pos": [983, 1254]}, {"name": "syst_nul", "pos": [957, 1175]}, {"name": "syst_nul", "pos": [1059, 1155]}, {"name": "syst_nul", "pos": [1121, 1892]}, {"name": "syst_nul", "pos": [1142, 1836]}, {"name": "syst_nul", "pos": [1100, 1879]}, {"name": "syst_nul", "pos": [1152, 1849]}, {"name": "syst_nul", "pos": [1142, 1843]}, {"name": "syst_nul", "pos": [1086, 1873]}, {"name": "syst_nul", "pos": [1150, 1874]}, {"name": "syst_nul", "pos": [1074, 1876]}, {"name": "syst_nul", "pos": [1143, 1862]}, {"name": "syst_nul", "pos": [1157, 1819]}, {"name": "syst_nul", "pos": [1133, 1841]}, {"name": "syst_nul", "pos": [1089, 1904]}, {"name": "syst_nul", "pos": [1130, 1859]}, {"name": "syst_nul", "pos": [1099, 1822]}, {"name": "syst_nul", "pos": [1080, 1848]}, {"name": "syst_nul", "pos": [1141, 1876]}, {"name": "syst_nul", "pos": [1115, 1859]}, {"name": "syst_nul", "pos": [151, 263]}, {"name": "syst_nul", "pos": [227, 281]}, {"name": "syst_nul", "pos": [208, 289]}, {"name": "syst_nul", "pos": [150, 285]}, {"name": "syst_nul", "pos": [140, 241]}, {"name": "syst_nul", "pos": [162, 241]}, {"name": "syst_nul", "pos": [215, 266]}, {"name": "syst_nul", "pos": [149, 237]}, {"name": "syst_nul", "pos": [175, 230]}, {"name": "syst_nul", "pos": [141, 296]}, {"name": "syst_nul", "pos": [193, 236]}, {"name": "syst_nul", "pos": [150, 317]}, {"name": "syst_nul", "pos": [144, 299]}, {"name": "syst_nul", "pos": [189, 293]}, {"name": "syst_nul", "pos": [1331, 1339]}, {"name": "syst_nul", "pos": [1382, 1423]}, {"name": "syst_nul", "pos": [1408, 1408]}, {"name": "syst_nul", "pos": [1342, 1426]}, {"name": "syst_nul", "pos": [1343, 1389]}, {"name": "syst_nul", "pos": [1373, 1379]}, {"name": "syst_nul", "pos": [1412, 1399]}, {"name": "syst_nul", "pos": [1382, 1342]}, {"name": "syst_nul", "pos": [1278, 1330]}, {"name": "syst_nul", "pos": [1281, 1388]}, {"name": "syst_nul", "pos": [1191, 1982]}, {"name": "syst_nul", "pos": [1127, 1962]}, {"name": "syst_nul", "pos": [1213, 1907]}, {"name": "syst_nul", "pos": [1176, 1944]}, {"name": "syst_nul", "pos": [1133, 1936]}, {"name": "syst_nul", "pos": [1200, 1989]}, {"name": "syst_nul", "pos": [1134, 1987]}, {"name": "syst_nul", "pos": [1211, 1942]}, {"name": "syst_nul", "pos": [1195, 1971]}, {"name": "syst_nul", "pos": [1203, 1938]}, {"name": "syst_nul", "pos": [1375, 1592]}, {"name": "syst_nul", "pos": [1440, 1666]}, {"name": "syst_nul", "pos": [1364, 1602]}, {"name": "syst_nul", "pos": [1441, 1649]}, {"name": "syst_nul", "pos": [1387, 1648]}, {"name": "syst_nul", "pos": [1365, 1636]}, {"name": "syst_nul", "pos": [1441, 1630]}, {"name": "syst_nul", "pos": [1359, 1586]}, {"name": "syst_nul", "pos": [1393, 1637]}, {"name": "syst_nul", "pos": [1420, 1652]}, {"name": "syst_nul", "pos": [1437, 1616]}, {"name": "syst_nul", "pos": [332, 164]}, {"name": "syst_nul", "pos": [348, 147]}, {"name": "syst_nul", "pos": [310, 232]}, {"name": "syst_nul", "pos": [344, 178]}, {"name": "syst_nul", "pos": [295, 161]}, {"name": "syst_nul", "pos": [312, 133]}, {"name": "syst_nul", "pos": [364, 227]}, {"name": "syst_nul", "pos": [308, 223]}, {"name": "syst_nul", "pos": [387, 178]}, {"name": "syst_nul", "pos": [338, 161]}, {"name": "syst_nul", "pos": [301, 191]}, {"name": "syst_nul", "pos": [326, 223]}, {"name": "syst_nul", "pos": [286, 172]}, {"name": "syst_nul", "pos": [383, 163]}, {"name": "syst_nul", "pos": [318, 160]}, {"name": "syst_nul", "pos": [434, 250]}, {"name": "syst_nul", "pos": [462, 215]}, {"name": "syst_nul", "pos": [421, 256]}, {"name": "syst_nul", "pos": [405, 245]}, {"name": "syst_nul", "pos": [448, 233]}, {"name": "syst_nul", "pos": [458, 200]}, {"name": "syst_nul", "pos": [429, 234]}, {"name": "syst_nul", "pos": [469, 198]}, {"name": "syst_nul", "pos": [436, 209]}, {"name": "syst_nul", "pos": [433, 191]}, {"name": "syst_nul", "pos": [438, 240]}, {"name": "syst_nul", "pos": [401, 219]}, {"name": "syst_nul", "pos": [429, 188]}, {"name": "syst_nul", "pos": [457, 232]}, {"name": "syst_nul", "pos": [405, 191]}, {"name": "syst_nul", "pos": [437, 227]}, {"name": "syst_nul", "pos": [427, 214]}, {"name": "syst_nul", "pos": [440, 209]}, {"name": "syst_nul", "pos": [461, 258]}, {"name": "syst_nul", "pos": [409, 489]}, {"name": "syst_nul", "pos": [387, 533]}, {"name": "syst_nul", "pos": [408, 527]}, {"name": "syst_nul", "pos": [366, 520]}, {"name": "syst_nul", "pos": [381, 444]}, {"name": "syst_nul", "pos": [353, 490]}, {"name": "syst_nul", "pos": [351, 467]}, {"name": "syst_nul", "pos": [419, 445]}, {"name": "syst_nul", "pos": [367, 514]}, {"name": "syst_nul", "pos": [359, 461]}], "sectors": [{"name": "nom_nul", "pos": [1470, 271]}, {"name": "nom_nul", "pos": [958, 90]}, {"name": "nom_nul", "pos": [1009, 1201]}, {"name": "nom_nul", "pos": [1113, 1859]}, {"name": "nom_nul", "pos": [186, 271]}, {"name": "nom_nul", "pos": [1346, 1397]}, {"name": "nom_nul", "pos": [1167, 1947]}, {"name": "nom_nul", "pos": [1402, 1629]}, {"name": "nom_nul", "pos": [341, 182]}, {"name": "nom_nul", "pos": [431, 225]}, {"name": "nom_nul", "pos": [376, 484]}], "links": [{"start": [1491, 204], "end": [1492, 231]}, {"start": [1492, 231], "end": [1411, 303]}, {"start": [1492, 231], "end": [1405, 225]}, {"start": [1492, 231], "end": [1450, 227]}, {"start": [1492, 231], "end": [1524, 295]}, {"start": [1492, 231], "end": [1486, 223]}, {"start": [1411, 303], "end": [1405, 225]}, {"start": [1411, 303], "end": [1419, 291]}, {"start": [1405, 225], "end": [1527, 331]}, {"start": [1405, 225], "end": [1423, 247]}, {"start": [1450, 227], "end": [1452, 245]}, {"start": [1527, 331], "end": [1423, 247]}, {"start": [1527, 331], "end": [1425, 287]}, {"start": [1527, 331], "end": [1419, 291]}, {"start": [1433, 266], "end": [1459, 295]}, {"start": [1452, 245], "end": [1450, 227]}, {"start": [1452, 245], "end": [1524, 295]}, {"start": [1452, 245], "end": [1412, 229]}, {"start": [1517, 246], "end": [1492, 231]}, {"start": [1517, 246], "end": [1450, 227]}, {"start": [1517, 246], "end": [1486, 223]}, {"start": [1517, 246], "end": [1425, 287]}, {"start": [1517, 246], "end": [1459, 295]}, {"start": [1517, 246], "end": [1412, 229]}, {"start": [1524, 295], "end": [1411, 303]}, {"start": [1524, 295], "end": [1527, 331]}, {"start": [1524, 295], "end": [1452, 245]}, {"start": [1524, 295], "end": [1419, 291]}, {"start": [1423, 247], "end": [1411, 303]}, {"start": [1423, 247], "end": [1405, 225]}, {"start": [1423, 247], "end": [1527, 331]}, {"start": [1423, 247], "end": [933, 103]}, {"start": [1486, 223], "end": [1491, 204]}, {"start": [1486, 223], "end": [1450, 227]}, {"start": [1486, 223], "end": [1433, 266]}, {"start": [1486, 223], "end": [1524, 295]}, {"start": [1480, 249], "end": [1492, 231]}, {"start": [1480, 249], "end": [1527, 331]}, {"start": [1480, 249], "end": [1423, 247]}, {"start": [1480, 249], "end": [1486, 223]}, {"start": [1480, 249], "end": [1480, 249]}, {"start": [1425, 287], "end": [1454, 304]}, {"start": [1467, 237], "end": [1457, 256]}, {"start": [1467, 237], "end": [1005, 73]}, {"start": [1457, 256], "end": [1459, 295]}, {"start": [1457, 256], "end": [1419, 291]}, {"start": [1412, 229], "end": [1433, 266]}, {"start": [1412, 229], "end": [1486, 223]}, {"start": [1412, 229], "end": [1459, 295]}, {"start": [1412, 229], "end": [920, 101]}, {"start": [1454, 304], "end": [1467, 237]}, {"start": [1419, 291], "end": [1524, 295]}, {"start": [1419, 291], "end": [1459, 295]}, {"start": [962, 88], "end": [954, 73]}, {"start": [962, 88], "end": [920, 101]}, {"start": [974, 90], "end": [1454, 304]}, {"start": [933, 103], "end": [1517, 246]}, {"start": [933, 103], "end": [1425, 287]}, {"start": [933, 103], "end": [969, 57]}, {"start": [954, 73], "end": [1457, 256]}, {"start": [954, 73], "end": [974, 90]}, {"start": [954, 73], "end": [920, 101]}, {"start": [1005, 73], "end": [1425, 287]}, {"start": [1005, 73], "end": [920, 101]}, {"start": [920, 101], "end": [1412, 229]}, {"start": [920, 101], "end": [1005, 73]}, {"start": [910, 40], "end": [1412, 229]}, {"start": [969, 57], "end": [1423, 247]}]}
    return jsonify(map)