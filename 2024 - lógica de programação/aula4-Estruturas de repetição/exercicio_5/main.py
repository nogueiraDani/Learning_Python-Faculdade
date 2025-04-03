"""
Truthy e Falsey
Falsey == Falso => número 0 (int ou float) e string vazio ('')
Truthy == True => qualquer outro dado

"""

name = '' # => Falsey

while not name: # => not Falsey
    name = input('Digite um nome: ') # => Truthy

value = int(input('Digite um valor: '))
if value:  # => value equivale a != 0
    print('Você digitou um valor diferente de Zero')
else:
    print('Você digitou Zero')