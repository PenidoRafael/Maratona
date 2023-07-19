valor = float(input()) + 0.001

notas = {
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        }

moedas = {
        1.00: 0,
        0.5: 0,
        0.25: 0,
        0.10: 0,
        0.05: 0,
        0.01: 0,
        }


while valor >= 2.0:

    for i in notas:
        if valor >= i:
            notas[i] += 1
            valor -= i
            break

while valor >= 0.01 and valor < 2.0:

    for i in moedas:
        if valor >= i:
            moedas[i] += 1
            valor -= i
            break

print('NOTAS:')
for i in notas:
    print(f'{notas[i]} nota(s) de R$ {i:.2f}')

print('MOEDAS:')
for i in moedas:
    print(f'{moedas[i]} moeda(s) de R$ {i:.2f}')
