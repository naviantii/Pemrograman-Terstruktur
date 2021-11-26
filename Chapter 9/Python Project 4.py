# modul
import random

# function
def shuffleString (x, n) :
    print('')
    myList = list (x)
    hasil =[]
    for i in range (n) :
        random.shuffle(myList)
        data = ''.join(myList)
        hasil += [data]
    print ("randomString('", x, "', ", n, ") -> ", hasil)

# output awal
n = int(input('Masukkan nilai n : '))
x = input('Masukkan x (kata) : ')
x = str(x)

# call
shuffleString(x, n)