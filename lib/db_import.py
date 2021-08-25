import sqlite3

connection = sqlite3.connect("../db.sqlite3")

cursor = connection.cursor()

sql_file = open("sample.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

for row in cursor.execute("SELECT * FROM results_states"):
    print(row)
