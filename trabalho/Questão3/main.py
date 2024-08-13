"""
Solução para a questão 03 do trabalho de lógica de programação e algoritmos
boas práticas baseadas no PEP8

"""


def mostrar_opcoes_modelo():
    """
    função para exibir as opções de camisetas
    """
    print('Entre com o modelo desejado')
    print('MCS - Manga Curta Simples')
    print('MLS - Manga Longa Simples')
    print('MCE - Manga Curta Com Estampa')
    print('MLE - Manga Longa Com Estampa')


def escolha_modelo():
    """
    função que classifica a opção escolhida
    :return: o valor de cada unidade baseada no modelo
    """
    while True:
        mostrar_opcoes_modelo()
        opcao_escolhida = input('>>')
        if (opcao_escolhida == 'MCS' or opcao_escolhida == 'MLS' or
                opcao_escolhida == 'MCE' or opcao_escolhida == 'MLE'):
            if opcao_escolhida == 'MCS':
                return 1.80
            elif opcao_escolhida == 'MLS':
                return 2.10
            elif opcao_escolhida == 'MCE':
                return 2.90
            else:
                return 3.20
        else:
            print('Escolha inválida, entre com o modelo novamente\n\n')


def num_camisetas():
    """
    função para perguntar quantidade de camisetas desejada, valida a
    quantidade e classifica o desconto conforme a quantidade
    :return: quantidade das camisetas já considerando o desconto se houver
    """
    while True:
        try:
            quantidade_de_camisetas = int(input('Entre com o número de '
                                                'camisetas: '))
        except ValueError:
            print(
                "Por favor, entre com o número de camisetas novamente.\n")
            continue
        else:
            if quantidade_de_camisetas > 20000:
                print('Não aceitamos tantas camisetas de uma vez.')
                print(
                    "Por favor, entre com o número de camisetas novamente.\n")
                continue
            else:
                if quantidade_de_camisetas < 20:
                    return quantidade_de_camisetas
                elif 20 <= quantidade_de_camisetas < 200:
                    return quantidade_de_camisetas * 0.95
                elif 200 <= quantidade_de_camisetas < 2000:
                    return quantidade_de_camisetas * 0.97
                elif 2000 <= quantidade_de_camisetas < 20000:
                    return quantidade_de_camisetas * 0.88


def mostrar_opcoes_frete():
    """
    função para exibir as opções de frente
    """
    print('\nEscolha o tipo de frete:')
    print('1 - Frete por transportadora - R$ 100.00')
    print('2 - Frete por Sedex - R$ 200.00')
    print('0 - Retirar pedido na fábrica - R$ 0.00')


def frete():
    """
    função que valida e classifica as opçoes de frente
    :return: o valor adicional da opção de frete desejada
    """
    while True:
        mostrar_opcoes_frete()
        opcao_escolhida = int(input('>>'))
        if 0 <= opcao_escolhida <= 2:
            if opcao_escolhida == 0:
                return 0.00
            elif opcao_escolhida == 1:
                return 100.00
            else:
                return 200.00
        else:
            continue


# programa principal


print('Bem vindos a Fábrica de Camisetas de Daniela Nogueira Rampim\n')

modelo = escolha_modelo()
num = num_camisetas()
frete = frete()

# print com o resultado final do pedido
print(f'Total: R$ {format((modelo * num) + frete, ".2f")} (Modelo: '
      f'{format(modelo, ".2f")} * Quantidade(com desconto): '
      f'{int(num)} + frete: '
      f'{format(frete, ".2f")})')
