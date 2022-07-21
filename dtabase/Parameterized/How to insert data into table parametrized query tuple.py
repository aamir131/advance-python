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
mak = ("Raja", 102, 35000.50)
try:
    myc.execute(sql,mak)
    conn.commit()
    print(myc.rowcount,"Row Inserted")
    print(f'Stu ID: {myc.lastrowid} Inserted')
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()


conn.close()        
