for i in range (6):
    print(f'de 0 a 5, {i}')

for i in range(1, 7, 2):
    print(f'de 1 a 6, de 2 em 2, {i}')

for i in range(20, 10, -3):
    print(f'de 20 a 10, de 3 em 3, {i}')

#Varredura de string

phrase = input('Digite a frase: ')

for i in range(0, len(phrase), 1):
    print(phrase[i], end="*")

