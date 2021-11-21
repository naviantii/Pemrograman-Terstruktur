print('==================================')
print('===Program Mengurutkan Bilangan===')
print('==========Besar ke Kecil==========')
print('==================================')
print('')

n = int(input('Masukkan nilai n : '))
bilBulat = []
for i in range (n) :
    bil = int(input('Masukkan bilangan bulat : '))
    if n == 0 :
        break
    else :
        bilBulat = bilBulat + [bil]
    i -= 1

bilBulat.sort(reverse=True)
print('')
print('Bilangan bulat : ', bilBulat)