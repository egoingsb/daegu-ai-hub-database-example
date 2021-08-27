import sqlite3
con = sqlite3.connect('topic_manager.db')
title = input('제목 : ')
body = input('본문 : ')
sql = "INSERT INTO topic(title, body) VALUES('"+title+"', '"+body+"')"
con.execute(sql)
con.commit()
con.close()