import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'N7p-Byjb',
    #database = 'db2',
)
cursor=conn.cursor()

cursor.execute("USE test_db2")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS fruits_table(
                id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                fruits VARCHAR(32),
                value INT);""")

conn.commit()

# データを挿入
insert_fruit = "INSERT INTO fruits_table (fruits, value) VALUES (%s, %s);"

fruit_list = [
    ("apple", 100),
    ("orange", 80),
    ("melon", 500),
    ("pineapple", 700)
]

for fruit in fruit_list:
    cursor.execute(insert_fruit, fruit)

conn.commit()

# データを更新
cursor.execute('UPDATE fruits_table SET value=1000 WHERE fruits="apple"')
conn.commit()

# データを取得
cursor.execute('SELECT * FROM fruits_table')
rows = cursor.fetchall()

# 出力
for i in rows:
    print(i)
