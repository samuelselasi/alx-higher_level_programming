#!/usr/bin/python3
"""A script that lists states with name starting with N from hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """Function that connects to MySQL server on localhost at port 3306"""

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
