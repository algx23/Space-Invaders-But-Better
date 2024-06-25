import pygame
from core.rocket import Rocket
from core.projectile import Projectile

pygame.init()


WIDTH, HEIGHT = 600, 400
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/images/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


ROCKET = Rocket("rocket.png", WIDTH / 2, HEIGHT / 2, 50, 50)
projectile_list = []
projectile = Projectile(ROCKET, screen)

print("screen rect", screen.get_rect())


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            projectile.draw(screen)
            projectile.travel(screen)

    screen.fill((0, 0, 0))
    ROCKET.move()
    ROCKET.draw(screen)
    pygame.display.update()


pygame.quit()
