hitung = 0
sum =0
for i in range(1, 100, 2) :
    bil= i
    if bil+2 :
        hitung = hitung+1
        sum = sum+bil
        print(bil)

print('')
print('Banyaknya bilangan ganjil : ' + str(hitung))
print('Jumlah seluruh bilangan : ' + str(sum))