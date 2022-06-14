from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('database.db')

with open('./database/schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)", 
            ('Frist Post', 'content for the fist post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)", 
            ('Second Post', 'content for the second post'))

connection.commit()
connection.close()