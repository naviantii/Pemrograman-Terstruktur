# script menghitung berapa minimal mengisi bensin
print("---Program Menghitung Mengisi Bensin---")
print("---------------------------------------")

jarak = int(input("masukkan jarak (km) : "))
konsumsiBBM = 1/12
kapasitasTangki = 50

banyakMengisiBensin = jarak * konsumsiBBM / kapasitasTangki
banyakMengisiBensin = str(banyakMengisiBensin)
print("minimal harus mengisi bensin : " + banyakMengisiBensin)