import sqlite3

import flask
from flask import Blueprint, render_template, redirect, request, g, session, make_response, flash
import libuser
import libsession
import libmfa

mod_user = Blueprint('mod_user', __name__, template_folder='templates')


@mod_user.route('/login', methods=['GET', 'POST'])
def do_login():

    session.pop('username', None)

    if request.method == 'POST':

        username_input = request.form.get('username')
        password = request.form.get('password')
        otp = request.form.get('otp')
        if libuser.is_locked(username_input):
            flash("Account is locked due to too many attempts. Try again later.")
            return render_template('user.login.mfa.html')

        username = libuser.login(username_input, password)

        if not username:
            libuser.increment_failed_attempts(username_input)

            if libuser.get_failed_attempts(username_input) >= libuser.MAX_FAILED_ATTEMPTS:
                flask.flash("Exceeded Password attempts. Try again later.")
                libuser.lock_account(username_input)
            else:
                flash("Invalid Username or Password")
            return render_template('user.login.mfa.html')


        libuser.set_failed_attempts(username_input, 0)
        libuser.unlock_account(username_input)

        if libmfa.mfa_is_enabled(username):
            if not libmfa.mfa_validate(username, otp):
                flash("Invalid OTP");
                return render_template('user.login.mfa.html')

        response = make_response(redirect('/'))
        response = libsession.create(request=request, response=response, username=username)
        return response

    return render_template('user.login.mfa.html')


@mod_user.route('/create', methods=['GET', 'POST'])
def do_create():

    session.pop('username', None)

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('password')
        libuser.user_create(username, password)
        session['username'] = libuser.login(username, password)

        if session['username']:
            return redirect('/')

    return render_template('user.create.html')


@mod_user.route('/chpasswd', methods=['GET'])
def do_chpasswd_get():
    return render_template('user.chpasswd.html')


@mod_user.route('/chpasswd', methods=['POST'])
def do_chpasswd_post():

    if 'username' not in g.session:
        return redirect('/')

    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    new_password_again = request.form.get('new_password_again')

    if not libuser.login(g.session['username'], current_password):
        flash("Invalid current password")
        return render_template('user.chpasswd.html')

    if new_password != new_password_again:
        flash("The passwords don't match")
        return render_template('user.chpasswd.html')

    if not libuser.is_password_allowed(new_password):
        flash("The password don't comply our requirements, please, choose another one.")
        return render_template('user.chpasswd.html')

    libuser.password_set(g.session['username'], new_password)
    return redirect('/')
    flash("Password changed")

