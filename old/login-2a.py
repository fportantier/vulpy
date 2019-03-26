#!/usr/bin/env python3

import sys
import sqlite3


if len(sys.argv) != 3:
    print("usage: {} username password".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

conn = sqlite3.connect('users2.sqlite')
conn.set_trace_callback(print)
conn.row_factory = sqlite3.Row
c = conn.cursor()

user = c.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password)).fetchone()

if user:
    if user['failures'] <= 5:
        c.execute("UPDATE users SET failures = 0 WHERE username = ?", (username,))
        conn.commit()

        print("login ok")
        sys.exit(0)

    else:
        print("user blocked")
        sys.exit(2)

else:
    c.execute("UPDATE users SET failures = failures + 1 WHERE username = ?", (username,))
    conn.commit()

    print("login failed")
    sys.exit(1)


