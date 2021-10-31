def faktorial (n) :
    if n == 0 :
        return 1
    else :
        return n*faktorial(n-1)

print('')
print('a. C(5, 3)')
kombinasi = faktorial(5)/(faktorial(5-3)*faktorial(3))
print(kombinasi)

print('')
print('b. P(10, 7)')
permutasi =faktorial(10)/faktorial(10-7)
print(permutasi)