print('===================================================')
print('Program Membuka, Membaca, Menampilkan Isi File Text')
print('===================================================')

try :
    namaFile = input('Masukkan nama file : ')
    file = open(namaFile, "r")
    print('Isi file ' + namaFile + ' adalah : ')
    print(file.read())
except FileNotFoundError :
    print('File tidak ditemukan')