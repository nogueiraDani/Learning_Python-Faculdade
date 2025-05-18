#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importa constantes de 'code.Const'.
from code.Const import WIN_WIDTH, ENTITY_SPEED

# Importa a classe 'Entity'.
from code.Entity import Entity


# Define a classe Background, que herda da classe Entity.
# Este é um exemplo do padrão de projeto Inheritance (Herança), onde Background adquire atributos e métodos de Entity.
class Background(Entity):
    # Inicializa o 'Background'.
    def __init__(self, name: str, position: tuple):
        # Chama inicialização da classe pai.
        super().__init__(name, position)

    # Define o movimento do background.
    def move(self):
        # Move o background para a esquerda, com velocidade específica.
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # Se saiu da tela pela esquerda...
        if self.rect.right <= 0:
            # ...reposiciona à direita para efeito de loop.
            self.rect.left = WIN_WIDTH
