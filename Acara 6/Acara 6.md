<center> 

# Modul Praktikum Numerik </h1>
## Acara 6. Partial Differential Equations (ODE) 
</center>

> ### Link Modul
> * [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
> * [Github](https://github.com/FajrulHQ/Prakt-Numerik)
>>  * [Acara 1 - Sistem Persamaan Linear simultaneous](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%201/Acara%201.md) [__[Download Here]__](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)
>>  * [Acara 2 - Sistem non linear dan mencari akar](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%202/Acara%202.md) [__[Download Here]__](https://drive.google.com/drive/folders/17aN5QrDvoH_QwJPU4YP9N5pLOv6nVo0q?usp=sharing)
>>  * [Acara 3 - Interpolasi dan kurva fitting](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%203/Acara%203.md) [__[Download Here]__](https://drive.google.com/drive/folders/1rDq2SUB0OCT58TML7OEPjWiuK4gC_GxT?usp=sharing)
>>  * [Acara 4 - Differensiasi dan Integrasi](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%204/Acara%204.md) [__[Download Here]__](https://drive.google.com/drive/folders/1eFA36m0f2kSgOjpuxNCS9V24IvUXwtKP)
>>  * [Acara 5 - Ordinary Differential Equations (ODE)](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%205/Acara%205.md) [__[Download Here]__](https://drive.google.com/drive/folders/1mr4_QPAsfgZ9kfSoK0zEPxMiex7iG5Ir)
>>  * [Acara 6 - Partial Differential Equations (PDE)](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%206/Acara%206.md) [__[Download Here]__](https://drive.google.com/drive/folders/1_Y8Rr2Few7SgH5HPCtPi-Q3TE4u3VKUH)

---

 ## Pengantar
 `Persamaan Differensial Parsial` adalah persamaan differensial yang mempunyai fungsi dengan jumlah variabel bebas lebih dari satu.

 PDE orde 2 secara umum:
<center>
<img src="https://render.githubusercontent.com/render/math?math=A\frac{\delta ^2u}{\delta x^2}%2BB\frac{\delta ^2u}{\delta x\delta y}%2BC\frac{\delta ^2u}{\delta y^2}%2BD\frac{\delta u}{\delta x}%2BE\frac{\delta u}{\delta y}%2BFu=G "><br>
<img src="https://render.githubusercontent.com/render/math?math=i.e.,\quad Au_{xx}%2BBu_{xy}%2BCu_{yy}%2BDu_x%2BEu_y%2BFu=G ">
<br>Di mana <b>A, B, C, D, E, F, G</b> adalah fungsi dari `x` dan `y` 
</center><br>

`PDE` diklasifikasikan menjadi 3 tipe yaitu eliptik, hiperbolik,dan parabolik berdasarkan nilai deskriminannya.
<center>
<img src="https://render.githubusercontent.com/render/math?math=D=B^3-4AC "><br><br>

|B<sup>3</sup> - 4AC    |Kategori   |
|:---:                  |:---:      |
|<  0                   |Elliptik    |
|=  0                   |Parabolik  |
|>  0                   |Hiperbolik |
</center>

### A. Persamaan Elliptik

#### 1. Poisson
<center>
<img src="https://render.githubusercontent.com/render/math?math=\frac{\delta^2u}{\delta x^2}%2B\frac{\delta^2u}{\delta y^2}=g(x,y) ">
</center><br>

#### 2. Laplace
<center>
<img src="https://render.githubusercontent.com/render/math?math=\frac{\delta^2u}{\delta x^2}%2B\frac{\delta^2u}{\delta y^2}=0 \quad \textrm{atau}\quad \nabla^2u=0 ">
</center><br>

### B. Persamaan Parabolik
 Contoh    : Persamaan konduktivitas panas
<center>
<img src="https://render.githubusercontent.com/render/math?math=\frac{\delta u}{\delta t}=\alpha\frac{\delta^2u}{\delta x^2} ">
</center>

Penyelesaian `u` adalah nilai suhu pada jarak `x` dari batas isolasi setelah `t` sekon

### C. Persamaan Hiperbolik

Contoh persamaan perambatan gelombang 1D
 <center>
<img src="https://render.githubusercontent.com/render/math?math=\frac{\delta ^2u}{\delta ^2t}=c^2\frac{\delta^2u}{\delta x^2} ">
</center>

Di mana `u` adalah perpindahan transversal pada jarak `x` dari ujung tali dengan panjang `l` dan saat waktu `t`

---
<br>
Contoh    :
<center>
<img src="https://github.com/FajrulHQ/pict/blob/main/Acara%206/Picture%201.png?raw=true ">
</center>

Persamaan perambatan panas 1D
<center>
<img src="https://render.githubusercontent.com/render/math?math=\frac{dT(i)}{dt}=\alpha[\frac{-(T_i-T_{i-1})}{\Delta x^2}%2B\frac{(T_{i%2B1}-T_i)}{\Delta x^2}] "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=T(t%2B\Delta t)\approx T(t)%2B\frac{dT}{dt}|_t^{\Delta t} ">
</center>