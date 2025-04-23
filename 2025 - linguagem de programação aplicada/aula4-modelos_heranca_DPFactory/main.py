from code.Cat import Cat
from code.dp_factory.AnimalFactory import AnimalFactory
from code.dp_builder.CasaBuilder import CasaBuilder

# criando objeto sem desgin pattern(dp)
new_cat_one = Cat(age=2, height=15, weight=20, position=15, fur='branco')

print(new_cat_one.fur)

# ------------------------------------------------------------------------------#
# Udando Design pattern Factory - pedindo para a Factory um objetc de cada tipo
new_dog = AnimalFactory.new_animal(animal_type='dog', age=5, weight=10, height=20, fur='marrom')
new_cat = AnimalFactory.new_animal(animal_type='cat', age=10, weight=8, height=20, fur='preto')

print(new_dog.position)
print(new_cat.position)

# ------------------------------------------------------------------------------#
# Usando Design pattern Builder - construindo com Builder um objetc
# Construindo uma casa com garagem e jardim
builder_casa = CasaBuilder()
casa = builder_casa.set_num_quartos(3).\
                    set_num_banheiros(2).\
                    adicionar_garagem().\
                    adicionar_jardim().\
                    obter_casa()
print("Características da casa:", casa)

# Construindo outra casa sem garagem e com 4 quartos
outra_casa = CasaBuilder().set_num_quartos(4).set_num_banheiros(3).obter_casa()
print("Características da outra casa:", outra_casa)
