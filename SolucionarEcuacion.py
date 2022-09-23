
from sympy import Symbol
x = Symbol('x')

ecuacion = -1.0462*x**5 + 5.8234*x**4 - 1.8345*x**3 - 4.4178*x**2+9.763*x
print(ecuacion.subs(x,4.1253))