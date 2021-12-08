# import modul
from datetime import *

# membuat file
myFile = open('data peminjaman buku perpus.txt', 'a+')

# header
print('================================')
print('=====DATA BUKU PERPUSTAKAAN=====')
print('================================')

# input data
while True :
    print('')
    kodeMember = input('Masukkan Kode Member	: ')
    namaMember = input('Masukkan Nama Member	: ')
    judulBuku = input('Masukkan Judul Buku 	: ')
    tglskrg = datetime.date(datetime.now())
    tglkembali = tglskrg + timedelta(days=7)

    data = kodeMember + '|' + namaMember + '|' + judulBuku + '|' + str(tglskrg) + '|' + str(tglkembali) + '\n'
    myFile.write(data)

    print('')
    tambah = input('Ulangi lagi (y/n)	: ')
    if (tambah == 'n') or (tambah == 'N') :
        print('')
        print('Terima kasih, data telah berhasil diinput.')
        break

# menutup file
myFile.close()