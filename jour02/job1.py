import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***********",
    database="Laplateforme"
)

cursor = mydb.cursor()

cursor.execute("select * from etudiants")

results = cursor.fetchall()
print(results)

cursor.close()
mydb.close()