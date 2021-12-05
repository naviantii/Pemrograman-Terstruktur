# membuka file dan membaca isi file
myFile = open('file.txt', 'r')
isi = myFile.readlines()

# menentukan bilangan ganjil genap
genap =[]
ganjil =[]
for i in range (len(isi)) :
    data = isi[i].replace('\n', '')
    if (int(data)%2 == 0) :
        genap += [data]
    elif (int(data)%2 != 0):
        ganjil +=[data]

# menutup file
myFile.close()

# output
print('Banyaknya bilangan genap : ', len(genap))
print('Banyaknya bilangan ganjil : ', len(ganjil))