import mysql.connector
def student_data(nm, ro, fe):
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
    myc = conn.cursor(prepared=True) # This is Prepares Method Or Satetment
    n = nm
    r = ro
    f = fe
    seq_of_para = (n, r, f)
    try:
        
        myc.execute(sql,seq_of_para) 
        conn.commit()
        print("Row Inserted")
        
    except:
        conn.rollback()
        print("Unable To Insert Data")
    myc.close()
    conn.close()
while True:
    # Data input From User
    nm = input('Enter Name: ')
    ro = int(input('Enter ROll: '))
    fe = float(input('Enter Fees: '))
    student_data(nm, ro, fe)
    ans = input("Do You Wnat To Exit?(y/n)")
    if(ans=='y'):
        break