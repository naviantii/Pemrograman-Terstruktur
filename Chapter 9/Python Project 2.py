def star(n) :
    print('')
    space = n*2-1
    for i in range(n) :
        print(('*' * (i*2+1)).center(space))

n = int(input('Masukkan nilai n : '))
star(n)