import sqlite3
con = sqlite3.connect('topic_author_manager.db')
result = con.execute('SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id')
rows = result.fetchall()
for row in rows:
    print(row)
con.close()