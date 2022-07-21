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
myc = conn.cursor(buffered=True)
try:
    myc.execute(sql)
    row = myc.fetchmany(4)    # this method is used to how many data are retrive 
    for r in row:
        stuid = r[0]
        name = r[1]
        roll = r[2]
        fees = r[3]
        print(f'Stud ID: {stuid} Name: {name} Roll: {roll} Fees: {fees} ')
    print("Total Row",myc.rowcount)
    print()
    row = myc.fetchall()    # this method is used to  retrive all data
    for r in row:
        stuid = r[0]
        name = r[1]
        roll = r[2]
        fees = r[3]
        print(f'Stud ID: {stuid} Name: {name} Roll: {roll}')
    print("Total Row",myc.rowcount)
except:
    conn.rollback()
    print("Unable to Show Data")
myc.close()
conn.close()