print("Hai.. nama saya Mr.Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
print("")

from random import randint
bil = randint (0, 100)
score = 100
while True :
    tebakan = int(input('Tebakan Anda: '))
    if (tebakan != bil) :
       score = score - 2 
    if (tebakan == bil) :
        print("Yeeee… Bilangan tebakan anda BENAR :-)") 
        break
    if (tebakan >= bil) :
        print("Hehehe... Bilangan tebakan anda terlalu besar")
    elif (tebakan <= bil) :
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
    if (score == 0) :
        break
 
 
print("")
print("Score Anda : " + str(score))