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


#sql = 'CREATE TABLE student1(stuid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(22), roll INT, fees FLOAT)'
sql = 'SHOW TABLES'
myc =conn.cursor()
myc.execute(sql)
for t in myc:
    print(t)
myc.close()
conn.close()        
