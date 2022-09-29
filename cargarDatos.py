import csv

def cargarDatos():

    with open('datos.csv') as file:
        reader = csv.reader(file)
        """
        Al cargar los datos desde el csv, estos se leen como tuplas de tipo string,
        con esta línea, se crean las tuplas tipo float.
        """
        datos = [(float(row[0]), float(row[1])) for row in reader]
    return datos

