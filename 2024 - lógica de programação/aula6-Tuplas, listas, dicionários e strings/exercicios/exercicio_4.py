#dicionarios

#carinha do dicionario, com {}
game = {'nome': 'Super Mario',
        'desenvolvedora': 'Nintendo',
        'ano': 1990}

#2 formas de criar dicionario vazio
vazio = {}
vazio_novo = dict()

print(game['ano'])

print(game.values())

print(game.keys())

print(game.items())

#itertar com for in pegando a chave e o valor de cada item
for keys, values in game.items():
    print(f'{keys} = {values}')







