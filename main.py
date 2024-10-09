import sqlite3

conn = sqlite3.connect('exemple.db')
cur = conn.cursor()
# cur.execute('''
#
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL
# );
# 
# ''')
# conn.commit()
# cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Алексей', 25))
# cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Игорь', 36))
# conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
