import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'N7p-Byjb',
    database = 'db2',
)

connected = conn.is_connected()
print(connected)
if (not connected):
    conn.ping(True)

cur = conn.cursor()
cur.execute('select * from tb_index')
table = cur.fetchall()
print(table)

print("成功しました")
