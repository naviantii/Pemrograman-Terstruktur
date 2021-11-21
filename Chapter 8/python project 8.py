def rerata(buah):
    data = list(buah.values())
    sum = 0
    for i in range (len(data)) :
        sum += data[i]
        if i == len(data) :
            break
        i += 1
    
    hasil = sum/len(data)
    print(hasil)


buah = {'apel' : 5000 ,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

rerata(buah)