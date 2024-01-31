import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="/5$JGF1d:yfTWKyJ",
    database="zoo"
)

cursor = mydb.cursor()

class Zoo:
    def __init__(self, mydb, cursor):
        self.mydb = mydb
        self.cursor = cursor

    def add_animal(self):
        self.cursor.execute("INSERT INTO animal (nom, race, date_de_naissance, pays_origine, id_type_cage) VALUES ('Nibi', 'Tigre du Bengal', '2020-02-01', 'Inde', 4)")
        self.cursor.execute("INSERT INTO animal (nom, race, date_de_naissance, pays_origine, id_type_cage) VALUES ('Vitinha', 'Chevre', '1999-06-07', 'Portugal', 1)")
        self.cursor.execute("INSERT INTO animal (nom, race, date_de_naissance, pays_origine, id_type_cage) VALUES ('Vitinha', 'Chevre', '1999-06-07', 'Portugal', 1)")

    def cage(self):
        self.cursor.execute("INSERT INTO cage (superficie, capacite, animaux) VALUES (40, 2, 2)")
        
    def show_animal(self):
        self.cursor.execute("SELECT * from animal")
        results = self.cursor.fetchall()
        for row in results:  
            print(row)

    def show_cage(self):
        self.cursor.execute("SELECT * from cage")
        results_cage = self.cursor.fetchall()
        for row in results_cage:  
            print(row)

zoo = Zoo(mydb, cursor)
zoo.add_animal()
zoo.cage()
zoo.show_animal()
zoo.show_cage()

cursor.close()
mydb.close()

