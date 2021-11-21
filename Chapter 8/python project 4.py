print('============================')
print('=====Program Data Sayur=====')
print('============================')

#data sayur
sayur = ['bayam', 'kangkung', 'wortel', 'selada']

#output awal
print('')
print('Menu : ')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
print('')
pilihan = input('Pilihan Anda : ')
if (pilihan == 'A') or (pilihan == 'a') :
    print('')
    tambah = input('Masukkan data yang akan ditambah : ')
    sayur.append(tambah)
    print('Data sayur : ', sayur)
elif (pilihan == 'B') or (pilihan == 'b') :
    print('')
    try :
        hapus = input('Masukkan data yang akan dihapus : ')
        sayur.remove(hapus)
        print('Data sayur : ', sayur)
    except ValueError :
        print('Data tidak ditemukan.')
elif (pilihan == 'C') or (pilihan == 'c') :
    print('')
    print('Data sayur : ', sayur)
else :
    print('Maaf, pilihan tidak tersedia.')