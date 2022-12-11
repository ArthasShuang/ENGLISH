import sqlite3
conn = sqlite3.connect('单词数据库.db')
#buıld connector
cursor = conn.cursor()
cursor.execute('select * from words where chapter = 1')
data = cursor.fetchall()
print(data)
