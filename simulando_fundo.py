import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Resgate nas Estrelas")  # Novo título da janela

# Definindo cores
WHITE = (255, 255, 255)
YELLOW = (200, 200, 0)
LIGHT_BLUE = (173, 216, 230)
LIGHT_PEACH = (246, 237, 233)
LIGHT_PINK = (236, 219, 211)
LIGHT_GRAY_GREEN = (236, 239, 232)
LIGHT_BLUE_GRAY = (221, 231, 239)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
COLORS = [WHITE, YELLOW, LIGHT_BLUE, LIGHT_PEACH, LIGHT_GRAY_GREEN, LIGHT_BLUE_GRAY]

# Função para criar estrelas
def create_stars(num_stars, max_speed):
    stars = []
    for _ in range(num_stars):
        x = random.randint(0, 800)
        y = random.randint(0, 800)
        color = random.choice(COLORS)
        speed = random.randint(1, max_speed)
        stars.append([x, y, color, speed])
    return stars

# Função para desenhar estrelas no fundo
def draw_stars(screen, stars):
    for star in stars:
        screen.set_at((star[0], star[1]), star[2])

# Função para atualizar posição das estrelas
def update_stars(stars):
    for star in stars:
        star[1] += star[3]  # Mover a estrela para baixo de acordo com a velocidade
        if star[1] > 800:  # Se a estrela sair da tela (parte inferior)
            star[1] = 0  # Reposicionar estrela no topo
            star[0] = random.randint(0, 800)  # Nova posição horizontal aleatória
            star[2] = random.choice(COLORS)  # Nova cor aleatória
            star[3] = random.randint(1, 3)  # Nova velocidade aleatória

# Número de estrelas por camada
num_stars_layer1 = 50
num_stars_layer2 = 50
num_stars_layer3 = 50

# Criar estrelas para cada camada
stars_layer1 = create_stars(num_stars_layer1, 1)  # Camada mais lenta
stars_layer2 = create_stars(num_stars_layer2, 2)  # Camada intermediária
stars_layer3 = create_stars(num_stars_layer3, 3)  # Camada mais rápida

# Função principal do jogo
def game_loop():
    clock = pygame.time.Clock()
    running = True
    score = 0
    energy = 100

    font = pygame.font.Font(None, 24)

    while running:
        clock.tick(30)  # Define a taxa de frames por segundo (FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenhar fundo preto
        screen.fill(BLACK)
        
        # Atualizar e desenhar estrelas de cada camada
        update_stars(stars_layer1)
        draw_stars(screen, stars_layer1)
        
        update_stars(stars_layer2)
        draw_stars(screen, stars_layer2)
        
        update_stars(stars_layer3)
        draw_stars(screen, stars_layer3)

        # Exibir pontuação
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Exibir barra de energia
        pygame.draw.rect(screen, RED, (550, 10, 240, 15))  # Barra vermelha (fundo)
        pygame.draw.rect(screen, GREEN, (550, 10, energy * 2.4, 15))  # Barra verde (energia)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Iniciar o jogo
game_loop()
