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

sql = 'SELECT * FROM student' # * is used for all rows
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()            # this method is used to fetch one by one
    while row is not None:
        stuid = row[0]
        name = row[1]
        roll = row[2]
        fees = row[3]
        print(f'Stud ID: {stuid} Name: {name} Roll: {roll} Fees: {fees} ')
        row = myc.fetchone()
    print("Total Row",myc.rowcount)
except:
    conn.rollback()
    print("Unable to Show Data")
myc.close()
conn.close()