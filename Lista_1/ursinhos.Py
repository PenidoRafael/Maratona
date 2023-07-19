limak, bob = list(map(int,input().split()))

count = 1

while True:
    limak *= 3
    bob *= 2
    if limak > bob:
        print(count)
        break

    count += 1