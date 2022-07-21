import mysql.connector
try:
    conn = mysql.connector.connect(
        user = 'root',
        password = 'root',
        host = 'localhost',
        database = 'pdb',
        port = 3306 
    )
    if(conn.is_connected):
        print("Connected Successfully!!!")
except:
    print("Unable to Connect!!!!")

sql = 'SELECT * FROM student WHERE stuid=3' # this method used to check one specific data 
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()            # this method is used to fetch one by one
    print(row)
    print("Total Row",myc.rowcount)
except:
    conn.rollback()
    print("Unable to Show Data")
myc.close()
conn.close()