
import mysql.connector

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="9am", auth_plugin='mysql_native_password')
    cur=dbcon.cursor()
   
    cur.execute("insert into employee values(101,'Rahul',450000)")
    dbcon.commit()
    print('Data Inserted successfully')
except:
    print('Unable to connect')
