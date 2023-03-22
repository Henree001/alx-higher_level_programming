#!/usr/bin/python3
"""Takes in the name of a state as an argument and
lists all cities of that state
"""


import MySQLdb
import sys

if __name__ == "__main__":

    connect = MySQLdb.connect(
        host='localhost',
        port=3306,
        database=sys.argv[3],
        user=sys.argv[1],
        passwd=sys.argv[2])
    cur = connect.cursor()
    cur.execute('SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE name = %s) \
                ORDER BY cities.id', (sys.argv[4],))
    rows = cur.fetchall()
    for i in range(len(rows)):
        separator = ', '
        if i == len(rows) - 1:
            separator = ''
        print(rows[i][0], end=separator)
    print()
