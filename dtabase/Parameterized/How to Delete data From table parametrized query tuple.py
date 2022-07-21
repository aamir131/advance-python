import mysql.connector
try:
    conn = mysql.connector.connect(     
        user = 'root', 
        password = 'root',
        host = 'localhost',
        database = 'pdb',
        port = 3306
    )
    
    if(conn.is_connected()):  
        print("Connected!!")

except:
    print("Unable to Connect")

#tuple sql = 'DELETE FROM student1 WHERE roll = %s' # This method is used to delete data in tuple
sql = 'DELETE FROM student1 WHERE stuid = %(id)s' # This method is used to delete data in Dictionary
myc = conn.cursor()
#n = int(input('Enter Roll to Delete: ')) # This is used to delete data in tuple from user
#del_value = (n,)
n = int(input('Enter ID to Delete: ')) # This is used to delete data in Dictionary from user
del_value = {'id':n}
try:
    myc.execute(sql,del_value)       # This method is used to Delete  data 
    conn.commit()
    print(myc.rowcount,"Row Deleteed")
    
except:
    conn.rollback()
    print("Unable to Delete Data")
myc.close()


conn.close()        
