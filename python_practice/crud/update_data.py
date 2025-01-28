# Python implementation to fetch data from a table in MySQL
import pymysql

# connecting to the mysql server

db = pymysql.connect(
	host="localhost",
	user="root",
	passwd="rootpass11",
	database="employee_db"
)

# cursor object c
c = db.cursor()

# update statement for tblemployee
# which modifies the salary of Vani
employeetbl_update = "UPDATE tblemployee SET salary = 115000 WHERE empid = 1"

# execute the update query to modify
# the salary of employee with
# employee id = 1 and commit to the database
c.execute(employeetbl_update)
db.commit()

# finally closing the database connection
db.close()
