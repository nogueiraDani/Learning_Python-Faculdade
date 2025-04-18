from code.Cat import Cat
from code.Dog import Dog


class AnimalFactory:

    @staticmethod
    def new_animal(animal_type, age, weight, height, fur):
        match animal_type:
            case 'dog':
                return Dog(age=age, height=height, weight=weight, position=0, fur=fur)
            case 'cat':
                return Cat(age=age, height=height, weight=weight, position=20, fur=fur)
        return None
