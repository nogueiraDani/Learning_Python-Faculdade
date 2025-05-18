#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Const import COLOR_CYAN, COLOR_GREEN, COLOR_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, SPAW_TIME, TIMEOUT_LEVEL, TIMEOUT_STEP, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


# Define a classe Level, que representa um nível do jogo.
# Esta classe gerencia as entidades do nível, a lógica do jogo e a interação com o jogador.
class Level:
    # Método construtor da classe Level.
    def __init__(
        self, window: Surface, name: str, game_mode: str, player_score: list[int]
    ):
        # Inicializa o tempo limite do nível com o valor da constante TIMEOUT_LEVEL.
        self.timeout = TIMEOUT_LEVEL
        # Armazena a superfície da janela do jogo.
        self.window = window
        # Armazena o nome do nível.
        self.name = name
        # Armazena o modo de jogo (1P, 2P Cooperativo, 2P Competitivo).
        self.game_mode = game_mode
        # Inicializa uma lista vazia para armazenar as entidades do nível.
        self.entity_list: list[Entity] = []
        # Utiliza a EntityFactory (padrão Factory Method) para criar os objetos de fundo do nível e os adiciona à lista de entidades.
        self.entity_list.extend(EntityFactory.get_entity(self.name + "Bg"))
        # Utiliza a EntityFactory para criar o objeto do jogador 1.
        player = EntityFactory.get_entity("Player1")
        # Define a pontuação inicial do jogador 1 com o valor passado para o construtor.
        player.score = player_score[0]
        # Adiciona o jogador 1 à lista de entidades.
        self.entity_list.append(player)
        # Verifica se o modo de jogo é cooperativo ou competitivo (2 jogadores).
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            # Cria o objeto do jogador 2 usando a EntityFactory.
            player = EntityFactory.get_entity("Player2")
            # Define a pontuação inicial do jogador 2.
            player.score = player_score[1]
            # Adiciona o jogador 2 à lista de entidades.
            self.entity_list.append(player)
        # Define um timer para o evento de surgimento de novos inimigos, com um intervalo de tempo definido pela constante SPAW_TIME.
        pygame.time.set_timer(EVENT_ENEMY, SPAW_TIME)
        # Define um timer para o evento de tempo limite do nível, com um intervalo definido por TIMEOUT_STEP.
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100ms

    # Define o método run, que contém o loop principal do nível.
    def run(self, player_score: list[int]):
        # Carrega a música de fundo do nível.
        pygame.mixer_music.load(f"./asset/{self.name}.mp3")
        # Define o volume da música de fundo.
        pygame.mixer_music.set_volume(0.3)
        # Inicia a reprodução da música de fundo em loop (-1 significa loop infinito).
        pygame.mixer_music.play(-1)
        # Cria um objeto Clock para controlar a taxa de quadros do jogo.
        clock = pygame.time.Clock()
        # Loop infinito que mantém o nível em execução até uma condição de saída seja atingida.
        while True:
            # Limita a taxa de quadros do jogo a 60 FPS.
            clock.tick(60)
            # Itera por cada entidade na lista de entidades.
            for ent in self.entity_list:
                # Desenha a superfície da entidade na janela na posição do seu retângulo.
                self.window.blit(source=ent.surf, dest=ent.rect)
                # Chama o método move de cada entidade para atualizar sua posição. (Padrão Template Method herdado de Entity)
                ent.move()
                # Verifica se a entidade é um jogador ou um inimigo (entidades que podem atirar).
                if isinstance(ent, (Player, Enemy)):
                    # Chama o método shoot da entidade para tentar disparar.
                    shoot = ent.shoot()
                    # Se o método shoot retornar um objeto (um tiro foi disparado).
                    if shoot is not None:
                        # Adiciona o tiro à lista de entidades.
                        self.entity_list.append(shoot)
                # Se a entidade for o jogador 1, exibe suas informações (vida e pontuação) na tela.
                if ent.name == "Player1":
                    self.level_text(
                        14,
                        f"Player1 - Health: {ent.health} | Score: {ent.score}",
                        COLOR_GREEN,
                        (10, 25),
                    )
                # Se a entidade for o jogador 2, exibe suas informações.
                if ent.name == "Player2":
                    self.level_text(
                        14,
                        f"Player2 - Health: {ent.health} | Score: {ent.score}",
                        COLOR_CYAN,
                        (10, 45),
                    )
            # Itera por todos os eventos que ocorreram desde a última iteração.
            for event in pygame.event.get():
                # Se o evento for do tipo QUIT (o jogador fechou a janela).
                if event.type == pygame.QUIT:
                    # Desinicializa todos os módulos Pygame.
                    pygame.quit()
                    # Finaliza o script Python.
                    sys.exit()
                # Se o evento for do tipo EVENT_ENEMY (hora de criar um novo inimigo).
                if event.type == EVENT_ENEMY:
                    # Escolhe aleatoriamente o tipo de inimigo a ser criado ("Enemy1" ou "Enemy2").
                    choice = random.choice(("Enemy1", "Enemy2"))
                    # Cria o inimigo usando a EntityFactory e o adiciona à lista de entidades.
                    self.entity_list.append(EntityFactory.get_entity(choice))
                # Se o evento for do tipo EVENT_TIMEOUT (intervalo do timer do nível).
                if event.type == EVENT_TIMEOUT:
                    # Decrementa o tempo restante do nível.
                    self.timeout -= TIMEOUT_STEP
                    # Se o tempo limite chegar a zero.
                    if self.timeout == 0:
                        # Itera pela lista de entidades para encontrar os jogadores e atualizar suas pontuações na lista player_score.
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == "Player1":
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == "Player2":
                                player_score[1] = ent.score
                        # Retorna True, indicando que o nível foi concluído (por tempo limite).
                        return True

            # Verifica se algum jogador ainda está presente na lista de entidades.
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            # Se nenhum jogador for encontrado (todos morreram), retorna False, indicando que o nível não foi concluído com sucesso.
            if not found_player:
                return False

            # Desenha o texto com o nome do nível e o tempo restante na tela.
            self.level_text(
                14,
                f"{self.name} - Timeout: {self.timeout / 1000:.1f}s",
                COLOR_WHITE,
                (10, 5),
            )
            # Desenha o texto com a taxa de quadros atual.
            self.level_text(
                14, f"fps: {clock.get_fps():.0f}", COLOR_WHITE, (10,
                                                                 WIN_HEIGHT - 35)
            )
            # Desenha o texto com o número de entidades ativas no nível.
            self.level_text(
                14,
                f"entidades: {len(self.entity_list)}",
                COLOR_WHITE,
                (10, WIN_HEIGHT - 20),
            )
            # Atualiza toda a tela para mostrar as mudanças.
            pygame.display.flip()
            # Verifica colisões entre as entidades usando o EntityMediator (padrão Mediator).
            EntityMediator.verify_collision(entity_list=self.entity_list)
            # Verifica a vida das entidades e remove aquelas com vida menor ou igual a zero usando o EntityMediator.
            EntityMediator.verify_health(entity_list=self.entity_list)

    # Define um método para exibir texto na tela do nível.
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # Cria uma fonte de texto com o tamanho especificado.
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        # Renderiza o texto na superfície com a cor especificada e ativa a transparência.
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        # Obtém o retângulo da superfície do texto e define sua posição.
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        # Desenha a superfície do texto na janela na posição do seu retângulo.
        self.window.blit(source=text_surf, dest=text_rect)
