#!/usr/bin/python
# -*- coding: utf-8 -*-

from Mammal import Mammal


class Cat(Mammal):
    def __init__(self, age, height, weight, position, fur):
        super().__init__(age, height, weight, position, fur)
        self.breed = None
        self.tail_fur = None

    def tail_fur_type(self, ):
        pass
