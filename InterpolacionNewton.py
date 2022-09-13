#!/usr/bin/python3

from math import *
from turtle import st
from prettytable import PrettyTable
import csv

"""
Aquí se define la tabla de manera global para poder modificarla en diferentes
partes del script 
"""
tabla_resultados = PrettyTable()
columnas = []


def extraerCoeficientes(datost):

    tabla_coeficientes = PrettyTable(["Coeficiente","Valor"])
    for i in range (len(datost)):
        tabla_coeficientes.add_row([f"Coeficiente {i}", "%.4f" % datost[i][i]])

    return tabla_coeficientes

def NewtonPol(datos):
    n = len(datos) - 1
    
    

    F = [[0 for x in datos] for x in datos]


    for i, p in enumerate(datos):
        F[i][0] = p[1]


    for i in range (1, n+1):
        for j in range (1, i+1):
            F[i][j] = (F[i][j-1]-F[i-1][j-1]) / (datos[i][0] - datos [i-j][0])
            
    def L(k, x):
        out = 1.0
        for i, p in enumerate(datos):
            if i <= k:
                out *= (x-p[0])
        return out

    def P(x):
        newt = 0.0
        for i in range(1, n+1):
            newt += F[i][i] * L(i-1, x)
        return newt + F[0][0]

    return F, P

"""
Se crea esta función para cargar los datos desde el archivo
'interpolacion_newton.csv', que debe tener los valores separados por comas
"""
datost = []
with open('interpolacion_newton.csv') as file:
   reader = csv.reader(file)
   """
   Al cargar los datos desde el csv, estos se leen como tuplas de tipo string,
   con esta línea, se crean las tuplas tipo float.
   """
   datost = [(float(row[0]), float(row[1])) for row in reader]
print(datost)


T, P = NewtonPol(datost)



print ("Tabla de diferencias divididas:" + "\n")

# Se recorre toda la lista de tuplas que se generó para crear la tabla. 
for i in range (len(T)):
    # Se crean los nombres de las columnas
    columnas.append(f"Diferencia {i}")
    # Se agregan las filas a la tabla
    tabla_resultados.add_row(T[i])

# Finalmente se agregan los nombres de las columnas
tabla_resultados.field_names = columnas

print(tabla_resultados)
print (extraerCoeficientes(T))

#Para analizar los puntos entre 0 y 5 minutos
x = 0.0
for i in range (26):
    # Se recorren los 5 segundos
    print(f"polinomio en {round(x, 1)}: {round(P(x), 4)}")
    x = x + 0.2
