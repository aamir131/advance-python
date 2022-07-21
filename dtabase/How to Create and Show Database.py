import mysql.connector
try:
    conn = mysql.connector.connect(     # Connect() This method is used to open establish a new connection. It return an object representing the connection and conn id object
        user = 'root', 
        password = 'root',
        host = 'localhost',
        port = 3306
    )
    
    if(conn.is_connected()):  # this method is used to check the connection to MySQL is Establish or not. It Retruns True if the connection is established successfully
        print("Connected!!")

except:
    print("Unable to Connect")


#sql = "CREATE DATABASE pdb" # This command is used to create a database
sql = "SHOW DATABASES"       # This command is used to show the database
myc = conn.cursor()
myc.execute(sql)
for d in myc:
    print(d)
myc.close() 








conn.close()        # This Method is used to close the connection