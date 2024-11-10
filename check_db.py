import sqlite3

conn = sqlite3.connect('med_calendar.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM event')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
