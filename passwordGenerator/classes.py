####################################################
# -*- coding:utf-8 -*-
#Created by Rodrigo Cordeiro
#
####################################################
#
from random import choice

special_characters=['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '.', ',', ';', '?', '{', '[', '}', ']', '^', '>', '<', ':']
numbers=["0","1","2","3","4","5","6","7","8","9"]
lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
all=numbers + special_characters + uppercase + lowercase


class Password:
    def __init__(self):
        self = self.__init__

    def pwdSize(self):
        size = choice(range(12))
        while size <=8:
            size = choice(range(12))
        return size

    def generate(self):
        passwd = ''.join([choice(all) for a in range(self.pwdSize())])
        return passwd

class Validacoes:
    def __init__(self,passwd):
        self.passwd = passwd


    def validaTamanho(self):
        pwd = self.passwd
        if len(pwd) > 8:
            return [len(pwd),len(pwd)*4,1]
        else:
            return False

    def validaMaiusculas(self):
        pwd = self.passwd
        chars = 0
        for char in pwd:
            if char in uppercase:
                chars += 1
        if chars > 0:
            return [chars,(len(pwd) - chars)*2,1]
        else:
            return False

    def validaMinusculas(self):
        pwd = self.passwd
        chars = 0
        for char in pwd:
            if char in lowercase:
                chars += 1
        if chars > 0:
            return [len(pwd),(len(pwd) - chars)*2]
        else:
            return False

    def validaNumeros(self):
        pwd = self.passwd
        chars = 0
        for char in pwd:
            if char in numbers:
                chars += 1
        if chars > 0:
            return [chars,chars *4]
        else:
            return False

    def validaCaracteres(self):
        pwd = self.passwd
        chars = 0
        for char in pwd:
            if char in special_characters:
                chars += 1
        if chars > 0:
            return [chars,chars *6]
        else:
            return False

    def validaNumORChar(self):
        pwd = self.passwd
        ok = 0
        if self.validaNumeros() != False:
            ok +=1
        if self.validaCaracteres() != False:
            ok +=1
        return [ok,ok*2]

    def duplicate_count(self):
        pwd = self.passwd
        count = ''
        for a in pwd.lower():
            if pwd.lower().count(a) > 1:
                count = count + a
        return [len(count),-len(count)]

    def validate(self):
        pwd = self.passwd
        pontuacao = 0
        if self.validaMaiusculas() != False:
            pontuacao += self.validaMaiusculas()[1]
        else: return False
        if self.validaMinusculas() != False:
            pontuacao += self.validaMinusculas()[1]
        else: return False
        if self.validaNumeros() != False:
            pontuacao += self.validaNumeros()[1]
        else: return False
        if self.validaCaracteres() != False:
            pontuacao += self.validaCaracteres()[1]
        else: return False
        if self.validaTamanho() != False:
            pontuacao += self.validaTamanho()[1]
        if self.validaNumORChar() != False:
            pontuacao += self.validaNumORChar()[1]
        if self.duplicate_count() != False:
            pontuacao += self.duplicate_count()[1]
        else: return False

        valores = "\nMaiusculas: {}, +{}".format(self.validaMaiusculas()[0],self.validaMaiusculas()[1])
        valores += "\nMinusculas: {}, +{}".format(self.validaMinusculas()[0],self.validaMinusculas()[1])
        valores += "\nNumeros: {}, +{}".format(self.validaNumeros()[0],self.validaNumeros()[1])
        valores += "\nCaracteres especiais: {}, +{}".format(self.validaCaracteres()[0],self.validaCaracteres()[1])
        valores += "\nNúmeros ou caracteres especiais: {}, +{}".format(self.validaNumORChar()[0],self.validaNumORChar()[1])
        valores += "\nTamanho: {}, {}".format(self.validaTamanho()[0],self.validaTamanho()[1])
        return [pontuacao,valores]