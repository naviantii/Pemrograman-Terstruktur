print('=======================================')
print('=====Program Menghitung Harga Buah=====')
print('=======================================')

# list
buah = {'apel' : 5000 ,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

# loop
harga =[]
while True :
    print('')
    namaBuah = input('Nama buah yang dibeli 	: ')
    banyakKg = int(input('Berapa Kg		: '))
    
    data = buah.get(namaBuah, 0)
    hasil = banyakKg * data
    harga += [hasil]

    print('')
    tambah = input('Beli buah yang lain (y/n) ? ')
    if (tambah == 'n') or (tambah == 'N') :
        break

# hitung
sum = sum(harga)
print('-------------------------------------------')
print('Total harga		: Rp ', sum)