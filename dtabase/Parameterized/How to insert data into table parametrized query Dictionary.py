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

sql = 'INSERT INTO student1(name, roll, fees) VALUES(%(name)s,%(roll)s,%(fees)s)' # Insert single row using dicttionary
myc = conn.cursor()
mak = {'name':'Sholy', 'roll':90, 'fees':122000.57}
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
