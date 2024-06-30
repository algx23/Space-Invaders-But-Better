import pygame
from core.game_object import GameObject


class Projectile(GameObject):

    def __init__(self, x, y, screen):
        super().__init__("bullet.png", x, y, 25, 1)

        # debugging stuffs
        if not hasattr(self, "image"):
            print("initialization failed")
        else:
            print("Initialization success")

        self.velocity = 1
        self.screen = screen
        self.x = x
        self.y = y

    # passing in the enemy rect, to check for collision between the projectile and the thing
    def travel(self, enemy_r):
        print(f"before: {self.x}, {self.y}")
        while self.y > 0:
            pygame.Rect(self.x, self.y, 25, 1)
            self.y -= self.velocity
            self.screen.blit(self.image, (self.x, self.y))
            projectile_pos = (self.x, self.y)
            if pygame.Rect.collidepoint(enemy_r, projectile_pos):
                print("collision detected")
        pygame.display.flip()
