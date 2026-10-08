import sqlite3
import libuser


def login(username, password):
    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    user = c.execute(query, (username, password)).fetchone()

    conn.close()

    if user:
        return user['username']
    else:
        return False


def create(username, password):
    conn = sqlite3.connect('db_users.sqlite')
    c = conn.cursor()

    query = """
        INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret)
        VALUES (?, ?, ?, ?, ?)
    """
    c.execute(query, (username, password, 0, 0, ''))

    conn.commit()
    conn.close()


def userlist():
    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    users = c.execute("SELECT * FROM users").fetchall()

    conn.close()

    if not users:
        return []
    else:
        return [user['username'] for user in users]


def password_change(username, password):
    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    query = "UPDATE users SET password = ? WHERE username = ?"
    c.execute(query, (password, username))
    conn.commit()
    conn.close()

    return True


def password_complexity(password):
    return True