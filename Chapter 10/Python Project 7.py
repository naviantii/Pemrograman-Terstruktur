# mendapatkan file dan nilai keyword
file = input('Masukkan nama file : ')
keyword = int(input('Masukkan nilai n : '))

# membuka file
myFile = open (file, 'r')
readFile = myFile.read()

# mendapatkan nilai ASCII, ubah
list =[]
for x in readFile :
    if x.isalpha() :
        shift = ord(x)
        shift -= keyword
        if (shift < ord('A')) :
            shift += 26
        hasil = chr(shift)
    elif x.isspace() :
        hasil = chr(32)
    list += [hasil]

# buat file baru
newFile = open('hasil penyandian no.7.txt', 'w')

# memasukkan data ke file baru
newFile.write(''.join(list))
myFile.close()
newFile.close()