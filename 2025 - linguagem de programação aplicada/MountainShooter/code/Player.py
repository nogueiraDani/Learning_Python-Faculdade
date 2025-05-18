#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.PlayerShot import PlayerShot
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


# Define a classe Player, que herda da classe Entity.
# Este é um exemplo do padrão de projeto Inheritance.
class Player(Entity):
    # Método construtor da classe Player.
    def __init__(self, name: str, position: tuple):
        # Chama o construtor da classe pai (Entity).
        super().__init__(name, position)
        # Inicializa o atraso entre os tiros do jogador, obtendo o valor do dicionário ENTITY_SHOT_DELAY.
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    # Define o método move para controlar o movimento do jogador com base nas teclas pressionadas.
    def move(self, ):
        # Obtém um dicionário booleano de todas as teclas pressionadas no momento.
        pressed_key = pygame.key.get_pressed()
        # Verifica se a tecla de "para cima" do jogador (definida em PLAYER_KEY_UP) está pressionada e se o jogador não está no topo da tela.
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            # Move o jogador para cima, subtraindo a velocidade da coordenada y do centro do seu retângulo.
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Verifica se a tecla de "para baixo" do jogador está pressionada e se o jogador não está na parte inferior da tela.
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            # Move o jogador para baixo, adicionando a velocidade à coordenada y do centro do seu retângulo.
            self.rect.centery += ENTITY_SPEED[self.name]

        # Verifica se a tecla de "para a esquerda" do jogador está pressionada e se o jogador não está na borda esquerda da tela.
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            # Move o jogador para a esquerda, subtraindo a velocidade da coordenada x do centro do seu retângulo.
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # Verifica se a tecla de "para a direita" do jogador está pressionada e se o jogador não está na borda direita da tela.
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            # Move o jogador para a direita, adicionando a velocidade à coordenada x do centro do seu retângulo.
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass

    # Define o método shoot para controlar a ação de atirar do jogador.
    def shoot(self):
        # Decrementa o contador de atraso entre os tiros.
        self.shot_delay -= 1
        # Verifica se o atraso entre os tiros chegou a zero (ou seja, é hora de atirar).
        if self.shot_delay == 0:
            # Reseta o contador de atraso para o valor inicial definido em ENTITY_SHOT_DELAY.
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            # Obtém o estado das teclas pressionadas novamente para verificar se a tecla de tiro está pressionada.
            pressed_key = pygame.key.get_pressed()
            # Verifica se a tecla de "atirar" do jogador (definida em PLAYER_KEY_SHOOT) está pressionada.
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                # Se a tecla de tiro estiver pressionada, cria e retorna um novo objeto da classe PlayerShot.
                return PlayerShot(
                    name=f"{self.name}Shot",
                    position=(self.rect.centerx, self.rect.centery),
                )
            # Se a tecla de tiro não estiver pressionada, retorna None (o jogador não atirou).
            else:
                return None
        # Se o atraso entre os tiros ainda não chegou a zero, retorna None (o jogador não pode atirar ainda).
        else:
            return None
