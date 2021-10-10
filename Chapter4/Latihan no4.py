print("---Program Menghitung Waktu Sampai di kota C---")
print("-----------------------------------------------")

# input data
jarakKotaAB = int(input("masukkan jarak kota A - B (km) : "))
kecepatanKotaAB = int(input("masukkan rata- rata kecepatan kota A - B (km/jam) : "))
jarakKotaBC = int(input("masukkan jarak kota B - C (km) : "))
kecepatankotaBC = int(input("masukkan rata-rata kecepatan kota B - C (km/jam) : "))

# menghitung waktu
waktuJamKotaAB = jarakKotaAB//kecepatanKotaAB
waktuKotaAB2 = str(waktuJamKotaAB)
waktuMenitKotaAB = jarakKotaAB%kecepatanKotaAB
waktuMenitKotaAB2 = str(waktuMenitKotaAB)
print("lama waktu perjalanan kota A - B = " + waktuKotaAB2 + " jam " + waktuMenitKotaAB2 + " menit")
waktuJamKotaBC = jarakKotaBC//kecepatankotaBC
waktuJamKotaBC2 = str(waktuJamKotaBC)
waktuMenitKotaBC = jarakKotaBC%kecepatankotaBC
waktuMenitKotaBC2 = str(waktuMenitKotaBC)
print("lama waktu perjalanan kota B - C = " + waktuJamKotaBC2 + " jam " + waktuMenitKotaBC2 + " menit")

# input jam
waktuBerangkatJam = int(input("masukkan waktu berangkat (jam) : "))
waktuBerangkatMenit = int(input("masukkan waktu berangkat (menit) : "))
waktuIstirahatJam = int(input("masukkan lama istirahat (jam) : "))
waktuIstirahatMenit = int(input("masukkan lama istirahat (menit) : "))

if waktuBerangkatMenit >=60 :
    waktuBerangkatJam += 1
if waktuIstirahatMenit >=60 :
    waktuIstirahatJam += 1

# lama perjalanan total
totalLamaPerjalanan = waktuBerangkatJam + waktuJamKotaAB + waktuJamKotaBC + waktuIstirahatJam

waktuJamSampaiKotaC = waktuBerangkatJam + waktuJamKotaAB + waktuJamKotaBC + waktuIstirahatJam
waktuMenitSampaiKotaC = waktuBerangkatMenit + waktuMenitKotaAB + waktuMenitKotaBC + waktuIstirahatMenit
if waktuMenitSampaiKotaC >= 60 :
    waktuJamSampaiKotaC += 1
    waktuMenitSampaiKotaC -=60

waktuJamSampaiKotaC2 = str(waktuJamSampaiKotaC)
waktuMenitSampaiKotaC2 = str(waktuMenitSampaiKotaC)

print("Pak Amir sampai di kota C pada pukul = " + waktuJamSampaiKotaC2 + " : " + waktuMenitSampaiKotaC2)