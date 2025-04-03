#importando bibliotecas

##importando a biblioteca toda
#import math

#print(math.sqrt(9))

##importando somente a função da biblioteca -> desejavel
#from math import sqrt

#print(sqrt(9))

##apelidando uma biblioteca
#import math as matematica

#print(matematica.sqrt(9))

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(notas.count(7))
notas[-1] = 4
print(notas)

print(max(notas))

notas.sort()
print(notas)

print(sum(notas) / len(notas))







