def hargaMahal(buah) :
    urutan = sorted(buah.items(),key=lambda x:x[1], reverse = True)
    print(urutan[0][0])

buah = {'apel' : 5000 ,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

hargaMahal(buah)