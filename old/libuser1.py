import sqlite3

# SQL Injection vulnerability on username/password parameters
def login(username, password, **kwargs):

    conn = sqlite3.connect('users1.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute("SELECT * FROM users WHERE username = '{}' and password = '{}'".format(username, password)).fetchone()

    if user:
        return user['username']
    else:
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

    c.execute("UPDATE users SET password = '{}' WHERE username = '{}'".format(password, username))
    conn.commit()

    return True


def password_complexity(password):
    return True

