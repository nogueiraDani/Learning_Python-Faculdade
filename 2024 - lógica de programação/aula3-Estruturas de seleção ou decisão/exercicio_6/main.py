name = 'Daniela'

new_name = input('Digite um nome: ')
age = 0

if new_name == name:
    print(f'Olá, {new_name}')
else:
    age = int(input('Digite a idade: '))
    if age < 18:
        print(f'{new_name} é menor de idade')
    elif age > 100:
        print(f'{new_name} provavelmente nao está vivo')

