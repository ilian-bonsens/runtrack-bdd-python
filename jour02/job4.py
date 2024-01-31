import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***********",
    database="laplateforme"
)

cursor = mydb.cursor()

cursor.execute("select nom, capacite from salle")

results = cursor.fetchall()
print(results)

cursor.close()
mydb.close()