# modul
import random

# function
def shuffleString (x, n) :
    print('')
    myList = list (x)
    hasil =[]
    i = 0
    while i < n :
        data = ''.join(random.sample(x, len(x)))
        if (data not in hasil) and (data != x) :
            hasil += [data]
            i += 1
    print ("randomString('", x, "', ", n, ") -> ", hasil)

# output awal
n = int(input('Masukkan nilai n : '))
x = input('Masukkan x (kata) : ')
x = str(x)

# call
shuffleString(x, n)
