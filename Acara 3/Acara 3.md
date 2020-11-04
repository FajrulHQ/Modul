<center> 

# Modul Praktikum Numerik
## Acara 3. Interpolasi dan kurva fitting 
</center>

> ### Link Modul
> * [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
> * [Github](https://github.com/FajrulHQ/Prakt-Numerik)
>>  * [Acara 1 - Sistem Persamaan Linear simultaneous](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%201/Acara%201.md) [__[Download Here]__](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)
>>  * [Acara 2 - Sistem non linear dan mencari akar](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%202/Acara%202.md) [__[Download Here]__](https://drive.google.com/drive/folders/17aN5QrDvoH_QwJPU4YP9N5pLOv6nVo0q?usp=sharing)
>>  * [Acara 3 - Interpolasi dan kurva fitting](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%203/Acara%203.md) [__[Download Here]__](https://drive.google.com/drive/folders/1rDq2SUB0OCT58TML7OEPjWiuK4gC_GxT?usp=sharing)

---

 ## Interpolasi :
 ### A. Interpolasi Polinomial
 `Polinomial` orde ke-n digunakan sebagai interpolasi fungsi
<center>
<img src="https://render.githubusercontent.com/render/math?math=f(x)=b_0 %2Bb_1x %2Bb_2x^2 %2Bb_3x^3%2B\cdots%2Bb_nx^n ">
</center><br>

 Contoh :
Estimasi nilai `f(2.2)` dari data dibawah ini!
<center>

| _x_ | _f(x)_ |
|:----:|:----:|
| 1 | 1 |
| 2 | 8 |
| 3 | 27 |
| 4 | 64 |
</center>

Solusi :
Nilai `f(2.2)` diestimasi menggunakan interpolasi polinomial orde kedua:
<center>
<img src="https://render.githubusercontent.com/render/math?math=f(x)=b_0%2Bb_1x%2Bb_2x^2 ">
</center><br>

 Masukkan nilai `x=1`, `x=2`, dan `x=1` kita dapatkan 3 persamaan :

<center>
<img src="https://render.githubusercontent.com/render/math?math=b_0%2Bb_1%2Bb_2=1 "><br>
<img src="https://render.githubusercontent.com/render/math?math=b_0%2B2b_1%2B4b_2=8 "><br>
<img src="https://render.githubusercontent.com/render/math?math=b_0%2B3b_1%2B9b_2=27 ">
</center><br>

 Atau dalam bentuk matriks dapat diubah menjadi
<center>
<img src="https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture18.png?raw=True">
</center>

 Persamaan di atas dapat diselesaikan dengan eliminasi Gauss. Hasilnya kita dapatkan koefisien b<sub>0</sub> = 6, b<sub>1</sub> = -11, dan b<sub>2</sub> = 6. Interpolasi fungsi menjadi
<center>
<img src="https://render.githubusercontent.com/render/math?math=f(x)=6-11x%2B6x^2 ">
</center>

 Didapat estimasi nilai `f(2.2)`
<center>
<img src="https://render.githubusercontent.com/render/math?math=f(2.2)=6-11(2.2)%2B6(2.2)^2 "><br>
=10.83
</center>

 Dengan nilai error sebesar (fungsi sebenarnya adalah `f(x) = x3`
<center>
<img src="https://render.githubusercontent.com/render/math?math=err =\left\lvert{\frac{f(x)-f_r(x)}{f_r(x)}}\right\rvert"><br>
<img src="https://render.githubusercontent.com/render/math?math==\left\lvert{\frac{10.84-2.2^3}{2.2^3}}\right\rvert "><br>
=1.8%
</center>

 Di mana f(x) merupakan nilai estimasi _(estimated value)_, sedangkan f<sub>r</sub>(x) merupakan nilai sebenarnya _(exact value)

 ### B. Interpolasi Lagrange
 `Interpolasi Lagrange` untuk estimasi nilai f(x) didefinisikan sebagai:
<center>
<img src="https://render.githubusercontent.com/render/math?math=f(x)=\sum_{i=1}^{N%2B1}li(x)f(x_i) "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=l_i(x)=\prod_{j=1,j\ne i}^{N%2B1}\frac{x-x_j}{x_i-x_j} ">
</center>

 Dengan _li_ merupakan `interpolasi Lagrange` dan N adalah `orde polinomial`.
Misalkan untuk `orde polinomial` N=2
<center>
<img src="https://render.githubusercontent.com/render/math?math=f(x)=l_1(x)f(x_1)%2Bl_2(x)f(x_2)%2Bl_3(x)f(x_3) "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=l_1(x)=\frac{(x-x_2)(x-x_3)}{(x_1-x_2)(x_2-x_3)} "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=l_2(x)=\frac{(x-x_1)(x-x_3)}{(x_2-x_1)(x_2-x_3)} "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=l_3(x)=\frac{(x-x_1)(x-x_2)}{(x_3-x_1)(x_3-x_2)} ">
</center>

---

 ## Curve Fitting :
 Data-data yang bersifat diskrit dapat dibuat continuum melalui proses curve-fitting. Curve-fitting merupakan proses data-smoothing, yakni proses pendekatan terhadap kecenderungan data-data dalam bentuk persamaan model matematika.
Misalkan tersedia data-data `y` pada berbagai `x` (sejumlah `n` pasang), maka dapat dicari suatu persamaan `y = f(x)` yang memberikan hubungan `y` dengan `x` yang mendekati data. Proses ini disebut curve fitting.

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture1.png?raw=true">
</center><br>

 Langkah-langkah yang dapat ditempuh untuk menentukan persamaan empirik adalah sebagai berikut: 
1.	Membuat grafik `y` versus `x` berdasarkan data yang tersedia
1.	Meramalkan bentuk persamaan yang kira-kira sesuai (mengandung tetapan-tetapan yang belum diketahui), berdasarkan grafik Misal: 
>  *  Persamaan linier: <img src="https://render.githubusercontent.com/render/math?math=y=ax%20,%20y = a_0 %2B a_1x">
>  *  Persamaan kuadrat: <img src="https://render.githubusercontent.com/render/math?math=y = a_0%2Ba_1x%2Ba_2x^2"> 
>  *   Persamaan polinomial berorde-m: <img src="https://render.githubusercontent.com/render/math?math=y = a_0%2Ba_1 x%2Ba_2 x^2%2B... %2B a_{m-1} x^{m-1}%2Ba_m x^m">
>  *   Persamaan eksponensial: <img src="https://render.githubusercontent.com/render/math?math=y = a e^{bx}"> 
3.	Mengevaluasi nilai tetapan-tetapan tersebut berdasarkan data yang ada `Æ` regresi Secara garis besar, metode regresi ada 2 macam: __(a) regresi linier__ dan __(b) regresi non-linier__ 
4.	Mengevaluasi kesesuaian persamaan empirik terhadap data. 

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture2.png?raw=true">
</center><br>

 Cara mengevaluasi nilai-nilai tetapan dalam persamaan empirik: __visual inspection__, __method of average__, dan __metode kuadrat terkecil__ (_least squares_). Metode kuadrat terkecil merupakan metode yang paling banyak digunakan. Pada metode ini, nilai-nilai tetapan terbaik adalah yang memberikan jumlah kuadrat kesalahan/penyimpangan (_sum of squares of errors_, __SSE__) yang terkecil (minimum).

Bentuk persamaan linier: (1) y = a x dan (2) y = a<sub>0</sub> + a<sub>1</sub> x

---

 ### 1. Bentuk Persamaan: y=ax
 ingin dicari harga a (a biasa disebut sebagai slope)
Untuk pasangan data `xi`, `yi`, maka error-nya adalah:
<center><img src="https://render.githubusercontent.com/render/math?math=R_i=ax_i-y_i=y_{terhitung}-y_{data}"></center><br>

> sehingga nilai sum of squares of errors-nya: 
<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture3.png?raw=true"><br>
</center>

> Harga a terbaik adalah yang memberikan SSE minimum. Harga SSE akan minimum jika:
<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture4.png?raw=true" >
</center>

>> Sehingga: 
<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture5.png?raw=true" >
</center><br> 
<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture6.png?raw=true" >
</center><br>

>> Atau 
<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture7.png?raw=true" >
</center><br>

---

 ### 2.  Bentuk Persamaan: y = a<sub>0</sub> + a<sub>1</sub>x
 ingin dicari harga a<sub>0</sub> dan a<sub>1</sub> (a<sub>0</sub> biasa disebut sebagai intercept dan a<sub>1</sub> sebagai slope). Dengan cara yang sama, untuk pasangan data `xi`, `yi`, maka error-nya adalah:
<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture8.png?raw=true" >
</center>

> Sehingga nilai sum of squares of errors-nya:
<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture9.png?raw=true" >
</center><br>

> Harga SSE akan minimum jika: 

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture10.png?raw=true" >
</center><br>

>> Sehingga:

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture11.png?raw=true" >
</center><br>

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture12.png?raw=true" >
</center><br>

>> Dan 

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture13.png?raw=true" >
</center><br>

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture14.png?raw=true" >
</center><br>

> Berdasarkan persamaan (11) dan (12), maka harga `a_0` dan `a_1` ¬ dapat ditentukan. Misal, dengan menggunakan __Cramer’s rule__, diperoleh:

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture15.png?raw=true" >
</center><br>

> Maka:

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture16.png?raw=true" >
</center><br>

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture17.png?raw=true" >
</center>