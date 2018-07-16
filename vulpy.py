#!/usr/bin/env python3

from flask import Flask, g, redirect, request
from mod_hello import mod_hello
from mod_user import mod_user
from mod_posts import mod_posts
from mod_mfa import mod_mfa
import libsession

app = Flask('vulpy')
#app.config.from_mapping(config)
app.config['SECRET_KEY'] = 'aaaaaaa'
#csrf.init_app(app)

#login_manager.init_app(app)

app.register_blueprint(mod_hello, url_prefix='/hello')
app.register_blueprint(mod_user, url_prefix='/user')
app.register_blueprint(mod_posts, url_prefix='/posts')
app.register_blueprint(mod_mfa, url_prefix='/mfa')


@app.route('/')
def do_home():
    return redirect('/posts')

@app.before_request
def before_request():
    g.session = libsession.load(request)
    #print(g.session)
    #if 'logged_in' not in session and request.endpoint != 'login':
    #    return redirect(url_for('login'))


app.run(debug=True)


