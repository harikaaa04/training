# Python implementation to create a Database in MySQL
import pymysql

# connecting to the mysql server
db = pymysql.connect(
	host="localhost",
	user="root",
	passwd="rootpass11"
)

# cursor object c
c = db.cursor()

# executing the create database statement
c.execute("CREATE DATABASE employee_db")

# fetching all the databases
c.execute("SHOW DATABASES")

# printing all the databases
for i in c:
	print(i)
c = db.cursor()

# finally closing the database connection
db.close()

