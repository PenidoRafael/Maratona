N = int(input())

M = N // 60
N -= M * 60

H = M // 60
M -= H * 60

print(f'{H}:{M}:{N}')