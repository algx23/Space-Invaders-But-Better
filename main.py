import sys
import pygame
from core.rocket import Rocket
from core.enemy_manager import EnemyManager


def main():

    pygame.init()

    CLOCK = pygame.time.Clock()
    WIDTH, HEIGHT = 600, 400
    FPS = 60

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    bg_color = (0, 0, 0)

    ROCKET = Rocket("rocket.png", WIDTH / 2, HEIGHT / 2, 50, 50, screen)
    enemy_manager = EnemyManager(screen, "enemy.png", 20, 20)

    for i in range(5):
        enemy_manager.createEnemies()

    running = True

    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    enemy_rs = enemy_manager.getEnemyRects()
                    ROCKET.shoot(enemy_rs)

        screen.fill(bg_color)
        ROCKET.move()
        ROCKET.draw()

        enemy_manager.drawEnemies()
        enemy_manager.getEnemyRects()

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
