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
        print("Connected!!")

except:
    print("Unable to Connect")

sql = 'UPDATE student1 SET  name = %(n)s,roll = %(r)s,fees = %(f)s WHERE stuid = %(st)s'
myc = conn.cursor()
Id = int(input('Enter Student Id to Update: '))
nm = input("Enter Name: ")
ro = int(input('Enter Roll: '))
fe = float(input('Enter Fees: '))
update_value = {'n':nm,'r':ro,'f':fe,'st':Id}       # Update row get input from user and using dictionary method

try:
    myc.execute(sql,update_value)       # This method is used to update data 
    conn.commit()
    print(myc.rowcount,"Row Updated")
    
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()


conn.close()        
