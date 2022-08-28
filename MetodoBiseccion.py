#!/usr/bin/python3

"""
Script de python del método de bisección para el módulo virtual de métodos
numéricos suministrado en la lectura fundamental 1, adaptado por Raúl Moncada.
"""

from math import *
from prettytable import PrettyTable

# Se crea la tabla de forma global
resultados = PrettyTable(["Iteración","p"])

#Acá se define la función a evaluar, recibe como parámetro X
def f(x):

    return 10*x**4-3*x*exp(x)-3*exp(x)

"""
Función que calcula p, se detiene al momento de que x es menor a la tolerancia 
o al llegar al número de iteraciones a evaluar
"""
def biseccion(f, punto_a, punto_b, tolerancia, iteraciones_evaluar):

    iteraciones=1
    while iteraciones <= iteraciones_evaluar:

        p=punto_a+(punto_b-punto_a)/2.0
        """
        Se agregan van agregando las filas a la tabla conforme 
        se hace el cálculo
        """
        resultados.add_row(["%03d" % iteraciones,"%.14f" % p])
        if abs(f(p)) <= 1e-15 or (punto_b - punto_a)/2.0 < tolerancia:
            return p

        if f(punto_a) * f(p) > 0:
            punto_a=p
        else:
            punto_b=p

        iteraciones += 1

    print("Iteraciones finalizadas, no se encontró el resultado")

    return

print("\n"+r"Metodo de la Bisección:"+"\n")
"""
Llama a la función bisección y le pasa como parámetros:
- La función a evaluar
- el intervalo inicial a evaluar (a,b)
- La tolerancia a error
- El número de itereaciones donde se quiere detener el proceso
"""
biseccion(f,-1.0, -0.25, 1e-4, 100)
#Imprime la tabla con los valores calculados
print (resultados)