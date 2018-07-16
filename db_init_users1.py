import os
import sqlite3
#from passlib.hash import pbkdf2_sha256

def db_init():

    users = [
        ('admin', '123456'),
        ('john', 'password1'),
        ('tim', '123123123')
    ]

    conn = sqlite3.connect('users1.sqlite')
    c = conn.cursor()
    #c.execute("DROP TABLE users")
    c.execute("CREATE TABLE users (username text, password text)")

    for u,p in users:
        c.execute("INSERT INTO users (username, password) VALUES ('%s', '%s')" %(u, p))

    conn.commit()
    conn.close()


if __name__ == '__main__':

    try:
        os.remove('users1.sqlite')
    except FileNotFoundError:
        pass

    db_init()

