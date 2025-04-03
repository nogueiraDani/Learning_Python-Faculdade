from random import randint

usuario_ganhou = 0
computador_ganhou = 0
jogadas = []

print('JOKENPÔ')
print('1-pedra')
print('2-papel')
print('3-tesoura')
print('0-sair')


def validar_opcao(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (max < x):
        x = int(input(pergunta))
    return x


def jogar(jogador1, jogador2):
    global usuario_ganhou
    global computador_ganhou

    if jogador1 == 1:
        if jogador2 == 3:
            usuario_ganhou += 1
        elif jogador2 == 2:
            computador_ganhou += 1

    if jogador1 == 2:
        if jogador2 == 1:
            usuario_ganhou += 1
        elif jogador2 == 3:
            computador_ganhou += 1

    if jogador1 == 3:
        if jogador2 == 2:
            usuario_ganhou += 1
        elif jogador2 == 1:
            computador_ganhou += 1


while True:
    usuario = validar_opcao('Digite uma opção: ', 0, 3)
    if not usuario:
        break

    computador = randint(1, 3)

    jogar(usuario, computador)


if usuario_ganhou < computador_ganhou:
    print('Você perdeu!')
elif computador_ganhou < usuario_ganhou:
    print('Você ganhou!')
else:
    print('Empate')


