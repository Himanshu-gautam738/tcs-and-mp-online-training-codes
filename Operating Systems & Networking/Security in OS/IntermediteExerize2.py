import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

result = cursor.fetchall()
print(result)

conn.close()