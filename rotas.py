# -*- coding: utf-8 -*-
#########################################################################
#                                                                       #
#                       Rodrigo Cordeiro                                #
#                                                                       #
#                GNU General Public License v3                          #
#                                                                       #
#########################################################################
# Arquivo que irá controlar as ações em cada rota

import flask
from flask import request, jsonify
import classes

class Rota:
    def __init__(self):
        self.__init__
        self.classes = classes.Controladores()

    def rotas(self,acao):
        if acao == "classe":
            return self.classes.classe1()
