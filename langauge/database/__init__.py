"""
Developer documentation - https://cx-oracle.readthedocs.io/
"""

import cx_Oracle

# Establish the database connection
with cx_Oracle.connect("username", "password", "connection_string") as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM TABLE_NAME')
    for row in cursor:
        print(row[0])
