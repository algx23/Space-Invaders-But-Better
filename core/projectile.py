import pygame
from core.game_object import GameObject


class Projectile(GameObject):

    def __init__(self, x, y, screen) -> None:
        """initialises the projectile class

        Args:
            x (int): starting X co-ordinate of the projectile
            y (int): starting Y co-ordinate of the projectile
            screen (Surface): screen the projectiles will be drawn on to -
              in this case just the main window
        """
        super().__init__("bullet.png", x, y, 1, 25)

        self.velocity = 1
        self.screen = screen
        self.x = x
        self.y = y
        self.w = 1
        self.h = 25

    # passing in the enemy rect, to check for collision between the projectile and the thing
    def travel(self, enemy_rs) -> None:
        """function to model the travelling of the projectiles shot from the rocket

        Args:
            enemy_rs (List[rect]): list of rectangles corresponding to each enemy
        """
        while self.y > 0:
            projectile_r = pygame.Rect(self.x, self.y, self.w, self.h)

            self.y -= self.velocity
            self.screen.blit(self.image, (self.x, self.y))

            if self.checkHit(enemy_rs):
                print("collision")
                break
            else:
                print("no collision")

            pygame.display.flip()

    def checkHit(self, enemy_rs) -> bool:
        """checks if the projectile hit the enemy

        Args:
            enemy_r (rect): a rect that contains the enemy position
            projectile_r (rect): rect that tracks the projectile position

        Returns:
            bool: returns True if the projectile hit, otherwise false
        """

        projectile_r = pygame.Rect(self.x, self.y, self.w, self.h)
        for enemy in enemy_rs:
            if enemy.colliderect(projectile_r):
                return True
        return False
