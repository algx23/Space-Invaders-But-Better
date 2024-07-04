import sys
import pygame
from core.rocket import Rocket
from core.enemy_manager import EnemyManager


pygame.init()


CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 600, 400
FPS = 60
KEY = pygame.key.get_pressed()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/images/background.png")

ROCKET = Rocket("rocket.png", WIDTH / 2, HEIGHT / 2, 50, 50, screen)
enemy_manager = EnemyManager(screen, "enemy.png", 20, 20)


for i in range(5):
    enemy_manager.createEnemies()


running = True

while running:
    KEY = pygame.key.get_pressed()
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    ROCKET.move()
    ROCKET.update_position()
    ROCKET.draw()

    enemy_manager.drawEnemies()
    enemy_rs = enemy_manager.getEnemyRects()

    if KEY[pygame.K_o]:
        ROCKET.shoot(enemy_rs)

    pygame.display.flip()


pygame.quit()
sys.exit()
