"""
Solução para a questão 04 do trabalho de lógica de programação e algoritmos
boas práticas baseadas no PEP8

"""
import copy

#apresentação do programa
print('Bem vindos a empresa da Daniela Nogueira Rampim')

#lista dos funcionarios
lista_funcionarios = []

#variavel com o id inicial
id_global = 4922098


def cadastrar_funcionario(id_num):
    """
    função que cadastra um funcionario novo como um dicionario dentro de uma
    lista
    :param id_num: id_global que é incrementado externamente
    """
    print('-' * 66)
    print('-' * 20 + 'MENU CADASTRAR FUNCIONÁRIO' + '-' * 20)
    print(f'Id do Funcionário: {id_num}')
    nome = input('Por favor entre com o nome do Funcionário: ')
    setor = input('Por favor entre com o setor do Funcionário: ')
    salario = float(input('Por favor entre com o salário do Funcionário: '))

    print()
    funcionario = {'id': id_num,
                   'nome': nome,
                   'setor': setor,
                   'salario': salario}

    global lista_funcionarios
    lista_funcionarios.append(copy.copy(funcionario))


def mostrar_menu_consultar_funcionario():
    """
    função faz o print do menu consultar funcionario
    """
    print('-' * 66)
    print('-' * 20 + 'MENU CONSULTAR FUNCIONÁRIO' + '-' * 20)
    print('Escolha a opção desejada:')
    print('1 - Consultar Todos os Funcionários')
    print('2 - Consultar Funcionário por id')
    print('3 - Consultar Funcionário(s) por setor')
    print('4 - Retormar')


def mostrar_todos_funcionarios():
    """
    função busca dentro da lista dos funcionarios cada funcionario com suas
    informações e faz o print na tela
    """
    print('-' * 30)
    for i in lista_funcionarios:
        for keys, value in i.items():
            print(f'{keys}: {value}')
        print()


def mostrar_funcionario_id():
    """
    função pergunta por qual id do funcionario quer mostrar, percorre a lista
    dos
    funcionarios e copia o funcioario para outro dicionario e percorre esse
    novo dicionario e imprime as informações dele.
    """
    id_encontrado = {}
    id_pesquisado = int(input('Digite o id do funcionário: '))
    for i in lista_funcionarios:
        for keys, values in i.items():
            if keys == 'id':
                if values == id_pesquisado:
                    id_encontrado = i
                    break

    print('-' * 30)
    for keys, values in id_encontrado.items():
        print(f'{keys}: {values}')
    print()
    print('-' * 30)


def mostrar_funcionarios_setor():
    """
    função pergunta por qual setor do funcionario quer mostrar, percorre a
    lista dos
    funcionarios e copia o funcioario para uma lista e
    percorre essa lista e imprime as informações de cada funcionario
    """
    funcionarios_do_setor = []
    setor_pesquisado = input('Digite o setor do funcionário: ')
    for i in lista_funcionarios:
        for keys, values in i.items():
            if keys == 'setor':
                if values == setor_pesquisado:
                    funcionarios_do_setor.append((copy.copy(i)))
                    break

    print('-' * 30)
    for i in funcionarios_do_setor:
        for keys, values in i.items():
            print(f'{keys}: {values}')
        print()
    print('-' * 30)


def validar_resposta():
    """
    função mostra '>>' para recerber uma opçao e valida se esta dentro das
    opções de 1 a 4
    """
    opcao_num = int(input('>>'))
    if not 1 <= opcao_num <= 4:
        print('Opção inválida')
    else:
        return opcao_num


def consultar_funcionarios():
    """
    função para chamar a função mostrar menu consultar funcionario, valida a
    resposta e
    mostra as opções conforme a opção digitada e validada
    """
    while True:
        try:
            mostrar_menu_consultar_funcionario()
            opcao_digitada = validar_resposta()
        except:
            print('Opção inválida')
            continue
        else:
            match opcao_digitada:
                case 1:
                    mostrar_todos_funcionarios()
                case 2:
                    mostrar_funcionario_id()
                case 3:
                    mostrar_funcionarios_setor()
                case 4:
                    break
                case _:
                    continue


def validar_id(param):
    """
    função para validar o id passado se está dentro da lista de funcionarios
    :param param: id digitado pelo usuario
    :return: retorno o parametro se estaiver dentro da lista de funcionarios e
    retorna 0 se nao estiver
    """
    invalido = 0
    for i in lista_funcionarios:
        for keys, values in i.items():
            if keys in 'id':
                if values == param:
                    return param
                else:
                    invalido += 1
                    continue
    if invalido == len(lista_funcionarios):
        return 0


def remover_funcionario():
    """
    função pergunta o id do funcionario a remover e valida chamando a função
    validar_id. com o id validado percorre a lista de funcionario e exclui o
    funcionario correspondente
    """
    while True:
        print('-' * 66)
        print('-' * 21 + 'MENU REMOVER FUNCIONÁRIO' + '-' * 21)
        id_selecionado = validar_id(int(input('Digite o id do funcionário a '
                                              'ser removido: '
                                              '')))
        if id_selecionado > 0:
            for i in lista_funcionarios:
                for keys, values in i.items():
                    if keys in 'id':
                        if values == id_selecionado:
                            lista_funcionarios.remove(i)
                            print('Funcionário removido com sucesso!')
                            break
        else:
            print('Opção inválida.')
            continue
        break

#programa principal
while True:
    print('-' * 66)
    print('-' * 26 + 'MENU PRINCIPAL' + '-' * 26)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Funcionários')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remover Funcionário')
    print('4 - Sair')
    opcao = validar_resposta()

    match opcao:
        case 1:
            id_global += 1
            cadastrar_funcionario(id_global)
        case 2:
            consultar_funcionarios()
        case 3:
            remover_funcionario()
        case 4:
            break
