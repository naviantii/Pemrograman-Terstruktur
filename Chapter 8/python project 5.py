print('=========================')
print('=====Program Kuadrat=====')
print('=========================')
print('')

def kuadrat(bil) :
    bil1 = []
    i = len(bil)
    for i in range (len(bil)) :
        hasil = bil[i]**2
        bil1 = bil1 + [hasil]
    print('')
    print('Hasil kuadrat = ', bil1)

n = int(input('Masukkan nilai n = '))
bil = []
for i in range (n) :
    bilangan = int(input('Masukkan bilangan : '))
    if n == 0 :
        break
    else :
        bil = bil + [bilangan]
    i -= 1

kuadrat(bil)