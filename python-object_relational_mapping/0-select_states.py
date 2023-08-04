#!/usr/bin/python3

import sys
import MySQLdb


def list_states(username, password, database_name):
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()

    try:

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
