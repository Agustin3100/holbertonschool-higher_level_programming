#!/usr/bin/python3
"""Filter states by user input."""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    name = argv[4]

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(name))
    states = cur.fetchall()
    for row in states:
        print(row)
    cur = cur.close()
    db = db.close()
