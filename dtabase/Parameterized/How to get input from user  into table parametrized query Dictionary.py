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
nm = input('Enter Name: ')      # this is using for get input from user l19 to 22
ro = int(input('Enter Roll: '))
fe = float(input('Enter Fees: '))
mak = {'name':nm, 'roll':ro, 'fees':fe}
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
