import sqlite3

conn = sqlite3.connect("c:/dev/inmetro table/source/banco/banco.db")
cursor = conn.execute("SELECT * FROM balanca")
rows = cursor.fetchall()