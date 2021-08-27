import sqlite3
con = sqlite3.connect('topic_author_manager.db')
name = input('이름 : ')
job = input('직업 : ')
sql = "INSERT INTO author(name, job) VALUES('"+name+"', '"+job+"')"
con.execute(sql)
con.commit()
con.close()