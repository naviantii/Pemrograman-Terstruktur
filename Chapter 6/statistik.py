# function sum parameter tidak terbatas
def penjumlahan(*myData):

    # value
    sum = 0

    # input myData
    for data in myData :
        sum += data
    
    hasil = sum
    print('Hasil penjumlahannya : ' + str(hasil))


# function average parameter tidak terbatas
def ratarata(*myData):

    # value
    sum = 0
    i = 0

    # input myData
    for data in myData :
        sum += data
        i += 1
    
    hasil = sum/i
    print('Hasil rata-ratanya : ' + str(hasil))


# function max parameter tidak terbatas
def maksimum(*myData):

    # input myData
    for data in myData :
        hasil = max(data)
    
    print('Nilai maksimumnya : ' + str(hasil))


# function min parameter tidak terbatas
def minimum(*myData):

    # input myData
    for data in myData :
        hasil = min(data)
    
    print('Nilai minimumnya : ' + str(hasil))