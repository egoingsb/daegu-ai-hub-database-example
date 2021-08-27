import sqlite3
con = sqlite3.connect('topic_author_manager.db')
result = con.execute('SELECT * FROM author')
rows = result.fetchall()
for row in rows:
    print(row)
con.close()