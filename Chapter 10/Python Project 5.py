# membuka isi file, membaca
myFile = open('bilangan.txt', 'r')

# split data text
list = []
readData = myFile.readlines()

# memecah data
hasil = []
i = 0
for i in range (len(readData)) :
    split = readData[i].split('|')
    data = [int(split[0]), int(split[1].replace('\n',''))]
    hasil += [data]

# buat file baru
newFile = open('hasil penjumlahan.txt', 'w')

# memasukkan data ke file baru
for i in range (len(hasil)) :
    penjumlahan = sum (hasil[i])
    newFile.write(str(penjumlahan) + '\n')

# menutup file
myFile.close()
newFile.close()
