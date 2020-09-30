<center> <h1> Modul Praktikum Numerik </h1> </center>
<center> <h2> Acara 1. Sistem Persamaan Linear </h2> </center>

* [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
* [Github](https://github.com/FajrulHQ/Prakt-Numerik)
    * [Acara 1 (Drive) - Sistem Persamaan Linear](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)

### Contents

1. Pendahuluan
1. Eliminasi Gauss
1. Eliminasi Jacobi

#### 1. Pendahuluan
Pada acara ke 1 ini, kita akan belajar mengenai Sistem Persamaan Linear serta implementasi kode python untuk menghitung operasi SPL.

#### 2. Tujuan
Tujuan acara ke 1 ini :


* Praktikan mengerti cara mencari nilai `x1,x2,...,xn` dari sebuah SPL dengan metode beriterasi
* Mengimpelemntasikan operasi SPL dalam program python

#### A.Eliminasi Gauss
Eliminasi Gauss merupakan metode untuk menyelesaikan persamaan matrik `Ax = b`.<br> 
Eleminasi Gauss mengubah matrik dalam bentuk: <br>

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/01.png?raw=true">
</center>

menjadi matrik augmentasi

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/02.png?raw=true">
</center>

kemudian dilakukan operasi baris dan kolom (forward elimination) sehingga matrik diatas berubah menjadi

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/02-1.png?raw=true">
</center>

Persamaan diselesaikan untuk `xn` dari baris ke `n`, kemudian disubtitusikan kembali (_backward subtitution_) ke persamaan untuk `xn−1` dari baris ke `(n−1)`, berdasarkan persamaan berikut:

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/03.png?raw=true">
</center>

```python
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
```

#### A.Eliminasi Jacobi
Dengan metode Jacobi ini ada 2 asumsi yaitu : <br>

A. Sistem Persamaannya dan memiliki hasil yang unik

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/04.png?raw=true">
</center>

B.	Koefisien matrix A tidak mengandung _zeros_ (0) di diagonal matriksnya 

Untuk memulai, selesaikan persamaan 1 untuk `x1` , persamaan 2 untuk `x2` sampai ke persamaan `n` untuk `xn` yang di dapat di tuliskan dalam persamaan sebagai berikut : 

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/05.png?raw=true">
</center>

Dimana kita menentukan `x(0) = x1(0) , x2(0), … , xn(0)` dimana akan di dapatkan nilai _first approximation_ `x(1) = x1(1), x2(1),….,xn(1)`. 

Proses diatas dapat di katakan 1 proses iterasi. Untuk mencari nilai _second approximation_ dilakukan cara yang sama seperti cara _first approximation_. Dengan mengulangi iterasinya, kita akan mendapatkan urutan nilai _approximation_.

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/06.png?raw=true">
</center>

Untuk menyelesaikan metode Jacobi kita dapat menggunkan bentuk matrix. Untuk menyelesaikan dengan cara matriks kita akan melewati beberapa tahapan : 

Kita membutuhkan sebuah persamaan matriks dimana `Ax = b` dengan

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/07.png?raw=true">
</center>

Matriks akan kita bagi menjadi 3 bagian menjadi:

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/08.png?raw=true">
</center>

Hal tersebut menjadikan persamaan menjadi _(D – L – U )x = b ->  Dx = (L + U)x + b_

Untuk menghilangkan matriks ___D___ maka kita perlu mencari nilai ___D<sup>-1</sup>___ 

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/09.png?raw=true">
</center>

Maka persamaan berubah menjadi _x = D<sup>-1</sup>(L+U)x + D<sup>-1</sup>b_ 

Dan secara umum persamaan iterasi metode jacobi yaitu:

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/10.png?raw=true">
</center>

Kita asumsikan

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/11.png?raw=true">
</center>

Dan

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/12.png?raw=true">
</center>

Maka rumus akhirnya adalah

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/13.png?raw=true">
</center>

```python
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
```