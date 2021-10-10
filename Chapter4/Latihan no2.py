# script menghitung banyak liter bensin untuk perjalanan
print("-----Program Menghitung Bensin yang Diperlukan-----")
print("---------------------------------------------------")

jarak = int(input("masukkan jarak (km) : "))
konsumsiBBM = 1/12

banyakLiterBensin = jarak * konsumsiBBM
banyakLiterBensin = str(banyakLiterBensin)
print("banyaknya harus mengisi bensin : " + banyakLiterBensin)