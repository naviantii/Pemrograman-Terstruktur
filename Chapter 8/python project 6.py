def sortStringByChar(myData) :
    myData.sort(reverse= True, key=len)
    return myData


def buah() :
    n = int(input('Masukkan nilai n : '))
    myData = []
    for i in range (n) :
        data = input('Masukkan data (string) : ')
        if n == 0 :
            break
        else :
            myData = myData + [data]
        i -= 1
    return myData

myData = buah()
hasil = sortStringByChar(myData)

print('')
print('List myData :', myData)
print('Hasil dari list : ', hasil)