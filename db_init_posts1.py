import os
import sqlite3
#from passlib.hash import pbkdf2_sha256

def db_init():

    conn = sqlite3.connect('posts1.sqlite')
    c = conn.cursor()
    #c.execute("DROP TABLE users")
    c.execute("CREATE TABLE posts (date date, username text, text text)")

    #for u,p in users:
    #    c.execute("INSERT INTO users (username, password) VALUES ('%s', '%s')" %(u, p))

    conn.commit()
    conn.close()


if __name__ == '__main__':

    try:
        os.remove('posts1.sqlite')
    except FileNotFoundError:
        pass

    db_init()

