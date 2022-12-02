import os
import sqlite3

os.chdir("./nga/filters")

con = sqlite3.connect("filters.db")
cur = con.cursor()

print("Values for filter 'nationality' : ")
print(cur.execute("SELECT * from nationality").fetchall())

print('\n')

print("Values for filter 'style' : ")
print(cur.execute("SELECT * from style").fetchall())