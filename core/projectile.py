import pygame
from core.game_object import GameObject


class Projectile(GameObject):

    def __init__(self, x, y, screen):
        super().__init__("bullet.png", x, y, 1, 25)

        # debugging stuffs
        if not hasattr(self, "image"):
            print("initialization failed")
        else:
            print("Initialization success")

        self.velocity = 1
        self.screen = screen
        self.x = x
        self.y = y
        self.w = 1
        self.h = 25

    # passing in the enemy rect, to check for collision between the projectile and the thing
    def travel(self, enemy_rs) -> None:
        while self.y > 0:
            projectile_r = pygame.Rect(self.x, self.y, self.w, self.h)

            self.y -= self.velocity
            self.screen.blit(self.image, (self.x, self.y))

            if self.checkHit(enemy_rs, projectile_r):
                print("collision")
                break
            else:
                print("no collision")
        pygame.display.flip()

    def checkHit(self, enemy_rs, projectile_r) -> bool:
        """checks if the projectile hit the enemy

        Args:
            enemy_r (rect): a rect that contains the enemy position
            projectile_r (rect): rect that tracks the projectile position

        Returns:
            bool: returns True if the projectile hit, otherwise false
        """
        for enemy in enemy_rs:
            if enemy.colliderect(projectile_r):
                return True
        return False
