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

sql = 'SELECT * FROM prepared WHERE stuid = %s'
myc = conn.cursor(prepared=True)
#n = int(input('Enter Student Id To Retrieve: '))
value = (10,)
try:
    myc.execute(sql,value)
    row = myc.fetchone()            # this method is used to fetch one by one
    
    print(row)
    row = myc.fetchone()
    print("Total Row",myc.rowcount)
except:
    print("Unable to Retrieve")
myc.close()
conn.close()