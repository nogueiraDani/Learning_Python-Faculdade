cadastro = {'nome': [],
            'sexo': [],
            'ano': []}

while True:
    opcao = input('Deseja cadastrar uma pessoa: [S|N] ')
    if opcao.upper() in 'N':
        break

    if opcao.upper() not in 'S':
        print('Digite S para SIM e N para NÃO.')
        continue

    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo: ')
    ano = int(input('Digite o ano de nascimento: '))

    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)


