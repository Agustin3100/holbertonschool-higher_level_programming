#!/usr/bin/python3
"""Get all states."""
import MySQLdb
from sys import argv

db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id")
states = cur.fetchall()
for state in states:
    print(state)
cur = cur.close()
db.close()
