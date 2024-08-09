value = int(input('Digite o valor em R$ a calcular: '))

banknotes_1 = 0
banknotes_5 = 0
banknotes_10 = 0
banknotes_20 = 0
banknotes_50 = 0
banknotes_100 = 0
banknotes_200 = 0

while True:
    if value >= 200:
        banknotes_200 +=1
        value -= 200
    elif value >= 100:
        banknotes_100 += 1
        value -= 100
    elif value >= 50:
        banknotes_50 += 1
        value -= 50
    elif value >= 20:
        banknotes_20 += 1
        value -= 20
    elif value >= 10:
        banknotes_10 += 1
        value -= 10
    elif value >= 5:
        banknotes_5 += 1
    else:
        banknotes_1 += 1
        value -= 1

    if not value:
        break


print('Você vai precisar de:')
if banknotes_1:
    print(f'{banknotes_1} notas de R$ 1,00')

if banknotes_5:
    print(f'{banknotes_5} notas de R$ 5,00')

if banknotes_10:
    print(f'{banknotes_10} notas de R$ 10,00')

if banknotes_20:
    print(f'{banknotes_20} notas de R$ 20,00')

if banknotes_50:
    print(f'{banknotes_50} notas de R$ 50,00')

if banknotes_100:
    print(f'{banknotes_100} notas de R$ 100,00')

if banknotes_200:
    print(f'{banknotes_200} notas de R$ 200,00')
