print('=============================')
print('===Mahasiswa PTIK UNS 2021===')
print('=============================')
print('')

n = int(input('Masukkan jumlah mahasiswa : '))
namaMahasiswa = []
for i in range (n) :
    mhs = input('Masukkan nama mahasiswa : ')
    if n == 0 :
        break
    else :
        namaMahasiswa = namaMahasiswa + [mhs]
    i -= 1
namaMahasiswa.sort()
print('')
print('Mahasiswa : ')

i = 0
for i in range (n) :
    karakter = len(namaMahasiswa[i])
    if i == n :
        break
    else :
        print(namaMahasiswa[i], '(', karakter, ' karakter )')
    i += 1 