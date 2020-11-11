<center> 

# Modul Praktikum Numerik
## Acara 4. Differensiasi dan Integrasi
</center>

> ### Link Modul
> * [Google Drive](https://drive.google.com/drive/folders/1uMaBNZ2VWBWpx080plEPaRVnLfh66UfH?usp=sharing)
> * [Github](https://github.com/FajrulHQ/Prakt-Numerik)
>>  * [Acara 1 - Sistem Persamaan Linear simultaneous](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%201/Acara%201.md) [__[Download Here]__](https://drive.google.com/drive/u/0/folders/1183IOE2AyPF-gyQVuzTEYEBTQUtLgtzp)
>>  * [Acara 2 - Sistem non linear dan mencari akar](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%202/Acara%202.md) [__[Download Here]__](https://drive.google.com/drive/folders/17aN5QrDvoH_QwJPU4YP9N5pLOv6nVo0q?usp=sharing)
>>  * [Acara 3 - Interpolasi dan kurva fitting](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%203/Acara%203.md) [__[Download Here]__](https://drive.google.com/drive/folders/1rDq2SUB0OCT58TML7OEPjWiuK4gC_GxT?usp=sharing)
>>  * [Acara 4 - Differensiasi dan Integrasi](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/Acara%204/Acara%204.md) [__[Download Here]__](https://drive.google.com/drive/folders/1eFA36m0f2kSgOjpuxNCS9V24IvUXwtKP)

---

## Finite Difference
###  1. Deret Taylor : <br>
<img src="https://render.githubusercontent.com/render/math?math=f(x%2B\Delta x)=f(x)%2B\frac{d f(x)}{d x} \Delta x%2B\frac{d^{2} f(x)}{d x^{2}} \frac{(\Delta x)^{2}}{2 !}%2B\frac{d^{3} f(x)}{d x^{3}} \frac{(\Delta x)^{3}}{3 !}%2B\cdots"><br><br>

###  2. Forward Finite-Difference :<br>
<img src="https://render.githubusercontent.com/render/math?math=f'(x)=\frac{f(x%2Bh)-f(x)}{h}"><br><br>

###  3. Backward Finite-Difference :<br> 
<img src="https://render.githubusercontent.com/render/math?math=f'(x)=\frac{f(x)-f(x-h)}{h}"><br><br>

###  4. Central Finite-Difference :<br> 
<img src="https://render.githubusercontent.com/render/math?math=f'(x)=\frac{f(x%2Bh)-f(x-h)}{2h}"><br><br>

 Contoh : <br> Diketahui persamaan :<br>
<img src="https://render.githubusercontent.com/render/math?math=f(x)=e^{-x^2},-6\leq x\leq6"><br> 
Cari nilai differensiasi dengan nilai `x=[-6, -5.8,...., 5.8, 6]`menggunakan metode `Central Finite Difference`!

### Penerapan di Geofisika

<center>

![contoh1](../pict/Acara%204/contoh1.jpeg)<br>
<b> Gambar 1.</b> Penyelesaian derivatif
</center>

---

## Integral
### 1. Integrasi<br>
>Secara bahasa, integral berarti menggabungkan bagian-bagian sehingga membentuk suatu keseluruhan. Secara matematis, Integral berarti mencari nilai luasan di bawah sebuah kurva pada suatu batas, yang dipresentasikan dalam bentuk:<br>
<center>
<img src="https://render.githubusercontent.com/render/math?math=\int_a^b f(x)dx"> <br><br>
</center>

<center>

  ![Acara 4](https://github.com/FajrulHQ/Prakt-Numerik/blob/main/pict/Acara%204/Picture1.png?raw=true)<br>
  <b> Gambar 2.</b> Integral merupakan luasan dibawah suatu kurva f(x) pada a dan b
</center>

### 2. Metode Trapeziodal<br>
> `Metode Trapezoidal` didasarkan oleh formula `Newton-Cotes`, di mana integrand diasumsikan sebagai suatu polinomial orde 1

<center>
<img src="https://render.githubusercontent.com/render/math?math=\int_a^b f(x)dx\approx \int_a^b f_1(x)dx"><br><br>
<img src="https://render.githubusercontent.com/render/math?math==\int_a^b(a_0%2Ba_1x)dx"><br><br>
<img src="https://render.githubusercontent.com/render/math?math==a_0(b-a)%2Ba_1(\frac{b^2-a^2}{2})">
</center><br>

>> Lalu, jika kita andaikan terdapat garis lurus pada `(a, f(a))` dan `(b, f(b))`, maka

<center>
<img src="https://render.githubusercontent.com/render/math?math=f(a)=f_1(a)=a_0%2Ba_1a"><br><br>
<img src="https://render.githubusercontent.com/render/math?math=f(b)=f_1(a)=a_0%2Ba_1b">
</center><br>

>> Dari kedua persamaan tersebut, diperoleh
<center>
<img src="https://render.githubusercontent.com/render/math?math=a_1=\frac{f(b)-f(a)}{b-a}"><br>
<img src="https://render.githubusercontent.com/render/math?math=a_0=\frac{f(a)b-f(b)a}{b-a}">
</center><br>

>> Maka integral `f(x)` dapat didekati dengan
<center>
<img src="https://render.githubusercontent.com/render/math?math=\int_a^b f_1(x)dx\approx \frac {f(a)b-f(b)a}{b-a}(b-a) %2B \frac{f(b)-f(a)}{b-a}\frac{b^2-a^2}{2} "><br><br>
<img src="https://render.githubusercontent.com/render/math?math==(b-a)\frac{f(a)%2Bf(b)}{2} ">
</center><br>

>> Jika <img src="https://render.githubusercontent.com/render/math?math=h=\frac{b-a}{2} "> maka 
<center>
<img src="https://render.githubusercontent.com/render/math?math=\int_a^bf_1(x)dx=\frac{h}{2}[f(a)%2Bf(b)] ">
</center><br>

### 3. Metode Simpson's 1/3<br>
> `Metode Simpson’s 1/3` merupakan pengembangan dari metode Trapezoidal. Pada metode Trapezoidal integrand diasumsikan sebagai polinomial orde 1. Sedangkan pada `metode Simpson’s 1/3` integrand diasumsikan sebagai polinomial orde 2.
<center>
<img src="https://render.githubusercontent.com/render/math?math=\int_a^bf(x)dx\approx \int_a^bf_2(x)dx "><br><br>
<img src="https://render.githubusercontent.com/render/math?math==\int_a^b(a_0%2Ba_1x%2Ba_2x^2)dx "><br><br>
<img src="https://render.githubusercontent.com/render/math?math==a_0(b-a)%2Ba_1\frac{b^2-a^2}{2}%2Ba_2\frac{b^3-a^3}{3} ">
</center><br>

>> Pada <img src="https://render.githubusercontent.com/render/math?math=a_0,a_1 \: \textrm{dan} \: a_2 "> dengan masing-masing titik diasumsikan dalam <img src="https://render.githubusercontent.com/render/math?math=(a,f(a),(\frac{a%2Bb}{2},f(\frac{a%2Bb}{2})) "> dan <img src="https://render.githubusercontent.com/render/math?math=(b,f(b)) ">, maka

<center>
<img src="https://render.githubusercontent.com/render/math?math=f(a)=f_1(a)=a_0%2Ba_1a%2Ba_2a "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=f(\frac{a%2Bb}{2})=a_0%2Ba_1\frac{a%2Bb}{2}%2Babf(a)%2Bb^2f(a) "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=f(b)=f_(b)=a_0%2Ba_1b%2Ba_2b ">
</center><br>

>> Didapatkan <img src="https://render.githubusercontent.com/render/math?math=a_0,a_1 \: \textrm{dan} \: a_2 "> sebagai berikut

<center>
<img src="https://render.githubusercontent.com/render/math?math=a_0=\frac{a^2f(b)%2Babf(b)-4abf(\frac{a%2Bb}{2})%2Babf(a)%2Bb^2f(a)}{a^2-2ab%2Bb^2} "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=a_0=\frac{af(a)-4af(\frac{b%2Ba}{2})%2B3af(b)%2B3bf(a)-4bf(\frac{b%2Ba}{2})%2Bbf(b)}{a^2-2ab%2Bb^2} "><br><br>
<img src="https://render.githubusercontent.com/render/math?math=a_2=\frac{2f(a)-2f(\frac{b%2Ba}{2})%2Bf(b)}{a^2-2ab%2Bb^2} ">
</center><br>

>> Maka integralnya menjadi
<center>
<img src="https://render.githubusercontent.com/render/math?math=\int_a^bf_2(x)\approx\frac{b-a}{6}[f(a)%2B4f\frac{a%2Bb}{2}%2Bf(b)] ">
</center><br>

Sebelumnya kita mengasumsikan bahwa interval `[a,b]` dibagi menjadi 2 segement, dengan lebar segment
<center>
<img src="https://render.githubusercontent.com/render/math?math=h=\frac{b-a}{2} ">
</center><br>

Membuat persamaan integral menjadi seperti berikut
<center>
<img src="https://render.githubusercontent.com/render/math?math=\int_a^bf(x)dx=\frac{h}{3}[f(a)%2B4\sum_{i=1,3,5}^{n-1}f_i%2Bf(b)] ">
</center><br>

>> Karena terdapat persamaan <img src="https://render.githubusercontent.com/render/math?math=\frac{h}{3} "> , oleh sebab itu algoritma ini disebut sebagai `Simspson’s 1/3`

<center>

![contoh1](../pict/Acara%204/contoh2.jpeg)<br>
<b> Gambar 3.</b> Chargeability
</center>