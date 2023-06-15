#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """Function that connects to MySQL server on localhost at port 3306"""

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY %(name)s \
                 ORDER BY states.id ASC", {'name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
