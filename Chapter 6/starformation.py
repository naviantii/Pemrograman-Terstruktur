def starFormation1 (n):
    for i in range(n):
     for j in range(i+1):
        print('*', end='')
     print()


def starFormation2(n):
    for i in reversed(range(n)):
        for j in range(i+1):
            print('*', end='')
        print()

print('output program starformation jika n = 7 :')
starFormation1(4)
starFormation2(3)