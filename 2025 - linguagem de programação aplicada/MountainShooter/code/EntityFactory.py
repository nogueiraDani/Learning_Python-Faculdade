#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from typing import Any

from code.Enemy import Enemy
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


# Define a classe EntityFactory.
# Esta classe implementa o padrão de projeto Factory Method.
# O Factory Method é um padrão criacional que fornece uma interface para criar objetos em uma superclasse,
# mas permite que as subclasses alterem o tipo de objetos que serão criados.
class EntityFactory:
    # Comentário do usuário: # na factory nao existe __init__
    # Métodos de fábrica geralmente são estáticos para que não precisem ser chamados em uma instância da classe.
    # Isso permite criar objetos sem a necessidade de instanciar a própria fábrica.

    # Define um método estático chamado get_entity. Métodos estáticos pertencem à classe,
    # mas não precisam de uma instância da classe para serem chamados.
    @staticmethod
    # Este método recebe um nome de entidade (entity_name) como entrada e retorna um objeto do tipo correspondente.
    def get_entity(entity_name: str):
        # Utiliza a estrutura match para verificar o valor de entity_name.
        match entity_name:
            # Caso entity_name seja "Level1Bg":
            case "Level1Bg":
                # Inicializa uma lista vazia para armazenar os objetos de fundo do nível 1.
                list_bg = []
                # Loop para criar 7 pares de imagens de fundo para o nível 1.
                for i in range(7):
                    # Cria duas instâncias da classe Background. A primeira é posicionada no início da tela (x=0).
                    list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
                    # A segunda instância é posicionada no final da tela (x=WIN_WIDTH) para criar um efeito de rolagem contínua.
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                # Retorna a lista contendo todos os objetos de fundo criados para o nível 1.
                return list_bg
            # Caso entity_name seja "Level2Bg":
            case "Level2Bg":
                # Inicializa uma lista vazia para armazenar os objetos de fundo do nível 2.
                list_bg = []
                # Loop para criar 5 pares de imagens de fundo para o nível 2.
                # Número de imagens de fundo para o nível 2.
                for i in range(5):
                    # Cria duas instâncias da classe Background para o nível 2, similar ao nível 1.
                    list_bg.append(Background(f"Level2Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level2Bg{i}", (WIN_WIDTH, 0)))
                # Retorna a lista de objetos de fundo do nível 2.
                return list_bg
            # Caso entity_name seja 'Player1':
            case 'Player1':
                # Cria e retorna uma instância da classe Player para o jogador 1, posicionada perto da borda esquerda e no centro vertical da tela (com um pequeno ajuste).
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            # Caso entity_name seja 'Player2':
            case 'Player2':
                # Cria e retorna uma instância da classe Player para o jogador 2, posicionada de forma semelhante ao jogador 1, mas um pouco abaixo.
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            # Caso entity_name seja 'Enemy1':
            case 'Enemy1':
                # Cria e retorna uma instância da classe Enemy para o tipo 1.
                # O inimigo é posicionado inicialmente fora da tela à direita (WIN_WIDTH + 10) e em uma altura vertical aleatória dentro de uma faixa específica.
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            # Caso entity_name seja 'Enemy2':
            case 'Enemy2':
                # Cria e retorna uma instância da classe Enemy para o tipo 2, com posicionamento similar ao Enemy1.
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        # Se entity_name não corresponder a nenhum dos casos acima, retorna None.
        return None
