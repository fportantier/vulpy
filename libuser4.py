import sqlite3
import re
from time import sleep

def login(username, password, **kwargs):

    conn = sqlite3.connect('users1.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password)).fetchone()

    if user:
        return user['username']
    else:
        sleep(5)
        return False


def userlist():

    conn = sqlite3.connect('users1.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    users = c.execute("SELECT * FROM users").fetchall()

    if not users:
        return []
    else:
        return [ user['username'] for user in users ]


def password_change(username, password):

    conn = sqlite3.connect('users1.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("UPDATE users SET password = ? WHERE username = ?", (password, username))
    conn.commit()

    return True


def password_complexity(password):

    if len(password) < 8:
        return False

    if len(re.findall(r'[a-z]', password)) < 1:
        return False

    if len(re.findall(r'[A-Z]', password)) < 1:
        return False

    if len(re.findall(r'[0-9]', password)) < 1:
        return False

    with open('bad-passwords.txt') as f:
        for p in f.read().split('\n'):
            if password == p:
                return False

    return True

