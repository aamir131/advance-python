import mysql.connector
def student_data(nm,ro,fe):
    try:
        conn = mysql.connector.connect(     
            user = 'root', 
            password = 'root',
            host = 'localhost',
            database = 'pdb',
            port = 3306
        )
        
        if(conn.is_connected()):  
            print("Connected!!")

    except:
        print("Unable to Connect")

    sql = 'INSERT INTO student1(name, roll, fees) VALUES(%s,%s,%s)'
    myc = conn.cursor()
    n = nm
    r = ro
    f = fe
    user_input = (n, r, f)
    try:
        myc.execute(sql,user_input)       # This method is used to insert multiple data 
        conn.commit()
        print(myc.rowcount,"Row Inserted")
        print(f'Stu ID: {myc.lastrowid} Inserted')
    except:
        conn.rollback()
        print("Unable to Insert Data")
    myc.close()


    conn.close()        
while True:
    # input from User
    nm = input('Enter Name: ')
    ro = int(input('Enter Roll: '))
    fe = float(input('Enter Fees: '))
    student_data(nm,ro,fe)
    ans=input("Do You Want Exit?(y/n): ")
    if (ans =='y'):
        break