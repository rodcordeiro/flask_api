# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        print(form.password.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)



@app.errorhandler(404)
def page_not_found(e):
    return """<pre>def NaoEntendi():
    print(Que?!)
    return "Pra onde tu quer ir jovem?"
    </pre>

<a href='/index'> Voltar </a>
    """,404
