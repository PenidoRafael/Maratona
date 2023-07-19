num, iter = list(map(int,input().split()))

for i in range(iter):
    
    if num % 10 != 0:
        num -=  1
    else:
        num = num /10

print(int(num))