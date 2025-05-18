from code.Const import ENTITY_SPEED
from code.Entity import Entity


# Define a classe PlayerShot, que herda da classe Entity.
# Este é um exemplo do padrão de projeto Inheritance.
class PlayerShot(Entity):

    # Método construtor da classe PlayerShot.
    def __init__(self, name: str, position: tuple):
        # Chama o construtor da classe pai (Entity).
        super().__init__(name, position)

    # Define o método move para controlar o movimento do tiro do jogador.
    def move(self,):
        # Move o tiro do jogador para a direita, adicionando a sua velocidade à coordenada x do centro do seu retângulo. A velocidade é obtida do dicionário ENTITY_SPEED.
        self.rect.centerx += ENTITY_SPEED[self.name]
        
