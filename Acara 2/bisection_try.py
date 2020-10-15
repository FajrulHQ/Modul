import numpy as np
from bisection import*

def f(x): 
    return x**3 - 7.0*x + 1.0

x = bisection(f, 2.0, 4.0, tol = 1.0e-4)

print('\nx =', '{:6.4f}'.format(x))