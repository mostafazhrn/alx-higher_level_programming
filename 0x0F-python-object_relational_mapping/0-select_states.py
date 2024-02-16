#!/usr/bin/python3
""" This code shall list all states from hbtn_usa db"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states")
    [print(state) for state in cr.fetchall()]
    cr.close()
