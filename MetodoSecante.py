#!/usr/bin/python3

"""
Script de python del método de la secante para el módulo virtual de métodos
numéricos suministrado en la lectura fundamental 2, adaptado por Raúl Moncada.
"""

from math import *


def velocidad (x):

    return x**3+2*x**2+10*x-20

def secante (f, t0, t1, tolerancia, iteraciones):

    i=2
    while i <= iteraciones:

        t = t1-(f(t1)*(t1-t0))/(f(t1)-f(t0))
        print ("Iter=", "%03d" % i, "; t=", "%.10f" % t)
        if abs(t-t1)<tolerancia:
            return t

        t0=t1
        t1=t
        i += 1

    print ("Iteraciones agotadas")
    return

print ("Métod de la secante: ")
secante (velocidad, 0, 1, 1e-5, 20)
