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

#sql = 'UPDATE prepared SET fees = %s WHERE stuid = %s'
sql = 'UPDATE prepared SET fees = ? WHERE stuid = ?'
myc = conn.cursor(prepared=True) # This is Prepares Method Or Satetment
d = int(input('Enter Student ID to Update: '))
f = float(input('Enter fees: '))
del_valur=(f,d)


try:
    
    myc.execute(sql,del_valur)
    conn.commit()
    print("Row Updated")
    
except:
    conn.rollback()
    print("Unable To Update Data")
myc.close()
conn.close()