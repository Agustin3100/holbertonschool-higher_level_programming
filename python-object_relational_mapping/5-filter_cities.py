#!/usr/bin/python3
"""All cities by state."""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    name = argv[4]

    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities LEFT JOIN states
                ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (name,))
    cities = cur.fetchall()
    print(", ".join([city_name for city in cities for city_name in city]))
