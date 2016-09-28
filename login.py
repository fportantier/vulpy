from flask import Flask, render_template, request, url_for, make_response, g
from lib.db import db_init
from lib.auth import auth
import base64

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
        response = make_response("Success")
        response.set_cookie('session', value=base64.b64encode(user.encode()))
    else:
        response = make_response("Bad User/Password")

    return response


@app.route('/validate', methods=['GET'])
def validate():

    cookie = request.cookies.get('session')

    if not cookie:
        return "Invalid"

    decoded = base64.b64decode(cookie).decode()
    return "Valid for user: %s" %(decoded)



if __name__ == '__main__':
    app.run(port=8000)

