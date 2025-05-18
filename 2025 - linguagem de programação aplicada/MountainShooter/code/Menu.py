#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


# Define a classe Menu, que representa o menu principal do jogo.
class Menu:
    # Método construtor da classe Menu.
    def __init__(self, window):
        # Armazena a superfície da janela do jogo.
        self.window = window
        # imagens
        # Importa a imagem de fundo do menu.
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()

        # Desenha o retângulo para posicionar a imagem de fundo.
        self.rect = self.surf.get_rect(left=0, top=0)

    # Define o método run, que controla a lógica do menu.
    def run(self):
        # Inicializa a variável para controlar a opção do menu selecionada (começando pela primeira opção).
        menu_option = 0

        # Importa a música de fundo do menu.
        pygame.mixer_music.load('./asset/Menu.mp3')

        # Toca a música de fundo em loop infinito (-1).
        pygame.mixer_music.play(-1)

        # Loop infinito que mantém o menu em execução até que uma opção seja selecionada.
        while True:
            # Desenha a imagem de fundo do menu na janela.
            self.window.blit(source=self.surf, dest=self.rect)

            # Escreve o título do jogo.
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            # Itera pelas opções do menu para desenhá-las na tela.
            for i in range(len(MENU_OPTION)):
                # Se o índice atual for igual à opção do menu selecionada, a opção é desenhada com a cor amarela (indicando seleção).
                if i == menu_option:
                    self.menu_text(
                        25, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 180 + 30 * i))
                # Caso contrário, a opção é desenhada com a cor branca.
                else:
                    self.menu_text(
                        25, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))

            # Atualiza a tela para mostrar as alterações (fundo e texto do menu).
            pygame.display.flip()

            # Verifica todos os eventos que ocorreram desde a última iteração.
            for event in pygame.event.get():
                # Se o evento for do tipo QUIT (fechar a janela).
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o Pygame
                # Se o evento for do tipo KEYDOWN (tecla pressionada).
                if event.type == pygame.KEYDOWN:
                    # Se a tecla pressionada for a seta para baixo.
                    if event.key == pygame.K_DOWN:
                        # Se a opção do menu atual não for a última, incrementa a opção selecionada.
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        # Caso contrário, volta para a primeira opção do menu.
                        else:
                            menu_option = 0
                    # Se a tecla pressionada for a seta para cima.
                    if event.key == pygame.K_UP:
                        # Se a opção do menu atual não for a primeira, decrementa a opção selecionada.
                        if menu_option > 0:
                            menu_option -= 1
                        # Caso contrário, vai para a última opção do menu.
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    # Se a tecla pressionada for a tecla ENTER (RETURN).
                    if event.key == pygame.K_RETURN:
                        # Retorna a opção de menu selecionada (string). Isso fará com que o loop do menu termine e o jogo avance para a opção escolhida.
                        return MENU_OPTION[menu_option]

    # Define um método para desenhar texto na tela do menu.
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Método para desenhar o texto usando Pygame.

        # Cria uma fonte de texto com o tamanho especificado e a fonte "Lucida Sans".
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans", size=text_size)
        # Renderiza o texto com a cor especificada e ativa a transparência.
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        # Obtém o retângulo da superfície do texto, centralizando-o na posição especificada.
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        # Desenha a superfície do texto na janela na posição do seu retângulo.
        self.window.blit(source=text_surf, dest=text_rect)
