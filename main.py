# -*- coding: utf-8 -*-
#########################################################################
#                                                                       #
#                       Rodrigo Cordeiro                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################
# Arquivo principal, contém as rotas.
import flask
from flask import request, jsonify
import rotas

app = flask.Flask(__name__)
app.config["DEBUG"] = True


rotas = rotas.Rota()
@app.route('/',methods=['GET','POST'])
def home():
    return "<h1>Iniciando desenvolvimento</h1>"

@app.route('/classe',methods=['GET','POST'])
def classe():
    return rotas.rotas()


app.run()
