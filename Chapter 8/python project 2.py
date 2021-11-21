# function
def dataStat(x) :
    hasil = []
    a = sum(x[:])/len(x)
    hasil.append(a)
    b = max(x)
    hasil.append(b)
    c = min(x)
    hasil.append(c)
    print('Hasil rata-rata, nilai tertinggi, dan nilai terendah list x : ', hasil)

print('======================================')
print('=====Program Function dataStat(x)=====')
print('======================================')

# list bilangan, output
n = int(input('Masukkan nilai n : '))
x =[]
for i in range (n) :
    bil = int(input('Masukkan bilangan : '))
    if n == 0 :
        break
    else :
        x = x +[bil]
    i -= 1

print('')
print('List bilangan x :', x)
dataStat(x)
