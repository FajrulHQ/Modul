<center> <h1> Modul Praktikum Numerik </h1> </center>
<center> <h2> Acara 3. Curve Fitting </h2> </center>

* [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
* [Github](https://github.com/FajrulHQ/Prakt-Numerik)
    * [Acara 1 (Drive) - Sistem Persamaan Linear)](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)
    * [Acara 2 (Drive) - Persamaan Nonlinear](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
    * [Acara 3 (Drive) - Curve Fitting](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)

## Pengantar :
Data-data yang bersifat diskrit dapat dibuat continuum melalui proses curve-fitting. Curve-fitting merupakan proses data-smoothing, yakni proses pendekatan terhadap kecenderungan data-data dalam bentuk persamaan model matematika.

Misalkan tersedia data-data $y$ pada berbagai $x$ (sejumlah $n$ pasang), maka dapat dicari suatu persamaan $y = f(x)$ yang memberikan hubungan $y$ dengan $x$ yang mendekati data. Proses ini disebut curve fitting.

<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture1.png?raw=true">
</center><br>

Langkah-langkah yang dapat ditempuh untuk menentukan persamaan empirik adalah sebagai berikut: 

1.	Membuat grafik $y$ versus $x$ berdasarkan data yang tersedia

1.	Meramalkan bentuk persamaan yang kira-kira sesuai (mengandung tetapan-tetapan yang belum diketahui), berdasarkan grafik Misal: 

    *  Persamaan linier: $y = a x ; y = a_0 + a_1x$ 

    *  Persamaan kuadrat: $y = a_0 + a_1 x + a_2 x^2$ 
    
    *   Persamaan polinomial berorde-m: $y = a_0 + a_1 x + a_2 x^2 + ... + a_{m-1} x^{m-1} + a_m x^m$
    
    *   Persamaan eksponensial: $y = a e^{bx}$ 
1.	Mengevaluasi nilai tetapan-tetapan tersebut berdasarkan data yang ada $Æ$ regresi Secara garis besar, metode regresi ada 2 macam: __(a) regresi linier__ dan __(b) regresi non-linier__ 

1.	Mengevaluasi kesesuaian persamaan empirik terhadap data. 


<center>
<img alt="Acara 3" src = "https://github.com/FajrulHQ/pict/blob/main/Acara%203/Picture2.png?raw=true">
</center><br>

Cara mengevaluasi nilai-nilai tetapan dalam persamaan empirik: __visual inspection__, __method of average__, dan __metode kuadrat terkecil__ (_least squares_). 

Metode kuadrat terkecil merupakan metode yang paling banyak digunakan. Pada metode ini, nilai-nilai tetapan terbaik adalah yang memberikan jumlah kuadrat kesalahan/penyimpangan (_sum of squares of errors_, __SSE__) yang terkecil (minimum).

Bentuk persamaan linier: (1) $y = a x$ dan (2) $y = a_0 + a_1 x$

1. Bentuk Persamaan: $y=ax$
 
ingin dicari harga a (a biasa disebut sebagai slope)
Untuk pasangan data $xi$, $yi$, maka error-nya adalah:

$$R_i= a x_i- y_i	=y_{terhitung }- y_{data}$$

sehingga nilai sum of squares of errors-nya: 

$$∑_{i=1}^n(a x_i- y_i)^2=f(a)$$

Harga a terbaik adalah yang memberikan SSE minimum. Harga SSE akan minimum jika:

$$\frac{d(SSE)}{d a}=0$$

Sehingga: 

$$\frac{d(SSE)}{d a}= \sum_{i=1}^n 2(a x_i- y_i )x_i=0$$
$$a\sum(x_i)^2- \sum(x_i y_i)= 0$$

Atau 

$$a=\sum\frac{x_i y_i}{(x_i)^2}$$

2.  Bentuk Persamaan: $y = a_0 + a_1 x$

ingin dicari harga $a_0$ dan $a_1$ ($a_0$ biasa disebut sebagai intercept dan $a_1$ sebagai slope). 
Dengan cara yang sama, untuk pasangan data $xi$, $yi$, maka error-nya adalah:

$$R_i=a_0+ a_1  x_i-y_i =y_{terhitung}- y_{data}$$

Sehingga nilai sum of squares of errors-nya:

$$SSE= \sum_{i=1}^n(a_0+a_1 x_i- y_i)^2=f(a_0,a_1)$$

Harga SSE akan minimum jika: 

$$\frac{∂(SSE)}{∂a_0}=0 ;   \frac{∂(SSE)}{∂a_1 }=0$$

Sehingga:

$$\frac{∂(SSE)}{∂a_0 } =\sum_{i=1}^n2(a_0+a_1 x_i- y_i ).1=0$$

$$na_0+ a_1 \sum x_i= \sum y_i$$

Dan 

$$\frac{∂(SSE)}{∂a_1 }= \sum_{i=1}^n2(a_0+a_1 x_i- y_i ).x_i=0$$

$$a_0 \sum x_i+ a_1 \sum x_i^2 = \sum x_i y_i$$
<br>

Berdasarkan persamaan (11) dan (12), maka harga $a_0$ dan $a_1$ ¬ dapat ditentukan. Misal, dengan menggunakan __Cramer’s rule__, diperoleh:

$$\begin{bmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{bmatrix} \begin{bmatrix} a_0\\a_1 \end{bmatrix} = \begin{bmatrix} \sum y_i \\ \sum x_i y_i \end{bmatrix}$$

Maka:

$$a_0=  \frac{∆_1}{∆}=  \frac{\begin{vmatrix}\sum y_i & \sum x_i \\ \sum x_iy_i &\sum x_i^2\end{vmatrix}}{\begin{vmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{vmatrix}} =  \frac {\sum y_i \sum x_i^2 }{ n \sum x_i^2 - (\sum x_i^2)}$$

$$a_1=  \frac{∆_2}{∆}=  \frac{\begin{vmatrix}n & \sum y_i \\ \sum x_i &\sum x_iy_i \end{vmatrix}}{\begin{vmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{vmatrix}} =  \frac {n\sum x_iy_i - \sum y_i \sum x_i }{ n \sum x_i^2 - (\sum x_i^2)}$$