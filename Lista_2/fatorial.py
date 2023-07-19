num = int(input())

fat = 1
for i in range(num):
    fat = fat * num
    num -= 1
    
print(fat)