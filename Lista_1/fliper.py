P, R = map(int, input().split())

saida = 'C'

if P == 1:
	if R == 1:
		saida = 'A'
	else:
		saida = 'B'

print(saida)