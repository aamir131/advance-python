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

sql = 'INSERT INTO student1(name, roll, fees) VALUES(%(name)s,%(roll)s,%(fees)s)' 
myc = conn.cursor()
mak = [{'name':'Sholy', 'roll':91, 'fees':12000.57},    # Insert multiple row using dictionary
       {'name':'Baby', 'roll':92, 'fees':135000.37},
       {'roll':94, 'name':'Special 26', 'fees':25000.86},
       {'name':'Kesari', 'fees':31590, 'roll':95}]
try:
    myc.executemany(sql,mak)
    conn.commit()
    print(myc.rowcount,"Row Inserted")
    print(f'Stu ID: {myc.lastrowid} Inserted')
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()


conn.close()        
