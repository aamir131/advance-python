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

#sql = 'Delete FROM prepared WHERE stuid = %s'
sql = 'Delete FROM prepared WHERE stuid = ?'
myc = conn.cursor(prepared=True) # This is Prepares Method Or Satetment
d = int(input('Enter Student ID to Delete: '))
del_valur=(d,)


try:
    
    myc.execute(sql,del_valur)
    conn.commit()
    print("Row Deleted")
    
except:
    conn.rollback()
    print("Unable To Delete Data")
myc.close()
conn.close()