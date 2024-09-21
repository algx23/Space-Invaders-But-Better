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
        super().__init__("bullet.png", x, y, 20, 25)

        self.velocity = 1
        self.screen = screen
        self.x = x
        self.y = y
        self.w = 20
        self.h = 25

    def draw(self):
        # print("drawing..")
        self.update_position(self.x, self.y)

        self.screen.blit(self.image, (self.x, self.y))
        return

    # passing in the enemy rect, to check for collision between the projectile and the thing

    def travel(self, enemy_rs) -> None:

        projectile_r = pygame.Rect(self.x, self.y, self.w, self.h)
        while self.y > 0:
            self.y -= self.velocity

            self.draw()
            pygame.display.update()

        for rect in enemy_rs:
            if pygame.Rect.colliderect(projectile_r, rect):
                print(1)
            return
