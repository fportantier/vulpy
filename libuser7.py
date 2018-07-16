import sqlite3
import binascii
import hashlib
import re
from time import sleep

def login(username, password, **kwargs):

    conn = sqlite3.connect('users1.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if not user:
        sleep(5)
        return False

    # 64 = SHA256, 128 = Scrypt
    if len(user['password']) == 64:
        if binascii.hexlify(hashlib.sha256(password.encode()).digest()).decode() == user['password']:
            return username
        else:
            print('SHA256 does not validate')
            sleep(5)
            return False
    elif user['password'] == password:
        return username

    print('Plain Password does not validate')
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

    hashed_password = binascii.hexlify(hashlib.sha256(password.encode()).digest()).decode()
    print('Changing password to', hashed_password)
    c.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
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

    return True

