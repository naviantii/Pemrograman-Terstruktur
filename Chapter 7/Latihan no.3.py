print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')


sum = 0
i = 0
tambah = 'y'
while tambah == 'y' :
    try :
        bil = int(input('Masukkan bilangan bulat : '))
        sum += bil
        i += 1
        tambah = input('Lagi (y/n)? : ')
    except ValueError :
        print('Bukan bilangan bulat')
    if tambah == 'n' :
        break

print('')
hasil = sum/i
print('Rata-ratanya adalah: ' + str(hasil))