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