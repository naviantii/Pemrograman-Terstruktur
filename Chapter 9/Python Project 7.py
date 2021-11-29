# data mhs
mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

# memecah string menjadi substring
data =[]
for i in range (len(mhs)) :
    splitData = mhs[i].split(':')
    data += [splitData]

# mengubah urutan tanggal lahir
for i in range (len(data)) :
    data[i][2] = data[i][2].split('-')

print('===========================================================================')
print('NIM      NAMA MAHASISWA          TGL LAHIR                    TEMPAT LAHIR')
print('---------------------------------------------------------------------------')

for i in range (len(data)) :
    print(data[i][0].ljust(9), end ='')
    print(data[i][1].ljust(24), end ='')
    print (data[i][2][2], '/', data[i][2][1], '/', data[i][2][0].ljust(20), end='')
    print(data[i][3].ljust(1))

print('---------------------------------------------------------------------------')