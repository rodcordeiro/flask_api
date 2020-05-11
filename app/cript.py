####################################################
# -*- coding:utf-8 -*-
#Created by Rodrigo Cordeiro
#
####################################################
#
from app import app


import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CriptSuit:
	def __init__(self):
		self = self.__init__

	def registerKEY(self,password):
		password_provided = password
		password = password_provided.encode() # Convert to type bytes
		salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=salt,
			iterations=100000,
			backend=default_backend()
		)
		app.config['criptKEY'] = base64.urlsafe_b64encode(kdf.derive(password))
    
	def suite(self):
		suite = Fernet(app.config['criptKEY'])
		return suite

