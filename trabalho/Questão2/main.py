"""
Solução para a questão 02 do trabalho de lógica de programação e algoritmos
boas práticas baseadas no PEP8

"""
# apresentação inicial
boas_vindas = 'Bem vindos a loja de Marmitas da Daniela Nogueira Rampim'
print('-' * 3, boas_vindas, '-' * 4)

# textos do titulo da tabela
titulo_cardapio = 'Cardápio'
titulo_coluna_tamanho = 'Tamanho'
titulo_coluna_bife = 'Bife Acebolado(BA)'
titulo_coluna_frango = 'Filé de ''Frango(FF)'

# definições das decorações do menu
quantidade_decoracao_titulo_cardapio = int(
    (len(boas_vindas) - len(titulo_cardapio)) / 2) + 3

# decoração linha superior e inferior da tabela
decoracao_superior_inferior = ('-' * (len(boas_vindas) + 9))

# decorações laterais
decoracao_lateral_esquerda = ('-' * 6 + '|')
decoracao_lateral_direita = ('|' + '-' * 6)

# decoração da coluna tamanho
centralizacao_coluna_tamanho = (' ' * (int(len(titulo_coluna_tamanho) / 2)))

# tamanhos
nome_tamanho_marmita = 'PMG'

##valores
# bife
valor_bife_p = 16
valor_bife_m = 18
valor_bife_g = 22

# texto do valor do bife formatado
texto_valor_coluna_bife_p = f'R$ {format(valor_bife_p, ".2f")}'
texto_valor_coluna_bife_m = f'R$ {format(valor_bife_m, ".2f")}'
texto_valor_coluna_bife_g = f'R$ {format(valor_bife_g, ".2f")}'

# frango
valor_frango_p = 15
valor_frango_m = 17
valor_frango_g = 21

# texto do valor do frango formatado
texto_valor_coluna_frango_p = f'R$ {format(valor_frango_p, ".2f")}'
texto_valor_coluna_frango_m = f'R$ {format(valor_frango_m, ".2f")}'
texto_valor_coluna_frango_g = f'R$ {format(valor_frango_g, ".2f")}'

##apresentação do cardápio
# titulo
print('-' * quantidade_decoracao_titulo_cardapio,
      titulo_cardapio,
      '-' * (quantidade_decoracao_titulo_cardapio + 1)
      )

# imprimindo decoração superior
print(decoracao_superior_inferior)

# titulo da tabela do cardápio
print(decoracao_lateral_esquerda,
      titulo_coluna_tamanho, '|',
      titulo_coluna_bife, '|',
      titulo_coluna_frango,
      decoracao_lateral_direita
      )
# centralizadores das colunas de preço
centralizacao_coluna_bife = (' ' * (int((len(titulo_coluna_bife) - len(
    texto_valor_coluna_bife_p)) / 2) - 1))

centralizacao_coluna_frango = (' ' * (int((len(titulo_coluna_frango) - len(
    texto_valor_coluna_frango_p)) / 2) - 1))

# corpo da tabela
for i in range(1, 4, 1):

    texto_linha_coluna_tamanho = (f'{centralizacao_coluna_tamanho}'
                                  f'{nome_tamanho_marmita[i - 1]}'
                                  f'{centralizacao_coluna_tamanho}')

    if i == 1:
        texto_linha_coluna_bife = texto_valor_coluna_bife_p
        texto_linha_coluna_frango = texto_valor_coluna_frango_p
    elif i == 2:
        texto_linha_coluna_bife = texto_valor_coluna_bife_m
        texto_linha_coluna_frango = texto_valor_coluna_frango_m
    else:
        texto_linha_coluna_bife = texto_valor_coluna_bife_g
        texto_linha_coluna_frango = texto_valor_coluna_frango_g

    # imprimindo cada linha
    (print(decoracao_lateral_esquerda,
           texto_linha_coluna_tamanho, '|',
           centralizacao_coluna_bife, texto_linha_coluna_bife,
           centralizacao_coluna_bife, '|',
           centralizacao_coluna_frango, texto_linha_coluna_frango,
           centralizacao_coluna_frango,
           decoracao_lateral_direita))

# imprimindo decoração inferior da tabela
print(decoracao_superior_inferior)

# Solicitando sabor ao cliente
resposta_valida = False
tamanho_valido = False
nome_sabor = ''
nome_tamanho = ''
valor_pedido = 0
valor_marmita = ''

while not resposta_valida:

    #Validando sabor
    sabor_escolhido = input('Entre com o sabor desejado (BA/FF): ')
    if sabor_escolhido == 'BA' or sabor_escolhido == 'FF':
        if sabor_escolhido == 'BA':
            nome_sabor = 'Bife Acebolado'
            while not tamanho_valido:
                tamanho_escolhido = input(
                    'Entre com o tamanho desejado (P/M/G): ')
                if tamanho_escolhido == 'P':
                    nome_tamanho = 'P'
                    valor_pedido += valor_bife_p
                    valor_marmita = texto_valor_coluna_bife_p
                    tamanho_valido = True
                elif tamanho_escolhido == 'M':
                    nome_tamanho = 'M'
                    valor_pedido += valor_bife_m
                    valor_marmita = texto_valor_coluna_bife_m
                    tamanho_valido = True
                elif tamanho_escolhido == 'G':
                    nome_tamanho = 'G'
                    valor_pedido += valor_bife_g
                    valor_marmita = texto_valor_coluna_bife_g
                    tamanho_valido = True
                else:
                    print('Tamanho inválido. Tente novamente' + "\n")
                    break
                break

        elif sabor_escolhido == 'FF':
            nome_sabor = 'Filé de Frango'
            while not tamanho_valido:
                tamanho_escolhido = input(
                    'Entre com o tamanho desejado (P/M/G): ')
                if tamanho_escolhido == 'P':
                    nome_tamanho = 'P'
                    valor_pedido += valor_frango_p
                    valor_marmita = texto_valor_coluna_frango_p
                    tamanho_valido = True
                elif tamanho_escolhido == 'M':
                    nome_tamanho = 'M'
                    valor_pedido += valor_frango_m
                    valor_marmita = texto_valor_coluna_frango_m
                    tamanho_valido = True
                elif tamanho_escolhido == 'G':
                    nome_tamanho = 'G'
                    valor_pedido += valor_frango_g
                    valor_marmita = texto_valor_coluna_frango_g
                    tamanho_valido = True
                else:
                    print('Tamanho inválido. Tente novamente' + "\n")
                    break
                break

        #impressão de cada escolha
        if tamanho_valido:
            print(
                f'Você pediu um {nome_sabor} no tamanho {nome_tamanho}: '
                f'{valor_marmita}' + "\n")

            #validando nova escolha
            nova_escolha = input('Deseja mais alguma coisa? (S/N): ')
            if nova_escolha == 'S':
                tamanho_valido = False
            elif nova_escolha == 'N':

                #Impressão do valor total do pedido
                print("\n" + f'O valor total a ser pago: R$ '
                      f'{format(valor_pedido, ".2f")}')
                break
            else:
                continue
    else:
        print('Sabor inválido. Tente novamente' + "\n")

