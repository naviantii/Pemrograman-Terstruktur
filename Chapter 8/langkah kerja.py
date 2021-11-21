# nomor 1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

# nomor 2
a.insert(3, 10)
b.insert(2, 15)
# --cek
print('a = ', a)
print('b = ', b)

# nomor 3
a.append(4)
b.append(8)
# --cek
print('a = ' , a)
print('b = ' , b)

# nomor 4
a.sort()
b.sort()
# --cek
print('a = ' , a)
print('b = ' , b)

# nomor 5
c = a[0:8]
d = b[2:10]
# --cek
print('c = ' , c)
print('d = ' , d)

# nomor 6

i = 0
e = []

for i in range (len(c)) :
    bil = c[i] + d[i]
    tambah = sum([bil])
    if i == 8 :
        break
    else :
        e = e + [tambah]
    i += 1
print('e = ' , e)


# nomor 7
eTuple = tuple(e)
print('e = ' , eTuple)

# nomot 8
minimal = min(eTuple)
maksimal = max(eTuple)
jumlah = sum(eTuple)

print('min : ', minimal)
print('maks : ', maksimal)
print('jumlahan : ', jumlah)

# nomor 9
myString = 'python adalah bahasa pemrograman yang menyenangkan'

# nomor 10
huruf = set(myString)

print('karakter huruf : ', huruf)

# nomor 11
myString2 = list(huruf)
myString2.sort()
print('karakter huruf : ', myString2)
