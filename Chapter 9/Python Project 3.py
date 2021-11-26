def star(n) :
    print('')
    space = n*2-1
    for i in range(int(n/2)) :
        print(('*' * (i*2+1)).center(space))
    for i in reversed (range(int(n/2+1))) :
        print(('*' * (i*2+1)).center(space))

n = int(input('Masukkan nilai n : '))
star(n)