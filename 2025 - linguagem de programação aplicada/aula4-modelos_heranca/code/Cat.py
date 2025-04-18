#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Mammal import Mammal


class Cat(Mammal):

    def __init__(self, age, height, weight, position, fur):
        super().__init__(age, height, weight, position, fur)
        self.breed = None
        self.tail_fur = None

    def tail_fur_type(self, fur_type=None):
        if fur_type:
            self.tail_fur = fur_type
        return self.tail_fur

    def move_x(self):
        pass

    def move_y(self):
        pass

    def move_z(self):
        pass
