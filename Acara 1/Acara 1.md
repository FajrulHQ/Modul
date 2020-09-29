<center> <h1> Modul Praktikum Numerik </h1> </center>
<center> <h2> Acara 1. Sistem Persamaan Linear </h2> </center>

* [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
* [Github](https://github.com/FajrulHQ/Prakt-Numerik)
    * [Acara 1 - Sistem Persamaan Linear](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)

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