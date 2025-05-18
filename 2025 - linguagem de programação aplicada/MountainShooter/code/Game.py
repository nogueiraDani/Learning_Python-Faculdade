#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from code.Score import Score
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


# Define a classe Game, que provavelmente controla o fluxo principal do jogo.
class Game:
    # Método construtor da classe Game. É chamado quando um objeto Game é criado.
    def __init__(self):
        # Inicializa todos os módulos importados do Pygame.
        pygame.init()

        # Define o tamanho da janela do jogo, usando as constantes de largura e altura definidas anteriormente.
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    # Define o método run, que contém o loop principal do jogo.
    def run(self, ):
        # Loop infinito que mantém o jogo em execução até que o jogador decida sair.
        while True:
            # Cria uma instância da classe Score, passando a janela do jogo como argumento.
            score = Score(self.window)
            # Cria uma instância da classe Menu, também passando a janela.
            menu = Menu(self.window)
            # Executa o menu e armazena o valor retornado (a opção escolhida pelo jogador).
            menu_return = menu.run()

            # Verifica se a opção de menu retornada corresponde a uma das opções de "novo jogo" (1 Jogador, 2 Jogadores Cooperativo, 2 Jogadores Competitivo).
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Inicializa a pontuação dos jogadores para [0, 0].
                player_score = [0, 0]  # [Player1, Player2]
                # Cria uma instância da classe Level para o primeiro nível ("Level1"), passando a janela, o nome do nível, a opção de menu escolhida e a lista de pontuação dos jogadores.
                level = Level(self.window, "Level1", menu_return, player_score)
                # Executa o primeiro nível e armazena o valor retornado (que pode indicar se o nível foi concluído com sucesso).
                level_return = level.run(player_score)
                # Se o primeiro nível foi concluído com sucesso (level_return é True):
                if level_return:
                    # Cria uma instância da classe Level para o segundo nível ("Level2"), reutilizando a mesma pontuação dos jogadores.
                    level = Level(self.window, "Level2",
                                  menu_return, player_score)
                    # Executa o segundo nível e armazena o resultado.
                    level_return = level.run(player_score)
                    # Se o segundo nível também foi concluído com sucesso:
                    if level_return:
                        # Salva a pontuação dos jogadores, juntamente com a opção de menu escolhida (para identificar o tipo de jogo), usando o objeto Score.
                        score.save(menu_return, player_score)

            # Verifica se a opção de menu retornada é a de exibir a pontuação.
            elif menu_return == MENU_OPTION[3]:
                # Chama o método show do objeto Score para exibir a tela de pontuação.
                score.show()
            # Verifica se a opção de menu retornada é a de sair.
            elif menu_return == MENU_OPTION[4]:
                # Desinicializa todos os módulos Pygame.
                pygame.quit()  # Fecha a janela
                # Finaliza o programa Pygame.
                quit()  # Encerra o Pygame
            # Caso a opção de menu não corresponda a nenhuma das anteriores (tratamento de erro ou saída inesperada).
            else:
                # Desinicializa os módulos Pygame.
                pygame.quit()
                # Finaliza o script Python.
                sys.exit()
