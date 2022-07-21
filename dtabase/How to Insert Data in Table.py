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

sql = 'INSERT INTO student(name, roll, fees) VALUES("Rahul", 1, 25000.50),("Umesh", 19, 5000.78),("Virat", 18, 17000.20)'                   # This command is used to delete row from the table
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print("Row Inserted")
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()


conn.close()        
