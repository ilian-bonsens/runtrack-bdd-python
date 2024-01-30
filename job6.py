import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="/5$JGF1d:yfTWKyJ",
    database="laplateforme"
)

cursor = mydb.cursor()

cursor.execute("select sum(capacite) from salle")

results = cursor.fetchall()

superficie = results[0][0]

print(f"La capacite de toutes les salles est de {superficie}.")

cursor.close()
mydb.close()