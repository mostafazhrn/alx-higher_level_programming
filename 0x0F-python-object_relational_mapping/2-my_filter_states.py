#!/usr/bin/python3
# This script shall display all values of table that match arg
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
               (sys.argv[4],))
    [print(state) for state in cr.fetchall()]
    cr.close()
