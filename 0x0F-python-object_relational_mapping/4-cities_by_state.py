#!/usr/bin/python3
""" This code shall list all cities from the db """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id
    ORDER BY cities.id""")
    [print(city) for city in cr.fetchall()]
    cr.close()
