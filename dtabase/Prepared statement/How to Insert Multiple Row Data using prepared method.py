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

#sql = 'INSERT INTO prepared(name, roll, fees) VALUES(%s,%s,%s)'
sql = 'INSERT INTO prepared(name, roll, fees) VALUES(?,?,?)' # This is qmark
myc = conn.cursor(prepared=True) # This is Prepares Method Or Satetment
seq_of_para=[('John',40,1000),
      ('Kapil',32,45000),
      ('Ajay',23,70900),
      ('Jubin',11,45000) 
      ]

try:
    
    myc.executemany(sql,seq_of_para) # This method is used to insert multiple data
    conn.commit()
    print("Row Inserted")
    
except:
    conn.rollback()
    print("Unable To Insert Data")
myc.close()
conn.close()