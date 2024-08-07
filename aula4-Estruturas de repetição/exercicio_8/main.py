#tabuada
x = 1

while x <= 10:
    print(f'Tabuada do {x}')
    for i in range(1, 11):
        print(f'{x}X{i} = {x*i}')
        i += 1
    print('-' * 10)
    x += 1

