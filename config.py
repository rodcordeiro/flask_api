import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'O6OB9p2AZA7jsV4dNPtpzWVWuERr3zitwSZ3wldC_H0='