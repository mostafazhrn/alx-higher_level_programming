#!/usr/bin/python3
""" This script shall display all values of table that match arg"""
import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    """ This shall access the db and get states"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
               .format(sys.argv[4]))
    [print(state) for state in cr.fetchall()]
    cr.close()
