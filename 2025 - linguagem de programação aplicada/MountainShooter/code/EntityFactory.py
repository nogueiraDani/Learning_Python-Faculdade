#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Any

from code.Background import Background
from code.Const import WIN_WIDTH


# entidade Fabrica resposavel por gerar player, enemy e background
class EntityFactory:
# na factory nao existe __init__
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
                return list_bg
        return None
