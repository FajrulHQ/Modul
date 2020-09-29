#!/usr/bin/python
## example2_4
import numpy as np
from gaussElimin import *


a = np.array([[2.0,5.0,3.0],
              [3.0,4.0,2.0],
              [1.0,3.0,1.0]])

b = np.array([1.0,-3.0,2.0])

aOrig = a.copy() # Save original matrix
bOrig = b.copy() # and the constant vector


x = gaussElimin(a,b)
det = np.prod(np.diagonal(a))
print('x =\n',x)
print('\ndet =',det)
print('\nCheck result: [a]{x} - b =\n',np.dot(aOrig,x) - bOrig)