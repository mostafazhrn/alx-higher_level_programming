#!/usr/bin/python3
""" This code shall list all states from database """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id",
               (sys.argv[4],))
    [print(state) for state in cr.fetchall()]
    cr.close()
