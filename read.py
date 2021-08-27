import sqlite3
con = sqlite3.connect('topic_manager.db')
result = con.execute('SELECT * FROM topic')
rows = result.fetchall()
for row in rows:
    print(row)
con.close()