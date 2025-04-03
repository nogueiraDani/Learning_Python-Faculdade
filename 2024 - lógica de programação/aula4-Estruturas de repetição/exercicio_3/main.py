amount = 0
x = 1

while x <= 5:
    test_grade = float(input(f'Digite a nota da {x}ª prova: '))
    amount += test_grade
    x += 1

print(f'A média final é: {amount / 5}')
