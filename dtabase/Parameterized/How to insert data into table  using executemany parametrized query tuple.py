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

sql = 'INSERT INTO student1(name, roll, fees) VALUES(%s,%s,%s)'
myc = conn.cursor()
multipledata = [("Raj", 103, 15000.52),('Gabbar',25,5000),('Jai',23,4999),('Veeru',101,2344),('Thakur',104,10000.34)]
try:
    myc.executemany(sql,multipledata)       # This method is used to insert multiple data 
    conn.commit()
    print(myc.rowcount,"Row Inserted")
    print(f'Stu ID: {myc.lastrowid} Inserted')
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()


conn.close()        
