def jumlah (a, b) :
    hasil = a + b
    return hasil

def kali (a, b) :
    hasil = a * b
    return hasil

def kurang (a, b ) :
    hasil = a - b
    return hasil

def bagi (a, b) :
    hasil = a / b
    return hasil

a = jumlah(2, kali(4,6))
b = kurang(0, 4)
print('Hasil dari 2+4*6-4 adalah ', jumlah(a,b))

a = jumlah(4, 7)
b = kurang(6, 9)
print('Hasil dari (4+7)*(6-9) adalah ', kali(a, b))

a = bagi(jumlah (10, 2), jumlah(7, 5))
b = kurang(12,34)
print('Hasil dari (10+2)/(7+5)/(12-34) adalah ', bagi(a, b))