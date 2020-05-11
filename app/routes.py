from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
from app.cript import CriptSuit
from app.password import password


@app.route('/index', methods=['GET','POST'])
def index():
    #cript = CriptSuit().suite()
 #   try:
  #      mensagem = cript_suite.decrypt(b'gAAAAABeejhHHotXX41EGcq3z413lzKzpPYolrW4wbqEPMvLZwK1RPxAjg0ZYAVrhFXIVOUa2hQqMXXMa4hKVPYhukdWKoaI9Q==')
   # except:
    mensagem = password()
    return render_template('index.html',title="Cordeiro's DEV",mensagem = mensagem)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        password_provided = CriptSuit().registerKEY(form.password.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/teste')
def teste():
    user = {'username':'RodCordeiro'}
    dados = [{'titulo':'Teste','login': 'RodCordeiro','senha':'@C0rdeiro'},{'titulo':'Desenvolvimento','login':'cordeiro','senha':'master'},{'titulo':'MySQL','login':'cordeiro','senha':'@C0rdeiro'}]
    return render_template('teste.html',title="Cordeiro's DEV",user=user, info=dados)





@app.errorhandler(404)
def page_not_found(e):
    return render_template('erro.html'),404