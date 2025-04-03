#Strings e listas dentro de listas

mochila = ['Machado', 'Camisa', 'Tênis']

#perdorrer cada caracter de cada item da lista com for in
for item in mochila:
    print(item)
    for i in item:
        print(i)

print('-' * 10)

#percorred cada caracter de cada item da lista iterando
for i in range(0, len(mochila), 1):
    print(mochila[i])
    for j in range(0, len(mochila[i]), 1):
        print(mochila[i][j])

#lista de listas
mochila_nova = [['Cebola', 0.39],
                ['Tomate', 0.49],
                ['Maçã', 0.89]]


