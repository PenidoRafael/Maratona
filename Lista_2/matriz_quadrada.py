while True:
    matriz = int(input())
    if matriz == 0:
        break

    n = matriz
    mat = [[0] * n for _ in range(n)]

    ordem = len(str((2 ** (n-1)) ** 2))

    for x in range(n):
        for y in range(n):
            mat[y][x] = (2 ** x) * (2 ** y)

    for l in mat:
        for c in l:
            print('{:{}d} '.format(c, ordem), end = '')
        print('')

    print()