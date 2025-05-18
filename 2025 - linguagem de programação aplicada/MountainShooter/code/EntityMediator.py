from code.EnemyShot import EnemyShot
from code.Const import WIN_WIDTH
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Enemy import Enemy
from code.Entity import Entity


# Define a classe EntityMediator.
# Esta classe implementa o padrão de projeto Mediator.
# O Mediator define um objeto que encapsula como um conjunto de objetos interage.
# Promove o baixo acoplamento ao evitar que os objetos se refiram explicitamente uns aos outros.
# Em vez disso, eles se comunicam através do objeto mediador.
class EntityMediator:

    # Define um método estático privado para verificar colisões de uma entidade com as bordas da janela.
    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Se a entidade for do tipo Enemy:
        if isinstance(ent, Enemy):
            # Verifica se a borda direita do inimigo saiu da tela pela esquerda.
            if ent.rect.right < 0:
                # Se saiu, define a vida do inimigo para 0 para que seja removido.
                ent.health = 0
        # Se a entidade for do tipo PlayerShot:
        if isinstance(ent, PlayerShot):
            # Verifica se a borda esquerda do tiro do jogador saiu da tela pela direita.
            if ent.rect.left > WIN_WIDTH:
                # Se saiu, define a vida do tiro para 0.
                ent.health = 0
        # Se a entidade for do tipo EnemyShot:
        if isinstance(ent, EnemyShot):
            # Verifica se a borda direita do tiro do inimigo saiu da tela pela esquerda.
            if ent.rect.right <= 0:
                # Se saiu, define a vida do tiro para 0.
                ent.health = 0

        pass

    # Define um método estático privado para verificar colisões entre duas entidades.
    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        # Inicializa uma variável para rastrear se a interação entre as entidades é válida para colisão.
        valid_interaction = False
        # Verifica se ent1 é um Inimigo e ent2 é um Tiro do Jogador.
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            # Se sim, a interação é válida para colisão.
            valid_interaction = True
        # Verifica se ent1 é um Tiro do Jogador e ent2 é um Inimigo.
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            # Se sim, a interação é válida.
            valid_interaction = True
        # Verifica se ent1 é um Jogador e ent2 é um Tiro do Inimigo.
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            # Se sim, a interação é válida.
            valid_interaction = True
        # Verifica se ent1 é um Tiro do Inimigo e ent2 é um Jogador.
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            # Se sim, a interação é válida.
            valid_interaction = True

        # Se a interação for considerada válida para colisão:
        if valid_interaction:  # if valid_interaction == True:
            # Verifica se houve sobreposição entre os retângulos das duas entidades (condição para colisão).
            if (
                ent1.rect.right >= ent2.rect.left
                and ent1.rect.left <= ent2.rect.right
                and ent1.rect.bottom >= ent2.rect.top
                and ent1.rect.top <= ent2.rect.bottom
            ):
                # Se houve colisão, diminui a vida de ent1 pelo dano de ent2.
                ent1.health -= ent2.damage
                # Diminui a vida de ent2 pelo dano de ent1.
                ent2.health -= ent1.damage
                # Registra em ent1 qual foi a última entidade que lhe causou dano.
                ent1.last_dmg = ent2.name
                # Registra em ent2 qual foi a última entidade que lhe causou dano.
                ent2.last_dmg = ent1.name

    # Define um método estático privado para dar pontos ao jogador que destruiu o inimigo.
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        # Verifica se o inimigo foi destruído por um tiro do Player1.
        if enemy.last_dmg == "Player1Shot":
            # Itera pela lista de entidades.
            for ent in entity_list:
                # Se encontrar a entidade com o nome "Player1".
                if ent.name == "Player1":
                    # Adiciona a pontuação do inimigo à pontuação do Player1.
                    ent.score += enemy.score
        # Verifica se o inimigo foi destruído por um tiro do Player2.
        elif enemy.last_dmg == "Player2Shot":
            # Itera pela lista de entidades.
            for ent in entity_list:
                # Se encontrar a entidade com o nome "Player2".
                if ent.name == "Player2":
                    # Adiciona a pontuação do inimigo à pontuação do Player2.
                    ent.score += enemy.score

    # Define um método estático para verificar colisões entre todas as entidades da lista.
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # Itera pela lista de entidades usando o índice.
        for i in range(len(entity_list)):
            # Obtém a primeira entidade a ser verificada.
            entity1 = entity_list[i]
            # Chama o método para verificar a colisão da entidade com a janela.
            EntityMediator.__verify_collision_window(entity1)
            # Itera pela lista de entidades a partir do próximo elemento de entity1 para evitar verificar colisões duplicadas.
            for j in range(i + 1, len(entity_list)):
                # Obtém a segunda entidade a ser verificada.
                entity2 = entity_list[j]
                # Chama o método para verificar a colisão entre entity1 e entity2.
                EntityMediator.__verify_collision_entity(entity1, entity2)

    # Define um método estático para verificar a vida das entidades e remover aquelas com vida <= 0.
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Itera por cada entidade na lista.
        for ent in entity_list:
            # Verifica se a vida da entidade é menor ou igual a 0.
            if ent.health <= 0:
                # Se a entidade for um inimigo.
                if isinstance(ent, Enemy):
                    # Chama o método para dar a pontuação ao jogador que o destruiu.
                    EntityMediator.__give_score(ent, entity_list)
                # Remove a entidade da lista.
                entity_list.remove(ent)
