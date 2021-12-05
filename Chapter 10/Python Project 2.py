print('------------------------------------------')
print('---Program Membaca Input Data Mahasiswa---')
print('------------------------------------------')

# membuka / membuat file
myFile = open('datamahasiswa.txt', 'a+')

# input data
while True :
    print('')
    nim = input('Masukkan NIM		: ')
    nama = input('Masukkan Nama Mhs	: ')
    alamat = input('Masukkan Alamat         : ')

    data = nim + '|' + nama + '|' + alamat + '\n'
    myFile.write(data)
    
    print('')
    tambah = input('Ulangi input lagi (y/n) : ')
    if (tambah == 'n') or (tambah == 'N') :
        break

# menutup file
myFile.close()