# como definir uma classe

class Dog:

    # anotacao 01
    # def __init__(self): # __init__ == construtor
    #     pass # pass == a criar construtor vazio

    # anotacao 02
    # def __init__(self): # self == this
    #     self.age = 10 # quando houver atributos sempre inicia-los dentro do init

    # anotacao 03
    # def __init__(self, name, age):  # iniciando o contrutor com atributos do objeto
    #     self.name = name

    # anotacao 04

    # atributo da classe
    # family = 'Canidae'
    #
    # def __init__(self, name, age):  # iniciando o contrutor com atributos do objeto
    #     self.name = name
    #     self.age = age

    # anotacao 05
    # iniciando o construtor com atributo tipado
    # def __init__(self, age: int):
    #     self.age :int = age

    # anotacao 07
    def __init__(self, age: int, name: str):
        self._age: int = age  # _xpto indica que é um atributo privado e nao deve ser modificado fora da classe
        self.__name: str = name  # __xpto faz o interpretador gerar erro, nesse caso o atributo é protegido

    def get_age(self) -> int:  # -> int define o tipo do dado do return
        return self._age

    def get_name(self) -> str: # -> str define o tipo do dado do return
        return self.__name


# prints-------------------
# anotacao 01
# bingo = Dog() # como criar uma instancia de Dog
# print(bingo)
#
# anotacao 02
# caramelo = Dog()
# print(f'A idade do caramelo é: {caramelo.age}')

# anotacao 03
# bingo = Dog('Bingo', 20)
# print(f'O nome do cachorro é {bingo.name} e a sua idade é {bingo.age}')

# anotacao 04
# bingo = Dog('Bingo', 20)
# print(f'O nome do cachorro é {bingo.name} e a sua idade é {bingo.age}')
# print(f'A familia do cachorro é {bingo.family}')
# print(f'A familia do {bingo.name} é {Dog.family}')

# anotacao 06
# bingo = Dog(10)
# # como descobrir a classe do objeto
# print(f'Bingo é um objeto de qual classe? R: {bingo.__class__.__name__}')

# anotacao 07
# bingo = Dog(2, "Bingo")
# print(f'A idade de {bingo.get_name()} é {bingo.get_age()} anos.')