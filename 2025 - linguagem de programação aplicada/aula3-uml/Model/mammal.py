#!/usr/bin/python
# -*- coding: utf-8 -*-

from Animal import Animal


class Mammal(Animal):
    def __init__(self, age, height, weight, position, fur):
        Animal.__init__(self, age, height, weight, position)
        self.fur = fur

    def fur_type(self):
        pass
