H, P, F, D = list(map(int,input().split()))

while True:
    F = (F + D)%16

    if F == H:
        print('S')
        break

    if F == P:
        print('N')
        break

