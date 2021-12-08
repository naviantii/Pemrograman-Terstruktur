# import modul
from datetime import *

tglskrg = datetime.date(datetime.now())

# membuka file
myFile = open ('data peminjaman buku perpus.txt', 'r')

# header
print('===============================================================')
print('===============DATA PEMINJAMAN BUKU PERPUSTAKAAN===============')
print('===============================================================')

# input nim dicari, output awal
print('')
kodeDicari= input('Masukkan Kode Member            :  ')

# membuat list isi data
kodeMember = []
namaMember = []
judulBuku = []
tglpinjam = []
tglhrskembali = []

for data in myFile :
    pecahData = data.split('|')
    kodeMember += [pecahData[0]]
    namaMember += [pecahData[1]]
    judulBuku += [pecahData[2]]
    tglpinjam += [pecahData[3]]
    tglhrskembali += [pecahData[4]]

# mencari kode member peminjam buku dari list data
if kodeDicari in kodeMember :
    x = kodeMember.index(kodeDicari)
    
    # hasil
    print('')
    print('Data Peminjaman Buku')
    print('Kode Member	        	: ', kodeMember[x])
    print('Nama Member		        : ', namaMember[x])
    print('Judul Buku 		        : ', judulBuku[x])
    print('Tanggal Mulai Peminjaman	: ', tglpinjam[x])
    print('Tanggal Maks Peminjaman      	: ', tglhrskembali[x].replace('\n', ''))
    print('Tanggal Pengembalian	        : ', str(tglskrg))
    
    # memisah data dari list
    pinjam = tglpinjam[x].split('-')
    for item in pinjam :
        thnPinjaman = pinjam[0]
        blnPinjaman = pinjam[1]
        tglPinjaman = pinjam[2]
    
    # menghitung keterlambatan dan denda
    selisih = tglskrg - date(int(thnPinjaman), int(blnPinjaman), int(tglPinjaman)) 
    selisihHari = selisih.days
    if selisihHari >= 7 :
        terlambat = selisihHari - 7
    else :
        terlambat = 0

    print('Terlambat                       : ', terlambat ,' hari')
    print('Denda			        :  Rp ', terlambat*2000)

else :
    print('')
    print('Data peminjaman tidak ditemukan.')
