class Animal: # definindo calsse pai
    def __init__(self, name: str, height: float, weight: float, position: tuple):
        self._name = name
        self._height = height
        self._weight = weight
        self._position = position

    def move_x(self):
        self._position[0] += 1

    def move_y(self):
        self._position[1] += 1

    def move_z(self):
        self._position[2] += 1


class Cat(Animal): # criando classe q herda Animal
    def __init__(self, name: str, height: float, weight: float, position: tuple):
        Animal.__init__(self, name, height, weight, position) #buscando o construtor da classe pai == super()

    def get_name(self):
        return self._name

    def move_z(self): #reescrevendo a funcao agora na classe cat
        self._position[2] += 2

floky = Cat(name='Floky', height=50, weight=100, position=('x', 100, 'y', 50))
print(floky.get_name())