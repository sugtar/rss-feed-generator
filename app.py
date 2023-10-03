import sqlite3

dbname = 'data.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute('SELECT * FROM test')
print(cur.fetchall())
cur.close()
conn.close()