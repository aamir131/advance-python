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

sql = 'DELETE FROM student WHERE stuid=2' # This command is used to delete row from the table
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()               # Commiting are used to save to the Change
    print(myc.rowcount,"Row Deleted")    
except:
    conn.rollback()             # rollback the change
    print("Unable to Delete Data")


myc.close()         # Close cursor
conn.close()        # Close Connection
