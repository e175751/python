import mysql.connector
import sys

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'N7p-Byjb'
)
cursor=db.cursor()

def init():
    cursor.execute("use test_python")
    db.commit()
    cursor.execute("""create table user_info(
                    id_name VARCHAR(32),
                    id_password VARCHAR(32));""")
    db.commit()


def user_info_input():
    name = input("your id name >>")
    password = input("your id pqssword >>")
    return name,password


def insert_info(name,pass):
    insert_string = "insert into id_serche(id_name,id_password) VALUES (%s, %s);"
    cursor.execute(insert_string,name,pass)
    db.commit()


init()
user_id_name,user_id_password = user_info_input()
insert_info(user_id_name,user_id_password)
