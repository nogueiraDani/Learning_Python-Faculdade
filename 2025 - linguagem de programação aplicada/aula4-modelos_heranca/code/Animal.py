#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


# craindo classe abstrata
class Animal(ABC):
    def __init__(self, age, height, weight, position):
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        pass

    @abstractmethod
    def move_x(self, ):
        pass

    @abstractmethod
    def move_y(self, ):
        pass

    @abstractmethod
    def move_z(self, ):
        pass
