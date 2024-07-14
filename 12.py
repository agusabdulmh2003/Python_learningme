import mysql. connector
mydb = mysql . connector . connect(
host="localhost",
user="root",
password=""
)
mycursor = mydb . cursor ()

mycursor = mydb . cursor()
mycursor . execute("CREATE TABLE cust")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLEcust (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR (255))")
for x in mycursor:

    print (x)

