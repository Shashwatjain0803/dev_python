import  mysql.connector

conn = mysql.connector.connect(host='localhost',database= 'Batman', user='root',password ='root')

# Creating the cursor for connection
cursor = conn.cursor()

create = 'create table employee(eno int , enname varchar(40) , age int, ecity varchar (40) , ecountry varchar(40));'
# Using cursor to execute one or more queries
cursor.execute(create)
print("table created")

# closing the cursor
cursor.close()

# closing connection object
conn.close()