#!/usr/bin/python3
"""This code shall list all states in db name start with n"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cr.fetchall() if state[1][0] == "N"]
    cr.close()
