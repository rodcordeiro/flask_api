####################################################
# -*- coding:utf-8 -*-
#Created by Rodrigo Cordeiro
#
####################################################
#
from classes import Password, Validacoes

import sys
argumentos = sys.argv


def password():
    passwd = Password().generate()
    validate = Validacoes(passwd).validate()
    if validate != False:
        if "-v" in argumentos:
            print("Generating Password")
            print('='*10+'\n'+passwd)
            print(validate[1])
            print("\nPontuação: {}".format(validate[0]))
        else:
        	print(passwd)
        	return passwd
    else:
        password()

password()