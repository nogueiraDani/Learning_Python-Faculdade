#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from abc import ABC, abstractmethod
from code.Const import ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE


# Define a classe Entity como uma Abstract Base Class (ABC).
# O padrão Abstract Base Class define uma interface para outras classes sem implementar os detalhes.
# Classes que herdam de Entity são obrigadas a implementar os métodos abstratos definidos aqui.
class Entity(ABC):
    # Método construtor da classe Entity. É chamado quando um objeto de uma classe que herda de Entity é criado.
    def __init__(self, name: str, position: tuple):
        # Inicializa o atributo name com o nome da entidade fornecido.
        self.name = name
        # Carrega a imagem da entidade do arquivo correspondente e usa convert_alpha() para lidar com a transparência.
        self.surf = pygame.image.load(
            './asset/' + name + '.png').convert_alpha()
        # Obtém o retângulo (bounding box) da superfície da imagem e define sua posição inicial.
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        # Inicializa o atributo speed com 0.
        self.speed = 0
        # Inicializa o atributo health da entidade buscando o valor correspondente no dicionário ENTITY_HEALTH.
        self.health = ENTITY_HEALTH[self.name]
        # Inicializa o atributo damage da entidade buscando o valor correspondente no dicionário ENTITY_DAMAGE.
        self.damage = ENTITY_DAMAGE[self.name]
        # Inicializa o atributo score da entidade buscando o valor correspondente no dicionário ENTITY_SCORE.
        self.score = ENTITY_SCORE[self.name]
        # Inicializa o atributo last_dmg para rastrear a última fonte de dano.
        self.last_dmg = "None"

    # Decorador @abstractmethod indica que este método é um método abstrato.
    # Isso significa que a classe Entity não fornece uma implementação para este método,
    # e qualquer classe que herde de Entity *deve* implementar o seu próprio método move.
    @abstractmethod
    # Define o método abstrato move, que será responsável pela lógica de movimento de cada tipo de entidade.
    # Este é um exemplo do padrão Template Method (em um sentido mais amplo). A classe base (Entity) define a estrutura de um método,
    # mas delega a implementação de algumas etapas para as subclasses (as diferentes entidades).
    def move(self, ):
        # A palavra-chave pass indica que este método não faz nada na classe base.
        pass
