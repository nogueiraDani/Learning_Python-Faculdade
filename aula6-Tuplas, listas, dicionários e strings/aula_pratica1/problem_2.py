palavras = []


for i in range(3):
    palavra = input('Digite uma palavra: ')
    contador = 0
    vogais = []
    for char in palavra:
        if char.lower() in 'aeiou':
            contador += 1
            vogais.append(char.lower())
    palavras.append({f'{palavra}': [f'{contador}', f'{vogais}']})

print(palavras)


