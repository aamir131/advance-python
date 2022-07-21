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

sql = 'SELECT * FROM student1 WHERE fees = %s' # * is used for all rows
myc = conn.cursor()
n = float(input('Enter Student Fees to Display: '))
disp_value = (n,)
try:
    myc.execute(sql,disp_value)
    row = myc.fetchone()            # this method is used to fetch one by one
    while row is not None:
        print(row)
        row = myc.fetchone()
    print("Total Row",myc.rowcount)
except:
    conn.rollback()
    print("Unable to Retrieve Data")
myc.close()
conn.close()