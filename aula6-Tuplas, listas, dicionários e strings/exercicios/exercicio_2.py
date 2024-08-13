#Listas

#carinha da lista, com []
mochila = ['Machado', 'Camiseta', 'Bacon', 'Abacate']
print(mochila)

#duas formas de criar lista vazia
lista = []
lista_vazia = list()

#pode alterar itens
mochila[2] = 'Laranja'

# pode add itens, no final como abaixo
mochila.append('Lanterna')

#pode inserir itens definindo o local
mochila.insert(3, 'Sapato')

#pode deletar itens definindo indice
del mochila[1]

#pode remover baseado no conteudo
mochila.remove('Machado')

#mesma referência
lista_original = [1, 2, 3]
lista_referenciada = lista_original

print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 3

print(lista_original)
print(lista_referenciada)


#para fazer cópia
lista_nova = [1, 2, 3, 4, 5]
lista_nova_copia = lista_nova[:]

print(lista_nova)
print(lista_nova_copia)

lista_nova_copia[0] = 2
print(lista_nova)
print(lista_nova_copia)
