#!/usr/bin/env python3

import sys
import sqlite3


if len(sys.argv) != 2:
    print("usage: {} username".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]

conn = sqlite3.connect('users2.sqlite')
conn.set_trace_callback(print)
conn.row_factory = sqlite3.Row
c = conn.cursor()


user = c.execute("UPDATE users SET failures = 0 WHERE username = ?", (username,))
conn.commit()
sys.exit(0)

