<center> 

# Modul Praktikum Numerik
## Acara 2. Sistem non linear dan mencari akar 
</center>

> ### Link Modul
> * [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
> * [Github](https://github.com/FajrulHQ/Prakt-Numerik)
>>  * [Acara 1 - Sistem Persamaan Linear simultaneous](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%201/Acara%201.md) [__[Download Here]__](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)
>>  * [Acara 2 - Sistem non linear dan mencari akar](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%202/Acara%202.md) [__[Download Here]__](https://drive.google.com/drive/folders/17aN5QrDvoH_QwJPU4YP9N5pLOv6nVo0q?usp=sharing)
> ### Contents
>1. Metode Biseksi
>1. Metode Newton Raphson
>1. Metode Secant
---
## 1. Metode Biseksi
Metode Biseksi merupakan metode pencarian akar yang paling sederhana. Metode ini mencari akar dengan asumsi `f(x) = 0` pada suatu batas tertutup yang diinputkan, yakni: `a` dan `b`. Oleh karena itu `f(a)` dan nilai `f(b)` harus mempunyai beda tanda

<center><img src="https://render.githubusercontent.com/render/math?math=f(a)*f(b)\lt0"></center>
<br>

Selanjutnya kita hitung `f(c)` dimana `c` adalah nilai tengah antara `a` dan `b`.

<center><img src="https://render.githubusercontent.com/render/math?math=c=\frac{a+b}{2}"></center>

<br>
<center>
    <img alt="Acara 2" src="https://github.com/FajrulHQ/pict/blob/main/Acara%202/Picture1.jpg?raw=true"><br>
    <b>Gambar 1.</b> Grafik Konsep Metode Biseksi
</center>
<br>

Jika `f(c) = 0` maka `c` adalah akar dari `f(x)`. Jika `f(c) ≠ 0`, kita harus menentukan interval berikutnya. Ada dua kemungkinan interval yang harus kita pilih. Pilihan antara interval `a` dan `c` atau `c` dan `b` dapat ditentukan dengan mencari hasil negatif perkalian `f(c)*f(a)` atau `f(c)*f(b)`. 

Jika kemungkinan pertama benar maka interval selanjutnya yang kita analisis adalah interval antara `a` dan `c`. Demikian juga sebaliknya. Dengan proses yang sama kita cari nilai `f(x)` dari nilai tengah interval yang baru.

Jumlah biseksi yang diperlukan dapat dihitung dari `ε`.  Interval `Δx` menjadi `Δx/2` setelah 1 biseksi, `Δx^2` setelah `2` biseksi, sehingga setelah `n` biseksi menjadi `Δx/2^n`. Dengan `Δx/2^n = ε`, maka `n` (bilangan bulat) diperoleh:

<center><img src="https://render.githubusercontent.com/render/math?math=n= \frac{ln (\Delta x/\varepsilon)}{ln(2)}"></center>

### Algoritma
1. Pilih batas `a` dan `b`, dengan syarat <img src="https://render.githubusercontent.com/render/math?math=f(a)*f(b)\leq0"><br><br>
2. . Tentukan nilai tengah `c`, dengan <img src="https://render.githubusercontent.com/render/math?math=c=\frac{a+b}{2}"><br><br>
3.  Lalu lakukan pengecekan
> *	Jika `f(a)` atau `f(b)` atau `f(c)` bernilai `nol`, maka penyelesaiannya adalah nilai tersebut
> *	Jika `f(a)*f(c) < 0`, maka nilai akar berada antara `a` dan `c`, lakukan swap, `a = a` dan `b = c`
> * Jika `f(a)*f(c) > 0`, maka nilai akar berada antara `c` dan `b`, lakukan swap, `a = c` dan `b = b`
> *	Jika `f(a)*f(c) = 0`, maka akarnya adalah `c`. Hentikan Algortitma
> *	Langkah 2 diulang dengan menggunakan nilai `a` dan `b` yang baru 
> *	Jika nilai `c` sudah memenuhi nilai tolerasi. Program dihentikan 

```python
import math
from numpy import sign

def bisection(f,x1,x2,switch=1,tol=1.0e-9):
  f1 = f(x1)
  if f1 == 0.0: 
      return x1
  f2 = f(x2)
  if f2 == 0.0: 
      return x2
  if sign(f1) == sign(f2):
      raise ValueError('Root is not bracketed')

  n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))
  for i in range(n):
      x3 = 0.5*(x1 + x2); f3 = f(x3)
      if (switch == 1) and (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
          return None
      
      if f3 == 0.0: return x3
      if sign(f2)!= sign(f3): x1 = x3; f1 = f3
      else: x2 = x3; f2 = f3
  return (x1 + x2)/2.0
```

```python
import numpy as np
from bisection import*

def f(x): 
    return x**3 - 7.0*x + 1.0

x = bisection(f, 2.0, 4.0, tol = 1.0e-4)

print('\nx =', '{:6.4f}'.format(x))
```
---
## 2. Metode Newton Raphson
 Metode Newton Raphson adalah salah satu metode pencarian akar per-samaan nonlinear yang bersifat open methods, artinya dalam proses metode ini tidak diperlukan suatu nilai batas interval seperti metode Biseksi.<br><br>
 Prinsip Metode Newton Raphson adalah jika suatu persamaan `f(x) = 0`, memiliki akar yang diasumsikan pada x<sub>i</sub>. Lalu dengan menggambarkan kurva tangesial pada f(x<sub>i</sub>), maka titik x<sub>i+1</sub> pada kurva tangesial yang memotong sumbu-x dianggap sebagai akar yang baru. Proses ini dilakukan terus menerus hingga mendapatkan nilai yang konvergen.
 <center><img src="https://render.githubusercontent.com/render/math?math=n= \frac{ln (\Delta x/\varepsilon)}{ln(2)}"></center><br>

>maka
> <center><img src="https://render.githubusercontent.com/render/math?math=n= \frac{ln (\Delta x/\varepsilon)}{ln(2)}"></center><br>

<br>
<center>
    <img alt="Acara 2" src="https://github.com/FajrulHQ/pict/blob/main/Acara%202/Picture2.jpg?raw=true"><br>
    <b>Gambar 2.</b> Konsep Metode Newthon Raphson
</center>

### Algoritma

1. Tentukan 
`f’(x)` secara analitik
2. Tentukan asumsi akar x<sub>i </sub>untuk menentukan nilai akar yang baru x<sub>i+1</sub><img src="https://render.githubusercontent.com/render/math?math=n= \frac{ln (\Delta x/\varepsilon)}{ln(2)}">
=======


### Algoritma

1. Tentukan `f’(x)` secara analitik
2. Tentukan asumsi akar x<sub>i</sub>, untuk menentukan nilai akar yang baru x<sub>i+1</sub>` dengan melakukan iterasi seperti berikut
 <center><img src="https://render.githubusercontent.com/render/math?math=n= \frac{ln (\Delta x/\varepsilon)}{ln(2)}"></center>
3. Jika nilai akar x<sub>i</sub>, telah korvergen (memenuhi batas toleransi), maka program dihentikan<br>

```python
## newthonRaphson method

def f(x): return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752
def df(x): return 4.0*x**3 - 19.2*x**2 + 12.9*x + 20.538

def newtonRaphson(x,tol=1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol: return x,i 
    print ('Too many iterations\n')

root,numIter = newtonRaphson(2.0)
# nilai 2.0 akan diinputkan ke fungsi newtonRaphson sebagai x

print ('Root =',root) 
print ('Number of iterations =',numIter)
```
---
## Metode Secant
 Jika pada metode Newton Raphson diperlukan proses iterasi untuk mendapatkan nilai akar yang baru `x_{i+1}` dan memerlukan proses derivatif dari persamaan secara analitik, seperti pada __persamaan (1)__ berikut

<center><img src="https://render.githubusercontent.com/render/math?math=x_{i%2B1}= x_i-  \frac{f(x_i)}{f'(x_i)}"></center><br>

 Maka proses dari metode Newton Raphson akan sedikit rumit, jika persamaan nonlinear tidak bisa dilakukan derivatif secara analitik. Oleh karena itu, dilakukan proses pendekatan secara geometri seperti pada __gambar (3)__ atau dengan melakukan pendekatan analitik seperti __persamaan (2)__ berikut

<center><img src="https://render.githubusercontent.com/render/math?math=f(x_i )= x_i-  \frac{f(x_i)-f(x_{i-1}) }{x_i-x_{i-1} }"></center>
<br>

 Substitusikan __persamaan (1)__ dan __(2)__, maka didapatkan __persamaan (3)__

<center><img src="https://render.githubusercontent.com/render/math?math=x_{i%2B1}= x_i-  \frac{f(x_i) - (x_i - x_{i-1})}{f(x_i)-f(x_{i-1})}"></center>

<br>
<center>
    <img alt="Acara 2" src="https://github.com/FajrulHQ/pict/blob/main/Acara%202/Picture3.jpg?raw=true"><br>
    <b>Gambar 3.</b> Konsep Metode Secant
</center>
<br>

__Persamaan (3)__ di atas lah yang melahirkan metode Secant. Dalam metode ini diperlukan 2 nilai awal, namun tidak seperti metode Biseksi yang digunakan sebagai batas interval. 2 nilai awal pada metode Secant digunakan untuk nilai x<sub>i</sub> dan x<sub>i</sub>.

Atau secara geometric persamaan tersebut didapatkan dengan menggambarkan garis lurus antara 2 nilai awal x<sub>i-1</sub> dan x<sub>i</sub>. Didaptkan 2 buah segitiga (_ABE_, _DEC_) yang sebangun, berdasarkan konsep sebangun didapatkan

<center><img src="https://render.githubusercontent.com/render/math?math=\frac{AB}{AE}=  \frac{DC}{DE}"></center>
<br>

<center><img src="https://render.githubusercontent.com/render/math?math=\frac{f(x_i) }{x_i-x_{i+1} }=  \frac{f(x_{i-1}) }{x_{i-1}-x_{i+1}}"></center>

Jika persamaan di atas disederhanakan, didapatkan kembali __persamaan (3)__

### Algoritma
1. Tentukan x<sub>i</sub> dan x<sub>i-1</sub>
2. Lakukan iterasi menentukan nilai akar yang baru xi+1 dengan
<center><img src="https://render.githubusercontent.com/render/math?math=n=x_{i%2B1}= x_i - \frac{f(x_i )-(x_i-x_{i-1})}{f(x_i)-f(x_{i-1})}"></center>
3. Jika nilai akar x<sub>i+1</sub> , telah korvergen (memenuhi batas toleransi), maka program dihentikan.

```python
# Program Secant 
print("------------ Program Secant ------------")

def f(x):
    return x**3 - 7.0*x + 1.0

xlama = int(input("Masukkan nilai x1: ")) 
xbaru = int(input("Masukkan nilai x2: "))

eps = float(input("Masukkan nilai toleransi:")) 
max_iter = int(input("\nMasukkan nilai maksimal iterasi: "))
count = 0

for i in range(max_iter):
    if (abs(xbaru-xlama) >= eps):
        count=count+1
        xsementara = xbaru
        xbaru = xbaru-(f(xbaru)*(xbaru-xlama))/(f(xbaru)-f(xlama))
        xlama = xsementara
        print(count," ",'{:17.15f}'.format(xbaru),"",'{:17.15f}'.format(xlama))

x = xbaru
x = xbaru 

print("\nNilai akar adalah: ",x) 
print("\nJumlah iterasi: ",count)