import mysql.connector

database=mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='password123'
)

# prepare a cursor object

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

# print("All Done!!")


