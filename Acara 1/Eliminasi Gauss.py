# Gauss Elimination

import numpy as np
def gaussElimin(a,b):
  n = len(b)
  
  # Elimination Phase
  for k in range(0,n-1):
    for i in range(k+1,n):
       
      if a[i,k] != 0.0:
        lam = a[i,k]/a[k,k]
        a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
        b[i] = b[i] - lam*b[k]

# Back substitution
  for k in range(n-1,-1,-1):
    b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
  return b

A = np.array([[4.0,-2.0,1.0],
              [-2.0,4.0,-2.0],
              [1.0,-2.0,4.0]])

B = np.array([11.0,-16.0,17.0])

aOrig = A.copy() # Save original matrix
bOrig = B.copy() # and the constant vector
x = gaussElimin(A,B)
det = np.prod(np.diagonal(A))
print('x =',x)
print('\ndet =',det)
print('\nCheck result: [a]{x} - b =',np.dot(aOrig,x) - bOrig)
input("\nPress return to exit")