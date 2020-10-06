<center> 

# Modul Praktikum Numerik
## Acara 1. Sistem Persamaan Linear simultaneous
</center>

> ### Link Modul 
>* [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
> * [Github](https://github.com/FajrulHQ/Prakt-Numerik)
>>  * [Acara 1 - Sistem Persamaan Linear simultaneous](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%201/Acara%201.md) [__[Download Here]__](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)
> ### Contents
> 1. Pendahuluan
> 1. Tujuan
> 1. Eliminasi Gauss
> 1. Eliminasi Jacobi
> 1. Penerapan di Geofisika
---
> ## 1. Pendahuluan
> Pada acara ke 1 ini, kita akan belajar mengenai Sistem Persamaan Linear serta implementasi kode python untuk menghitung operasi SPL.
---
> ## 2. Tujuan
>Tujuan acara ke 1 ini :  
> * Praktikan mengerti cara mencari nilai `x1,x2,...,xn` dari sebuah SPL dengan metode beriterasi 
> * Mengimpelemntasikan operasi SPL dalam program python
---
> ## 3.Eliminasi Gauss
> Eliminasi Gauss merupakan metode untuk menyelesaikan persamaan matrik `Ax = b` 
> Eleminasi Gauss mengubah matrik dalam bentuk: <br>

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/01.png?raw=true">
</center>

> menjadi matrik augmentasi

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/02.png?raw=true">
</center>

> kemudian dilakukan operasi baris dan kolom (forward elimination) sehingga matrik diatas berubah menjadi

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/02-1.png?raw=true">
</center>

> Persamaan diselesaikan untuk `xn` dari baris ke `n`, kemudian disubtitusikan kembali (_backward subtitution_) ke persamaan untuk `xn−1` dari baris ke `(n−1)`, berdasarkan persamaan berikut:

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/03.png?raw=true">
</center>

```python
-----------------------------------------------------------
# Script python akan ditampilkan di jam Praktikum
-----------------------------------------------------------
```
---
> ## 4.Eliminasi Jacobi
> Dengan metode Jacobi ini ada 2 asumsi yaitu : <br>
> A. Sistem Persamaannya dan memiliki hasil yang unik

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/04.png?raw=true">
</center>

> B.	Koefisien matrix A tidak mengandung _zeros_ (0) di diagonal matriksnya <br>
Untuk memulai, selesaikan persamaan 1 untuk `x1` , persamaan 2 untuk `x2` sampai ke persamaan `n` untuk `xn` yang di dapat di tuliskan dalam persamaan sebagai berikut : 

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/05.png?raw=true">
</center>

> Dimana kita menentukan `x(0) = x1(0) , x2(0), … , xn(0)` dimana akan di dapatkan nilai _first approximation_ `x(1) = x1(1), x2(1),….,xn(1)`. 
<br>
Proses diatas dapat di katakan 1 proses iterasi. Untuk mencari nilai _second approximation_ dilakukan cara yang sama seperti cara _first approximation_. Dengan mengulangi iterasinya, kita akan mendapatkan urutan nilai _approximation_.

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/06.png?raw=true">
</center>

> Untuk menyelesaikan metode Jacobi kita dapat menggunkan bentuk matrix. Untuk menyelesaikan dengan cara matriks kita akan melewati beberapa tahapan : 
<br> Kita membutuhkan sebuah persamaan matriks dimana `Ax = b` dengan

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/07.png?raw=true">
</center>

> Matriks akan kita bagi menjadi 3 bagian menjadi:

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/08.png?raw=true">
</center>

> Hal tersebut menjadikan persamaan menjadi _(D – L – U )x = b ->  Dx = (L + U)x + b_
<br> Untuk menghilangkan matriks ___D___ maka kita perlu mencari nilai ___D<sup>-1</sup>___ 

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/09.png?raw=true">
</center>

> Maka persamaan berubah menjadi _x = D<sup>-1</sup>(L+U)x + D<sup>-1</sup>b_ 
<br> Dan secara umum persamaan iterasi metode jacobi yaitu:

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/10.png?raw=true">
</center>

> Kita asumsikan

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/11.png?raw=true">
</center>

> Dan

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/12.png?raw=true">
</center>

> Maka rumus akhirnya adalah

<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/13.png?raw=true">
</center>

```python
-----------------------------------------------------------
# Script python akan ditampilkan di jam Praktikum
-----------------------------------------------------------
```

> ## 5. Penerapan dibidang Geofisika
> Pada iterasi jacobi memiliki bentuk `Ax = B` sama halnya dengan forward problem yaitu `Gm = d`,  dimana `G` adalah fungsi pembangkit, `m` adalah parameter model dan `d` adalah data yang dicari. pada iterasi jacobi dicari nilai `x` sedangkan pada geofisika, kita akan mencari `m`, dimana `d` sudah diperoleh dari data lapangan dan `G` adalah persamaan matematis, proses ini disebut __inverse modelling__. Diperlukan tebakan awal sebagai model awal, tebakan awal akan mempengaruhi kecepatan iterasi dalam mencapai model yang sebenarnya. dalam melakukan iterasi dilihat pada nilai errornya, jika error kecil maka sudah mendekati model sebenarnya.
<center>
    <img alt="Acara 1" src="https://github.com/FajrulHQ/pict/blob/main/Acara%201/14.jpeg?raw=true">
</center>