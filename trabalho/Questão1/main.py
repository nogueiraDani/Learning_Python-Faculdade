"""
Solução para a questão 01 do trabalho de lógica de programação e algoritmos
boas práticas baseadas no PEP8
"""

print('Bem-vindos a loja da Daniela Nogueira Rampim')


#solicitando informações do usuário
valor_do_pedido = float(input('Entre com o valor do pedido: '))
quatidade_de_parcelas = int(input('Entre com a quantidade de parcelas: '))

#classificando juros conforme quantidade de parcelas
juros = 0

if quatidade_de_parcelas < 4:
    juros = 0
elif 4 <= quatidade_de_parcelas < 6:
    juros = 4/100
elif 6 <= quatidade_de_parcelas < 9:
    juros = 8/100
elif 9 <= quatidade_de_parcelas < 13:
    juros = 16/100
else:
    juros = 32/100

#calculando parcelas e valor total parcelado
valor_da_parcela = (valor_do_pedido * (1 + juros)) / quatidade_de_parcelas
valor_total_parcelado = valor_da_parcela * quatidade_de_parcelas

#exibindo resultado
print(f'O valor das parcelas é de:R$ {round(valor_da_parcela, 2)}')
print(f'O valor Total Parcelado é de:R$ '
      f'{format(valor_total_parcelado, ".2f")}')

