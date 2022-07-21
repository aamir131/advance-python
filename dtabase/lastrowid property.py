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

sql = 'INSERT INTO student(name, roll, fees) VALUES("Sufiyan", 37, 23000.50)'
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()               # Commiting are used to save to the Change
    print(myc.lastrowid)        # This Property are used to Show last Row Id Inserted suppose multiple Data insert in this case show the first insert data id 
except:
    conn.rollback()             # rollback the change
    print("Unable to Insert Data")


myc.close()         # Close cursor
conn.close()        # Close Connection
