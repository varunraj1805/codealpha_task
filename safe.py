import sqlite3
import os

user_input = input("Enter ID: ")

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

query = "SELECT * FROM users WHERE id=?"
cursor.execute(query, (user_input,))

print("Secure Query Executed")

connection.close()
