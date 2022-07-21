import mysql.connector
def medicine_record(nm,pr,br):
    try:
        conn = mysql.connector.connect(
        user = 'root',
        password = 'root',
        host = 'localhost',
        database = 'medicine',   
        port = '3306'
        )
        if(conn.is_connected()):
            print("Connected")
    except:
        print("Unable to Connect!!")
        
    sql = 'INSERT INTO medi(name, price, brand) VALUES(%s,%s,%s)'
    myc = conn.cursor()
    n = nm
    p = pr
    b = br
    med = (n, p, b)
    try:
        myc.execute(sql,med)
        conn.commit()
        print(myc.rowcount,"Row Inserted")
    except:
        conn.rollback()
        print("Unable to Insert Data")
    myc.close()
    conn.close()
while True:
    nm = input("Enter Medicine Name: ")
    pr = float(input("Enter Price: "))
    br = input("Enter Brand Name: ")
    medicine_record(nm,pr,br)
    print("If You Want Save More Record Type n")
    ans = input("Do You Want To Exit?(y/n)")
    if ans == 'y':
        break
