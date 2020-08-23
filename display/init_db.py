import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, category, content) VALUES (?, ?, ?)",
             ('First_News', 'ADS','The government is cool')
             )




connection.commit()
connection.close()