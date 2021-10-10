print ("-----Program Menghitung Total Tarif-----")
print ("---------Sewa Mobil TeuBengkel----------")
print ("----------------------------------------")

# input data
tarif12JamPertama = 200000
tarif1JamBerikutnya = 10000

# input waktu
print("---memasukkan waktu masuk---")
jamAwalJam = int(input("masukkan jam masuk, jam : "))
jamAwalMenit = int(input("masukkan jam masuk, menit : "))
jamAwalDetik = int(input("masukkan jam masuk, detik : "))

print("---memasukkan waktu keluar---")
jamAkhirJam = int(input("masukkan jam keluar, jam : "))
jamAkhirMenit = int(input("masukkan jam keluar, menit : "))
jamAkhirDetik = int(input("masukkan jam keluar, detik : "))

waktuAwal =jamAwalJam + jamAwalMenit * 1/60 + jamAwalDetik * 1/3600
waktuAkhir =jamAkhirJam + jamAkhirMenit * 1/60 + jamAkhirDetik * 1/3600

waktuTotal = waktuAkhir - waktuAwal
if waktuTotal>12 :
    waktuTotal2 = waktuTotal % 12

totalTarif = tarif12JamPertama
if waktuTotal>12 :
    totalTarif = tarif12JamPertama + tarif1JamBerikutnya * waktuTotal2

totalTarif = str(totalTarif)

print("total tarif : " + totalTarif)