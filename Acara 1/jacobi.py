import numpy as np

A = np.array([[4.0,-2.0,1.0],
              [-2.0,4.0,-2.0],
              [1.0,-2.0,4.0]])

b = np.array([11.0,-16.0,17.0])

# toleransi error
tolerance = 0.00001

# iterasi masksimal
max_iter = 1000

nA = len(A)

# matrik identitas
D = np.identity(nA)

D_inv = np.zeros((nA,nA))

for i in range(nA):
    D_inv[i][i] = 1.0/A[i][i]

C = D - np.dot(D_inv,A)
d = np.dot(D_inv,b)

# nilai x awal
x_old = np.array([0,0,0])

# perhitungan nilai x dan iterasinya
for iteration in range(max_iter):
    x = d + np.dot(C,x_old)
    for i in range(nA):
        print(iteration,x[i],x[i]-x_old[i])

    error = np.max(abs(x-x_old))
    
    x_old = x
    
    # cek konvergensi
    if(error<tolerance):
        print()
        print("Penyelesaian matriks x adalah")
        for i in range (nA):
            print("x%s="%(i+1),x[i])
        print()
        print("error= ",error)
        break

