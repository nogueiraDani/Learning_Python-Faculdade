#tuplas

#carinha da tupla, com ()
mochila = ('Machado', 'Camiseta', 'Bacon', 'Acabate', 'Lanterna')

print(mochila)
print(mochila[0])
print(mochila[0:2])
print(mochila[-1])

#nao conseguimos alterar itens de tupla
#mochila[2] = 'Ovos'

for item in mochila:  #outra forma de fazer um for
    print(f'Na mochila tem: {item}')

upgrade = ('Queijo', 'Canivete')

mochila_grande = mochila + upgrade

print(mochila_grande)


#tuplas como paramentros de função | desempacotamento de parametros
def soma(*num):
    acumulado = 0
    print(f'Tupla: {num}')

    for i in num:
        acumulado += i

    return acumulado


print(f'Resultado: {soma(1, 2)}\n')
print(f'Resultado: {soma(1, 2, 3, 4, 5, 6, 7, 8, 9)}\n')


