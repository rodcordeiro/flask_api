# -*- coding: utf-8 -*-
import base64
import os

from app import app

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

app.config['DEBUG'] = True
app.run()
