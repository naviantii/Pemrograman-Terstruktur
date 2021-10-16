print("---Program Menentukan Gaji Pokok dan Gaji Bersih---")
print("------------Karyawan Berdasar Golongan-------------")
print("")

# input kode, nama, golongan karyawan
kodeKaryawan = int(input("Masukkan kode karyawan                  : "))
namaKaryawan = input("Masukkan nama karyawan    	        : ")
golonganKaryawan = input("Masukkan golongan		        : ")
statusKaryawan = int(input("Masukkan status (1: menikah, 2: blm)	: "))
if (str(statusKaryawan) == '1'):
    jumlahAnak = int(input("Masukkan jumlah anak			: "))

print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")

# hasil input kode, nama, golongan, karyawan
print("Nama Karyawan                   : " + namaKaryawan + " ( Kode : " + str(kodeKaryawan) + " )")
print("Golongan			: " + golonganKaryawan)
print("Status Menikah			: " + str(statusKaryawan))
if (statusKaryawan == 1) :
    print("Jumlah Anak			: " + str(jumlahAnak))
print("-----------------------------------------------------------")

# aturan perhitungan gaji pokok
if (golonganKaryawan == 'A') or (golonganKaryawan == 'a') :
    gajiPokok = 10000000
    potongan = 2.5
elif (golonganKaryawan == 'B') or (golonganKaryawan == 'b') :
    gajiPokok = 8500000
    potongan = 2.0
elif (golonganKaryawan == 'C') or (golonganKaryawan == 'c') :
    gajiPokok = 7000000
    potongan = 1.5
elif (golonganKaryawan == 'D') or (golonganKaryawan == 'd') :
    gajiPokok = 5500000
    potongan = 1.0

# perhitungan gaji dengan tunjangan
if (statusKaryawan == 1) :
    tunjanganIstriSuami = 10/100
if (statusKaryawan == 1):
     if (jumlahAnak >= 1) :
         tunjanganAnak = 5/100

# muncul gaji pokok dan potongan dari aturan perhitungan gaji pokok
print("Gaji Pokok			: Rp " + str(gajiPokok))
if (statusKaryawan == 1):
    print("Tunjangan Istri/Suami		: Rp " + str(gajiPokok*tunjanganIstriSuami))
    if (jumlahAnak >=1) :
        print("Tunjangan anak			: Rp " + str((gajiPokok*tunjanganAnak)*jumlahAnak))
print("----------------------------------------------------------- +")

if (statusKaryawan == 1):
    gajiKotor = gajiPokok + (gajiPokok*tunjanganIstriSuami) + (gajiPokok*tunjanganAnak)*jumlahAnak
elif (statusKaryawan ==2):
    gajiKotor = gajiPokok

print("Gaji Kotor			: Rp " + str(gajiKotor))
print("Potongan (" + str(potongan) + " %)		: Rp " + str(gajiKotor*potongan/100))
print("----------------------------------------------------------- -")

# gaji kotor - potongan, masukkan rumus
print("Gaji Bersih			: Rp " + str(gajiKotor-(gajiKotor*potongan/100)))