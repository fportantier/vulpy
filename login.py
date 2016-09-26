from flask import Flask, render_template, request, url_for
from lib.db import db_init
from lib.auth import auth
import sqlite3

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def login_get():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def login_post():

    db_init()

    user=request.form['user']
    password=request.form['password']

    if auth(user, password):
        return "Success!"
    else:
        return "Bad User/Password"


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=int("8000"))

