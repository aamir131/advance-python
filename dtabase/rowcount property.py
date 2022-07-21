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

sql = 'INSERT INTO student(name, roll, fees) VALUES("Aman", 69, 21000.50),("Snoj", 45, 11000.78),("Vishal", 62, 19000.20)'
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,"Row Inserted") # This Property are used to count How Many Rows Inserted
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()


conn.close()        
