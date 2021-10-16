print("---Program Menentukan Gaji Pokok dan Gaji Bersih---")
print("------------Karyawan Berdasar Golongan-------------")

# input kode, nama, golongan karyawan
kodeKaryawan = int(input("Masukkan kode karyawan          : "))
namaKaryawan = input("Masukkan nama karyawan    	: ")
golonganKaryawan = input("Masukkan golongan		: ")
print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------------------------")

# hasil input kode, nama, golongan, karyawan
print("Nama Karyawan                   : " + namaKaryawan + " (Kode : " + str(kodeKaryawan) + " )")
print("Golongan			: " + golonganKaryawan)
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

# muncul gaji pokok dan potongan dari aturan perhitungan gaji pokok
print("Gaji Pokok			: Rp " + str(gajiPokok))
print("Potongan (" + str(potongan) + " %)		: Rp " + str(gajiPokok*potongan/100))
print("----------------------------------------------------------- -")

# gaji pokok - potongan, masukkan rumus
print("Gaji Bersih			: Rp " + str(gajiPokok-(gajiPokok*potongan/100)))