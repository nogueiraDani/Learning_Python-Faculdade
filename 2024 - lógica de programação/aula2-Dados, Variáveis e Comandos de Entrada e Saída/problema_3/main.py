"""
Crie uma váriavel de string que receba uma frase qualquer. Cire uma segunda
variável, agora contendo a primeira metade da string digitada. Imprima na tela
somente os dois últimos caracteres da segunda variável do tipo string

"""

phrase = input('Informe aqui sua frase: ')

size_phrase = len(phrase)
new_phrase = phrase[:int(size_phrase/2)]

print(new_phrase[-2:]) # colocando o numero negativo, conseguimos pegar a
# frase ao contrario.
