# membuka file
myFile = open ('datamahasiswa.txt', 'r')

# input nim dicari, output awal
nimDicari= input('Masukkan NIM yang mau dicari : ')

# membuat list isi data
nim =[]
nama = []
alamat= []

for data in myFile :
    pecahData = data.split('|')
    nim += [pecahData[0]]
    nama += [pecahData[1]]
    alamat += [pecahData[2]]

# mencari nim dari list data
if nimDicari in nim :
    x = nim.index(nimDicari)
    
    # hasil
    print('')
    print('Data Mahasiswa')
    print('NIM      : ',nim[x])
    print('Nama     : ', nama[x])
    print('Alamat   : ', alamat[x])
else :
    print('Data mahasiswa tidak ditemukan.')
