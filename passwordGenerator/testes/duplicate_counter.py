# -*- coding: utf-8 -*-
# Author: Rodrigo Cordeiro
from classes import Password, Validacoes

special_characters=['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '.', ',', ';', '?', '{', '[', '}', ']', '^', '>', '<', ':']
numbers=["0","1","2","3","4","5","6","7","8","9"]
lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def duplicate_count(text):
	print(text)
	count = {'special' : 0,
	'upper' : 0,
	'lower' :0,
	'number' : 0}
	for char in text:
		if char in special_characters:
			count['special'] += 1
		elif char in lowercase:
			count['lower'] +=1
		elif char in uppercase:
			count['upper'] +=1
		elif char in numbers:
			count['number'] +=1
	for value in count.values():
		if value >=4: return False
	return True


def password():
    passwd = Password().generate()
    validate = Validacoes(passwd).validate()
    if validate != False:
    	print(passwd)
    	return passwd
    else:
        password()
teste = password()
print(duplicate_count(teste),teste)