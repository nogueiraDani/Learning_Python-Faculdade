#!/usr/bin/python
# -*- coding: utf-8 -*-


from code.EnemyShot import EnemyShot
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


# Define a classe Enemy, que herda da classe Entity.
# Mais um exemplo do padrão de projeto Inheritance.
class Enemy(Entity):
    # Método construtor da classe Enemy. É chamado quando um objeto Enemy é criado.
    def __init__(self, name: str, position: tuple):
        # Chama o construtor da classe pai (Entity) para inicializar os atributos básicos da entidade.
        super().__init__(name, position)
        # Inicializa o atributo shot_delay do inimigo com o valor correspondente do dicionário ENTITY_SHOT_DELAY, baseado no nome do inimigo.
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    # Define o método move para controlar o movimento do inimigo.
    def move(self,):
        # Move o inimigo para a esquerda, subtraindo a sua velocidade da coordenada x do centro do seu retângulo. A velocidade é obtida do dicionário ENTITY_SPEED.
        self.rect.centerx -= ENTITY_SPEED[self.name]

    # Define o método shoot para controlar a ação de atirar do inimigo.
    def shoot(self):
        # Decrementa o valor do shot_delay em 1 a cada vez que este método é chamado.
        self.shot_delay -= 1
        # Verifica se o shot_delay chegou a 0, indicando que é hora de o inimigo atirar novamente.
        if self.shot_delay == 0:
            # Se o shot_delay for 0, ele é resetado para o valor inicial obtido do dicionário ENTITY_SHOT_DELAY.
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            # Cria e retorna um novo objeto da classe EnemyShot.
            return EnemyShot(
                # O nome do tiro é gerado combinando o nome do inimigo com "Shot". A posição do tiro é definida como o centro do retângulo do inimigo.
                name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
