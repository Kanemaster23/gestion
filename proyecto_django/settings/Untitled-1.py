import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Pinball")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Configuración de la bola
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = random.choice([-4, 4])
ball_speed_y = random.choice([-4, 4])

# Configuración de los obstáculos
obstacles = []
for _ in range(5):
    obstacle_x = random.randint(100, WIDTH - 100)
    obstacle_y = random.randint(100, HEIGHT - 100)
    obstacles.append(pygame.Rect(obstacle_x, obstacle_y, 50, 10))

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Función para mostrar la puntuación
def show_score():
    score_text = font.render(f"Puntuación: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

# Función para detectar colisión entre la bola y el rectángulo
def collide_circle_rect(circle_pos, radius, rect):
    circle_distance_x = abs(circle_pos[0] - rect.centerx)
    circle_distance_y = abs(circle_pos[1] - rect.centery)

    if circle_distance_x > (rect.width / 2 + radius) or circle_distance_y > (rect.height / 2 + radius):
        return False

    if circle_distance_x <= (rect.width / 2) or circle_distance_y <= (rect.height / 2):
        return True

    corner_distance_sq = (circle_distance_x - rect.width / 2) ** 2 + (circle_distance_y - rect.height / 2) ** 2

    return corner_distance_sq <= (radius ** 2)

# Función principal del juego
def game_loop():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, score
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mover la bola
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisiones con los bordes
        if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
            ball_speed_x *= -1  # Rebotar en el borde izquierdo/derecho
        if ball_y <= ball_radius:
            ball_speed_y *= -1  # Rebotar en el borde superior
        if ball_y >= HEIGHT - ball_radius:
            ball_speed_y *= -1  # Rebotar en el borde inferior

        # Dibujar la bola
        pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

        # Dibujar obstáculos
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)

        # Detección de colisiones con obstáculos
        for obstacle in obstacles:
            if collide_circle_rect((ball_x, ball_y), ball_radius, obstacle):
                ball_speed_y *= -1  # Rebotar en el obstáculo
                score += 1  # Aumentar puntuación
                obstacles.remove(obstacle)  # Eliminar el obstáculo al ser golpeado

        # Mostrar puntuación
        show_score()

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Ejecutar el juego
game_loop()       