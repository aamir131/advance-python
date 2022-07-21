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
        print("Connected Successfully......")
except:
    print("Unable To Connect!!!!!!")

#sql = 'INSERT INTO prepared(name, roll, fees) VALUES(%s,%s,%s)'
sql = 'INSERT INTO prepared(name, roll, fees) VALUES(?,?,?)' # This is qmark
myc = conn.cursor(prepared=True)
para=('Sak',212,26000.78)

try:
    
    myc.execute(sql,para)
    conn.commit()
    print(myc.rowcount,"Row Inserted")
    print(f'Stu ID {myc.lastrowid} Inserted.')
except:
    conn.rollback()
    print("Unable To Insert Data")
myc.close()
conn.close()