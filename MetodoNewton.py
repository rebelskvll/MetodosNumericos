#!/usr/bin/python3

"""
Script de python del método de Newton para el módulo virtual de métodos
numéricos suministrado en la lectura fundamental 1, adaptado por Raúl Moncada.
"""

from math import *
from prettytable import PrettyTable

# Acá se define la función a evaluar
def funcion(x):

    return 2*sin(x)**2-3*cos(x)
     
# Derivada de la función a evaluar
def derivada(x):

    return 4*sin(x)*cos(x) + 3*sin(x)

# Se declara la tabla de forma global
resultados = PrettyTable(["Iteración","p"])

"""
En alguna literatura aparece que la primera iteración es 0 y va hasta n-1,
en el script arrancaba en 1. Pendiente validar con el tutor, por ahora, me 
parece más acertado iniciar en 0
"""
def newton(funcion, derivada, p0, tolerancia, maximo_iteraciones):

    iteraciones=1

    while iteraciones <= maximo_iteraciones:

        p = p0 - funcion(p0)/derivada(p0)
        if abs(p-p0) < tolerancia:
            return p
        p0=p
        resultados.add_row(["%03d" % iteraciones,"%.14f" % p])
        iteraciones+=1
        
        
    print("Iteraciones finalizadas, no se encontró el resultado")
    return
print("\n"+r"Metodo de Newton:"+"\n")
"""
Llama a la función de newton y le pasa como parámetros:
- La función a evaluar
- La derivada de la función
- el intervalo inicial p
- La tolerancia a error
- El número de itereaciones donde se quiere detener el proceso
"""
newton(funcion, derivada, 5, 1e-10, 100)

#Imprime la tabla con los valores calculados
print (resultados)
