import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER, 
    user_name TEXT,
    age INTEGER

)
""")

connect.commit()

users_list = [[1, "Vasya", 56], [2, "Petr", 32]]
for user in users_list:
    cursor.execute("INSERT INTO users VALUES(?,?,?);", user)
connect.commit()
