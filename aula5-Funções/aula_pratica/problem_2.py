"""
Suponha que você é um colecionar de jogos de videogame. Escreva um algoritmo
que permita cadastrar esses jogos informando o nome e a qual videogame ele
pertence
Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo
que foi cadastrado e sair
Para resolver esse exercício, crie pelo menos uma função para cada item do
menu
Além disso, armazene todos os dados em um arquivo de texto que deve ser
salvo em disco e manter os dados cadastrados

"""
import os


def exibir_menu():
    print('-' * 40)
    print('-' * 15 + '|', ' MENU ', '|' + '-' * 15)
    print('-' * 3 + '|', '1 - CADASTRAR NOVO JOGO' + ' ' * 7, '|' + '-' * 3)
    print('-' * 3 + '|', '2 - LISTAR JOGOS CADASTRADOS' + ' ' * 2, '|' + '-'
          * 3)
    print('-' * 3 + '|', '3 - EXCLUIR LISTA' + ' ' * 14, '|' + '-'
          * 3)
    print('-' * 3 + '|', '4 - SAIR' + ' ' * 22, '|' + '-' * 3)
    print('-' * 40)


def option_is_valid(option_selected):
    if 1 <= option_selected <= 4:
        return True
    else:
        print('Valor incorreto, digite entre as opções 1, 2 ou 3')
        return False


def create_file(name_file):
    try:
        a = open(name_file, 'wt+')
        a.write('Lista de jogos cadastrados\n')
        a.close()
    except:
        print(f'Erro ao criar {name_file}.')
    else:
        print(f'\nArquivo {name_file} criado com sucesso!\n')


def registrer_game(name_file, name_game, name_videogame):
    try:
        a = open(name_file, 'at')
    except:
        print('Erro ao abrir arquivo.')
    else:
        a.write(f'*{name_game} : {name_videogame}\n')


def list_games(name_file):
    try:
        a = open(name_file, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        print(a.read())


def delete_file(name_file):
    try:
        a = open(name_file, 'rt')
        a.close()
    except FileNotFoundError:
        print('Arquivo não encontrado')
    else:
        os.remove(name_file)
        print(f'\nArquivo {name_file} excluido com sucesso.\n')


def there_is_file_created(name_file):
    try:
        a = open(name_file, 'rt')
        a.close()
    except FileNotFoundError:
        create_file(name_file)
    else:
        print(f'\nArquivo: *{name_file}* localizado no computador\n')
        return True


while True:
    name_file = 'list of games.txt'
    exibir_menu()

    option_selected = int(input("---| Digite a opção desejada: "))

    if option_is_valid(option_selected):
        if option_selected == 1:
            there_is_file_created(name_file)
            name_game = input("---| Digite o nome do jogo: ")
            name_videogame = input("---| Digite o nome do videogame: ")
            registrer_game(name_file, name_game, name_videogame)
        elif option_selected == 2:
            print('\n')
            list_games(name_file)
        elif option_selected == 3:
            delete_file(name_file)
        else:
            break
