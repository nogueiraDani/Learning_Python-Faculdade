#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

from code.Animal import Animal


class Mammal(Animal, ABC):
    def __init__(self, age, height, weight, position, fur):
        Animal.__init__(self, age, height, weight, position)
        self.fur = fur

    def fur_type(self):
        return self.fur
