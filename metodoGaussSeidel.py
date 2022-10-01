from math import *
from pprint import pprint

def distinf(x, y):
    return max([abs(x[i]-y[i]) for i in range (len(x))])

def GaussSeidel (A, b, x0, TOL, MAX):
    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1

    while k <= MAX:
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print ("Imposible iterar")
                return
            s1 = sum ([A[i][j]*x[j] for j in range(i)])
            s2 = sum ([A[i][j]*x0[j] for j in range(i+1, n)])
            x[i] = (b[i] - float(s1) - float(s2)) / float(A[i][i])
        pprint (x)

        if distinf(x, x0) < TOL:
            print ("Solución encontrada")
            return
        
        k += 1 

        for i in range(n):
            x0[i] = x[i]
    
    print ("Iteraciones agotadas")
    return

A = [[20, 4, 7, 5], [10, 50, 10, 15], [5, 10, 25, 8], [7, 10, 8, 40]]
b = [600, 1500, 800, 900]
x0 = [1, 1, 1, 1]

print ("Matriz A: \n")
pprint (A)
print ("Vector b: \n")
pprint (b)
print ("Semilla x0: \n")
pprint (x0)
print ("Iteraciones de Gauss-Seidel")
GaussSeidel(A, b, x0, 1e-5, 50)
