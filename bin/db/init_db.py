import os 
import sqlite3

"""
Init the SQLite database
Intented to be run as a module (python -m bin.db.init_db) 
"""

os.chdir("./nga/filters")

con = sqlite3.connect("filters.db")

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS nationality;")
cur.execute("CREATE TABLE nationality(nationality)")

cur.execute("DROP TABLE IF EXISTS style;")
cur.execute("CREATE TABLE style(style)")

con.commit()

print("The filter database has been initialized.")