import mysql.connector

conn = mysql.connector.connect(host='localhost',database = 'Batman', user= 'root',password = 'root')

print('Connection Tested')

conn.close()