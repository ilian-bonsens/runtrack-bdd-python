import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***********",
    database="laplateforme"
)

cursor = mydb.cursor()

cursor.execute("select sum(superficie) from etage")

results = cursor.fetchall()

superficie = results[0][0]

print(f"La superficie de Laplateforme est de {superficie}m².")

cursor.close()
mydb.close()