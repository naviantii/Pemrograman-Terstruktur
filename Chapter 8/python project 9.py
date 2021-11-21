print('=======================================')
print('=====Program Menghitung Harga Buah=====')
print('=======================================')

# list
buah = {'apel' : 5000 ,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

# input data
print('')
namaBuah = input('Nama buah yang dibeli 	: ')
banyakKg = int(input('Berapa Kg		: '))

# hitung
data = buah.get(namaBuah, 0)
print('-------------------------------------------')
hasil = data * banyakKg

print('Total harga		: Rp ', hasil)