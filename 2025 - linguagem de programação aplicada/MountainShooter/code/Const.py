import pygame


# C

# Define uma tupla de cor para laranja no formato RGB (Red, Green, Blue).
COLOR_ORANGE = (255, 128, 0)
# Define uma tupla de cor para branco.
COLOR_WHITE = (255, 255, 255)
# Define uma tupla de cor para amarelo.
COLOR_YELLOW = (255, 201, 14)
# Define uma tupla de cor para verde.
COLOR_GREEN = (0, 128, 0)
# Define uma tupla de cor para ciano.
COLOR_CYAN = (0, 128, 128)

# E

# Define um dicionário para armazenar a pontuação de diferentes entidades.
# Este uso de dicionários para configurar diferentes aspectos de entidades pode ser visto como uma forma de Data Transfer Object (DTO)
# ou Value Object, onde os dados são organizados de forma clara e acessível.
ENTITY_SCORE = {
    # Pontuação para diferentes elementos de fundo do nível 1.
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level1Bg5": 0,
    "Level1Bg6": 0,
    # Pontuação para diferentes elementos de fundo do nível 2.
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    # Pontuação para o jogador 1.
    "Player1": 0,
    # Pontuação para o tiro do jogador 1.
    "Player1Shot": 0,
    # Pontuação para o jogador 2.
    "Player2": 0,
    # Pontuação para o tiro do jogador 2.
    "Player2Shot": 0,
    # Pontuação ao destruir o inimigo do tipo 1.
    "Enemy1": 100,
    # Pontuação para o tiro do inimigo do tipo 1.
    "Enemy1Shot": 0,
    # Pontuação ao destruir o inimigo do tipo 2.
    "Enemy2": 125,
    # Pontuação para o tiro do inimigo do tipo 2.
    "Enemy2Shot": 0,
}

# Define um dicionário para armazenar o dano causado por diferentes entidades do jogo.
ENTITY_DAMAGE = {
    # Dano causado por diferentes elementos de fundo do nível 1.
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level1Bg5": 0,
    "Level1Bg6": 0,
    # Dano causado por diferentes elementos de fundo do nível 2.
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    # Dano causado pelo jogador 1 ao colidir.
    "Player1": 1,
    # Dano causado pelo tiro do jogador 1.
    "Player1Shot": 25,
    # Dano causado pelo jogador 2 ao colidir.
    "Player2": 1,
    # Dano causado pelo tiro do jogador 2.
    "Player2Shot": 20,
    # Dano causado pelo inimigo do tipo 1 ao colidir.
    "Enemy1": 1,
    # Dano causado pelo tiro do inimigo do tipo 1.
    "Enemy1Shot": 20,
    # Dano causado pelo inimigo do tipo 2 ao colidir.
    "Enemy2": 1,
    # Dano causado pelo tiro do inimigo do tipo 2.
    "Enemy2Shot": 15,
}

# Define um dicionário para armazenar a vida (health points) de diferentes entidades do jogo.
ENTITY_HEALTH = {
    # Vida para diferentes elementos de fundo do nível 1 (muita vida, provavelmente indestrutíveis).
    "Level1Bg0": 999,
    "Level1Bg1": 999,
    "Level1Bg2": 999,
    "Level1Bg3": 999,
    "Level1Bg4": 999,
    "Level1Bg5": 999,
    "Level1Bg6": 999,
    # Vida para diferentes elementos de fundo do nível 2.
    "Level2Bg0": 999,
    "Level2Bg1": 999,
    "Level2Bg2": 999,
    "Level2Bg3": 999,
    "Level2Bg4": 999,
    # Vida do jogador 1.
    "Player1": 300,
    # Vida do tiro do jogador 1 (provavelmente 1 para desaparecer ao atingir algo).
    "Player1Shot": 1,
    # Vida do jogador 2.
    "Player2": 300,
    # Vida do tiro do jogador 2.
    "Player2Shot": 1,
    # Vida do inimigo do tipo 1.
    "Enemy1": 50,
    # Vida do tiro do inimigo do tipo 1.
    "Enemy1Shot": 1,
    # Vida do inimigo do tipo 2.
    "Enemy2": 60,
    # Vida do tiro do inimigo do tipo 2.
    "Enemy2Shot": 1,
}

# Define um dicionário para armazenar o atraso entre os tiros de diferentes entidades (em frames ou ticks do jogo).
ENTITY_SHOT_DELAY = {
    # Atraso entre os tiros do jogador 1.
    "Player1": 20,
    # Atraso entre os tiros do jogador 2.
    "Player2": 15,
    # Atraso entre os tiros do inimigo do tipo 1.
    "Enemy1": 100,
    # Atraso entre os tiros do inimigo do tipo 2.
    "Enemy2": 200,
}

# Define um dicionário para armazenar a velocidade de movimento de diferentes entidades.
ENTITY_SPEED = {
    # Velocidade dos diferentes elementos de fundo do nível 1 (diferentes para criar efeito de paralaxe).
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Level1Bg4": 4,
    "Level1Bg5": 5,
    "Level1Bg6": 6,
    # Velocidade dos diferentes elementos de fundo do nível 2.
    "Level2Bg0": 0,
    "Level2Bg1": 1,
    "Level2Bg2": 2,
    "Level2Bg3": 3,
    "Level2Bg4": 4,
    # Velocidade do jogador 1.
    "Player1": 3,
    # Velocidade do tiro do jogador 1.
    "Player1Shot": 1,
    # Velocidade do jogador 2.
    "Player2": 3,
    # Velocidade do tiro do jogador 2.
    "Player2Shot": 3,
    # Velocidade do inimigo do tipo 1.
    "Enemy1": 1,
    # Velocidade do tiro do inimigo do tipo 1.
    "Enemy1Shot": 5,
    # Velocidade do inimigo do tipo 2.
    "Enemy2": 1,
    # Velocidade do tiro do inimigo do tipo 2.
    "Enemy2Shot": 2,
}

# Define um evento de usuário personalizado para o surgimento de um novo inimigo.
EVENT_ENEMY = pygame.USEREVENT + 1

# Define um evento de usuário personalizado para indicar um tempo limite (timer).
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M

# Define uma tupla contendo as opções do menu do jogo.
MENU_OPTION = (
    "NEW GAME 1P",
    "NEW GAME 2P - COOPERATIVE",
    "NEW GAME 2P - COMPETITIVE",
    "SCORE",
    "EXIT",
)

# P

# Define dicionários para mapear teclas de controle para cada jogador.
# Novamente, o uso de dicionários para agrupar informações relacionadas pode ser visto como um DTO/Value Object.
PLAYER_KEY_UP = {"Player1": pygame.K_UP, "Player2": pygame.K_w}
# Define um dicionário que mapeia as teclas para mover para baixo para cada jogador.
PLAYER_KEY_DOWN = {"Player1": pygame.K_DOWN, "Player2": pygame.K_s}
# Define um dicionário que mapeia as teclas para mover para a esquerda para cada jogador.
PLAYER_KEY_LEFT = {"Player1": pygame.K_LEFT, "Player2": pygame.K_a}
# Define um dicionário que mapeia as teclas para mover para a direita para cada jogador.
PLAYER_KEY_RIGHT = {"Player1": pygame.K_RIGHT, "Player2": pygame.K_d}
# Define um dicionário que mapeia as teclas para atirar para cada jogador.
PLAYER_KEY_SHOOT = {"Player1": pygame.K_RCTRL, "Player2": pygame.K_LCTRL}

# S

# Define o tempo (em milissegundos) para o surgimento de novos inimigos.
SPAW_TIME = 4000

# T

# Define o intervalo de tempo (em milissegundos) para cada passo do timer.
TIMEOUT_STEP = 100  # 100ms
# Define o tempo limite total para o nível (em milissegundos).
TIMEOUT_LEVEL = 20000  # 20s


# W

# Define a largura da janela do jogo.
WIN_WIDTH = 576
# Define a altura da janela do jogo.
WIN_HEIGHT = 324


# S

# Define um dicionário para armazenar as posições de diferentes elementos da tela de pontuação.
SCORE_POS = {
    # Posição do título da tela de pontuação.
    "Title": (WIN_WIDTH / 2, 50),
    # Posição da mensagem para inserir o nome.
    "EnterName": (WIN_WIDTH / 2, 80),
    # Posição do rótulo para o nome.
    "Label": (WIN_WIDTH / 2, 90),
    # Posição para exibir o nome.
    "Name": (WIN_WIDTH / 2, 110),
    # Posição para a primeira pontuação na lista.
    0: (WIN_WIDTH / 2, 110),
    # Posição para a segunda pontuação.
    1: (WIN_WIDTH / 2, 130),
    # Posição para a terceira pontuação.
    2: (WIN_WIDTH / 2, 150),
    # Posição para a quarta pontuação.
    3: (WIN_WIDTH / 2, 170),
    # Posição para a quinta pontuação.
    4: (WIN_WIDTH / 2, 190),
    # Posição para a sexta pontuação.
    5: (WIN_WIDTH / 2, 210),
    # Posição para a sétima pontuação.
    6: (WIN_WIDTH / 2, 230),
    # Posição para a oitava pontuação.
    7: (WIN_WIDTH / 2, 250),
    # Posição para a nona pontuação.
    8: (WIN_WIDTH / 2, 270),
    # Posição para a décima pontuação.
    9: (WIN_WIDTH / 2, 290),
}
