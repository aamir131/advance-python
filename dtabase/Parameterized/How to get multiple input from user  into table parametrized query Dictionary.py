import mysql.connector
def student_data(nm,ro,fe):
    try:
        conn = mysql.connector.connect(
            user = 'root',
            password = 'root',
            host = 'localhost',
            database = 'pdb',
            port = '3306'
        )

        if (conn.is_connected()):
            print("Connected...")
    except:
        print("Unable To Connect!!!")

    sql = 'INSERT INTO student1(name,roll,fees) VALUES(%(name)s,%(roll)s,%(fees)s)'
    myc = conn.cursor()
    n = nm
    r = ro
    f = fe
    para = {'name': n,'roll':r,'fees':f}

    try:
        myc.execute(sql,para)
        conn.commit()
        print(myc.rowcount,"Row Inserted")
        print(f'Stu ID: {myc.lastrowid} Inserted')
    except:
        conn.rollback()
        print("Unable To Insert Data???")
    myc.close()
    conn.close()
while True:
    nm = input('Enter Name: ')
    ro = int(input('Enter Roll: '))
    fe = float(input('Enter Fees: '))
    student_data(nm,ro,fe)
    ans = input("Do You Want To Exit?(y/n)")
    if(ans=='y'):
        break