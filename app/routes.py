# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')



@app.errorhandler(404)
def page_not_found(e):
    return """<pre>def NaoEntendi():
    print(Que?!)
    return "Pra onde tu quer ir jovem?"
    </pre>

<a href='/index'> Voltar </a>
    """,404
