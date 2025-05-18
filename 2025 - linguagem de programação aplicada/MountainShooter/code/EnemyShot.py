from code.Const import ENTITY_SPEED
from code.Entity import Entity


# Define a classe EnemyShot, que herda da classe Entity.
# Este é outro exemplo do padrão de projeto Inheritance.
class EnemyShot(Entity):

    # Método construtor da classe EnemyShot. É chamado quando um objeto EnemyShot é criado.
    def __init__(self, name: str, position: tuple):
        # Chama o construtor da classe pai (Entity) para inicializar os atributos básicos da entidade.
        super().__init__(name, position)

    # Define o método move para controlar o movimento do tiro do inimigo.
    def move(self, ):
        # Move o tiro do inimigo para a esquerda, subtraindo a sua velocidade da coordenada x do centro do seu retângulo. A velocidade é obtida do dicionário ENTITY_SPEED.
        self.rect.centerx -= ENTITY_SPEED[self.name]
