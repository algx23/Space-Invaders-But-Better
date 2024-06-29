import sys
import pygame
from core.rocket import Rocket
from core.enemy import Enemy
from random import randint


pygame.init()


CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 600, 400
FPS = 60
KEY = pygame.key.get_pressed()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/images/background.png")

ROCKET = Rocket("rocket.png", WIDTH / 2, HEIGHT / 2, 50, 50, screen)


# creating the enemy and random positions
x = randint(10, WIDTH - 10)
y = randint(10, HEIGHT - 10)
print(x, y)
ENEMY = Enemy("enemy.png", x, y, 20, 20, screen)

background = pygame.transform.scale(background, (WIDTH, HEIGHT))


running = True

while running:
    KEY = pygame.key.get_pressed()
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    ROCKET.move()
    ROCKET.draw()
    ENEMY.draw()

    if KEY[pygame.K_o]:
        print("enemy:", ENEMY.x_pos, ENEMY.y_pos)
        ROCKET.shoot(ENEMY.x_pos, ENEMY.y_pos)

    pygame.display.flip()


pygame.quit()
sys.exit()
