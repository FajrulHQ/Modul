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

---

 ## Pengantar
 Persamaan Differensial adalah persamaan yang mempunyai fungsi satu variabel bebas. Persamaan Differensial Biasa (`Ordinary Partial Differential`) adalah persamaan differensial yang mempunyai fungsi satu variabel bebas.

 `ODE` digunakan untuk mendapatkan formulasi suatu fenomena yang mengalami perubahan terhadap waktu/tempat.
> Contoh:
Model penurunan suhu akibat pengaruh atsmosfer di sekitarnya:
<center>
<img src="https://render.githubusercontent.com/render/math?math=dT_{obj}=-\alpha(T_{obj}-T_{ruang}) "><br>
<img src="https://render.githubusercontent.com/render/math?math=T_{obj}=T_{ruang}%2B(T_{awal}-T_{ruang})e^{-\alpha t} ">
</center><br>

 ### Metode Euler
 `Metode Euler` digunakan untuk melakukan aproksimasi penyelesaian persamaan orde pertama
<center>
<img src="https://render.githubusercontent.com/render/math?math=y'=f(x,y),y(x_0)=y_0 ">
</center>

 Dengan nilai <img src="https://render.githubusercontent.com/render/math?math=\Delta x=\frac{(x_f-x_0)}{n-1} ">
<center>

|x              |y                  |
|:---:          |:---:              |
|x<sub>1</sub>  |y(x<sub>1</sub>)   |
|x<sub>2</sub>  |y(x<sub>2</sub>)   |
|.<br>.<br>.    |.<br>.<br>.        |
|x<sub>n</sub>  |y(x<sub>n</sub>)   |
</center>

 Untuk nilai x dekat dengan x<sub>0</sub>

<center>
<img src="https://render.githubusercontent.com/render/math?math=y(x)\approx y'(x_0)(x-x_0)%2By(x_0)=(x-x_0)f(x_0,y_0)%2By_0 ">
<img src="https://render.githubusercontent.com/render/math?math=y(x_1)\approx (x_1-x_0)f(x_0,y_0)%2By_0=\Delta xf(x_0,y_0)%2By_0 ">
<img src="https://render.githubusercontent.com/render/math?math=y(x_2)\approx (x_2-x_1)f(x_1,y_1)%2By_1=\Delta xf(x_1,y_1)%2By_1 "><br>
.<br>.<br>.<br>
<img src="https://render.githubusercontent.com/render/math?math=y(x_n)\approx (x_n-x_{n-1})f(x_n,y_{n-1})%2By_{n-1}=\Delta xf(x_{n-1},y_{n-1})%2By_{n-1} "><br>
<img src="https://render.githubusercontent.com/render/math?math=y_{j%2B1}=\Delta xf(x_j,y_j)%2By_j "><br>
</center>

> Contoh :
<center>
<img src="https://render.githubusercontent.com/render/math?math=y'=-y%2Bsin(x),y(0)=1 ">
</center><br>
Menggunakan metode Euler untuk mengaproksmasi nilai fungsi pada interval `[0, 10]` dengan `101` titik. <img src="https://render.githubusercontent.com/render/math?math=x_0=0, x_f-10, n=101, \Delta x=\frac{x_f-x_0}{n-1}=0.1 "> 

## Contoh Penerapan di Geofisika : <br> Metode Analitik untuk Interpretasi Anomali Gravitasi

### 1. First Horizontal Derivative (FHD) 
<center>

![contoh1](../pict/Acara%205/2.png)
![contoh1](../pict/Acara%205/3.jpeg)
</center>

<br>

### 2. Second Vertical Derivative (SVD)
<center>

![contoh2](../pict/Acara%205/1.png)
![contoh1](../pict/Acara%205/4.jpeg)
</center>