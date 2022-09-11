from sympy import *

a0 = 4.5445
a1 = 7.7084
a2 = 14.6727
a3 = 10.5083
a4 = -4.0108
a5 = -1.0462
x0 = 0.6
x1 = 0.8
x2 = 1.6
x3 = 1.8
x4 = 4.6
x5 = 5
x = Symbol('x')

print (poly_from_expr(a0 + a1*(x-x0) 
+ a2*(x-x0)*(x-x1) 
+ a3*(x-x0)*(x-x1)*(x-x2) 
+ a4*(x-x0)*(x-x1)*(x-x2)*(x-x3)))
