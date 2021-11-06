print('===============================================')
print('Program Membuka - Menambahkan Data ke File Text')
print('===============================================')

namaFile = input('Masukkan nama file : ')
tambah = 'y'

try :
    file = open(namaFile, "r")
    while tambah == 'y' :
        dataYgDitambah = input('Data yang mau ditambahkan : ')
        file = open(namaFile, "a")
        file.write(dataYgDitambah)
        tambah = input('Mau lagi (y/n) : ')
        if tambah == 'n' :
            file.close()
            break
except FileNotFoundError :
    print('File tidak ditemukan')