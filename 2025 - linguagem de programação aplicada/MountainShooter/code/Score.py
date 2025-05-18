import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import COLOR_WHITE, COLOR_YELLOW, SCORE_POS, MENU_OPTION
from code.DBProxy import DBProxy


# Define a classe Score, responsável por gerenciar e exibir a pontuação do jogo.
class Score:
    # Método construtor da classe Score. Recebe a janela do jogo como dependência (Dependency Injection).
    def __init__(self, window: Surface):
        # Armazena a superfície da janela do jogo.
        self.window = window
        # Carrega a imagem de fundo da tela de pontuação.
        self.surf = pygame.image.load("./asset/ScoreBg.png").convert_alpha()
        # Obtém o retângulo da superfície da imagem de fundo.
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    # Define o método save, responsável por exibir a tela de vitória, solicitar o nome do jogador e salvar a pontuação.
    def save(self, game_mode: str, player_score: list[int]):
        # Carrega a música da tela de pontuação.
        pygame.mixer_music.load("./asset/Score.mp3")
        # Toca a música da tela de pontuação em loop.
        pygame.mixer_music.play(-1)
        # Cria uma instância da classe DBProxy (Data Access Object) para interagir com o banco de dados de pontuações.
        db_proxy = DBProxy("DBScore")
        # Inicializa uma string vazia para armazenar o nome do jogador.
        name = ""
        # Loop principal para a tela de salvar pontuação.
        while True:
            # Desenha a imagem de fundo na janela.
            self.window.blit(source=self.surf, dest=self.rect)
            # Exibe o texto "YOU WIN!!" no topo da tela.
            self.score_text(48, "YOU WIN!!", COLOR_YELLOW, SCORE_POS["Title"])
            # Define o texto padrão para solicitar o nome do jogador 1.
            text = "Enter Player 1 name (4 characters):"
            # Obtém a pontuação do jogador 1.
            score = player_score[0]
            # Se o modo de jogo for para um jogador.
            if game_mode == MENU_OPTION[0]:
                # A pontuação é a do jogador 1 (já definida).
                score = player_score[0]
            # Se o modo de jogo for cooperativo.
            if game_mode == MENU_OPTION[1]:
                # A pontuação é a média das pontuações dos dois jogadores.
                score = (player_score[0] + player_score[1]) / 2
                # Altera o texto para solicitar o nome da equipe.
                text = "Enter Team name (4 characters):"
            # Se o modo de jogo for competitivo.
            if game_mode == MENU_OPTION[2]:
                # Se a pontuação do jogador 1 for maior ou igual à do jogador 2.
                if player_score[0] >= player_score[1]:
                    # A pontuação a ser salva é a do jogador 1.
                    score = player_score[0]
                # Caso contrário, a pontuação a ser salva é a do jogador 2.
                else:
                    score = player_score[1]
                    # Altera o texto para solicitar o nome do jogador 2.
                    text = "Enter Player 2 name (4 characters):"
            # Exibe a instrução para inserir o nome.
            self.score_text(20, text, COLOR_WHITE, SCORE_POS["EnterName"])

            # Itera por todos os eventos que ocorreram.
            for event in pygame.event.get():
                # Se o jogador clicar para fechar a janela.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Se um botão do teclado for pressionado.
                elif event.type == KEYDOWN:
                    # Se a tecla pressionada for ENTER e o nome tiver exatamente 4 caracteres.
                    if event.key == K_RETURN and len(name) == 4:
                        # Salva a pontuação no banco de dados usando o DBProxy.
                        db_proxy.save(
                            {"name": name, "score": score,
                                "date": get_formatted_date()}
                        )
                        # Exibe a tela com os melhores scores.
                        self.show()
                        # Retorna da função save para sair do loop.
                        return
                    # Se a tecla pressionada for BACKSPACE, remove o último caractere do nome.
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    # Para outras teclas pressionadas.
                    else:
                        # Se o comprimento do nome for menor que 4, adiciona o caractere digitado ao nome.
                        if len(name) < 4:
                            name += event.unicode
            # Exibe o nome que o jogador está digitando.
            self.score_text(20, name, COLOR_WHITE, SCORE_POS["Name"])
            # Atualiza a tela.
            pygame.display.flip()
            pass

    # Define o método show para exibir os 10 melhores scores.
    def show(self):
        # Carrega a música da tela de pontuação.
        pygame.mixer_music.load("./asset/Score.mp3")
        # Toca a música da tela de pontuação em loop.
        pygame.mixer_music.play(-1)
        # Desenha a imagem de fundo.
        self.window.blit(source=self.surf, dest=self.rect)
        # Exibe o título "TOP 10 SCORE".
        self.score_text(48, "TOP 10 SCORE", COLOR_YELLOW, SCORE_POS["Title"])
        # Exibe os rótulos das colunas da tabela de pontuação.
        self.score_text(
            20, "NAME     SCORE        DATE     ", COLOR_YELLOW, SCORE_POS["Label"]
        )
        # Cria uma instância do DBProxy para acessar o banco de dados.
        db_proxy = DBProxy("DBScore")
        # Recupera os 10 melhores scores do banco de dados.
        list_score = db_proxy.retrieve_top10()
        # Fecha a conexão com o banco de dados.
        db_proxy.close()

        # Itera pela lista de scores para exibir cada um na tela.
        for player_score in list_score:
            # Desempacota os dados de cada score (id, nome, pontuação, data).
            id_, name, score, date = player_score
            # Exibe os dados do jogador na tela, formatando a pontuação para ter sempre 5 dígitos.
            self.score_text(
                20,
                f"{name}     {score:05d}        {date}",
                COLOR_YELLOW,
                SCORE_POS[list_score.index(player_score)],
            )
        # Loop principal para a tela de exibição de scores.
        while True:
            # Itera por todos os eventos.
            for event in pygame.event.get():
                # Se o jogador clicar para fechar a janela.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Se a tecla ESC for pressionada, retorna para a tela anterior (menu).
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            # Atualiza a tela.
            pygame.display.flip()

    # Define um método para exibir texto na tela de pontuação.
    def score_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ):
        # Cria uma fonte de texto com o tamanho especificado e a fonte "Lucida Sans Typewriter".
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        # Renderiza o texto com a cor especificada e ativa a transparência.
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        # Obtém o retângulo da superfície do texto, centralizando-o na posição especificada.
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        # Desenha a superfície do texto na janela na posição do seu retângulo.
        self.window.blit(source=text_surf, dest=text_rect)


# Define uma função para obter a data e hora formatadas para salvar a pontuação.
def get_formatted_date():
    # Obtém a data e hora atuais.
    current_datetime = datetime.now()
    # Formata a hora no formato HH:MM.
    current_time = current_datetime.strftime("%H:%M")
    # Formata a data no formato DD/MM/YY.
    current_date = current_datetime.strftime("%d/%m/%y")
    # Retorna uma string combinando a hora e a data formatadas.
    return f"{current_time} - {current_date}"
