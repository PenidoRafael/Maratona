N = int(input())

fib1 = 2
fib2 = 1
fibn = 1

for i in range(N-2):

    fibn = fib1 + fib2
    fib2 = fib1
    fib1 = fibn

print(fibn)

