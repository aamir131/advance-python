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

sql = 'UPDATE student SET fees= 200 WHERE stuid=8' # This command is used to UPDATE data row from the table
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()               # Commiting are used to save to the Change
    print(myc.rowcount,"Row UPDATED")    
except:
    conn.rollback()             # rollback the change
    print("Unable to UPDATE Data")


myc.close()         # Close cursor
conn.close()        # Close Connection
