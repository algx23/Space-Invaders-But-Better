import sys
import pygame
from core.rocket import Rocket
from core.enemy_manager import EnemyManager


def showScore(screen, score) -> None:
    """Function to create and render the score of the player on the screen

    Args:
        screen (Pygame.Surface): the screen the score is shown onto
        score (int): current score
    """
    score_font = pygame.font.Font()
    score_text = score_font.render(str(score), True, (255, 255, 255), (255, 0, 0))
    score_rect = pygame.rect.Rect(50, 50, 100, 100)
    screen.blit(score_text, score_rect)
    return


def main() -> None:
    """
    this is the main function that handles the main game loop
    """

    pygame.init()

    CLOCK = pygame.time.Clock()
    WIDTH, HEIGHT = 600, 400
    FPS = 60
    score: int = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    bg_color = (0, 0, 0)

    ROCKET = Rocket("rocket.png", WIDTH / 2, HEIGHT / 2, 50, 50, screen)
    enemy_manager = EnemyManager(screen, "enemy.png", 20, 20)

    for num in range(4):
        enemy_manager.createEnemies()

    running = True
    while running:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # enemy_rs = enemy_manager.getEnemyRects()
                    if ROCKET.shoot(enemy_rs):
                        score += 1
                        print(score)

        for projectile in ROCKET.projectiles[:]:
            if not projectile.travel(enemy_rs):
                ROCKET.projectiles.remove(projectile)

        screen.fill(bg_color)
        showScore(screen, score)
        ROCKET.move()
        ROCKET.draw()

        enemy_manager.drawEnemies()
        enemy_rs = enemy_manager.getEnemyRects()

        for projectile in ROCKET.projectiles:
            projectile.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
