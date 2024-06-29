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

    def travel(self, enemy_x, enemy_y):
        print(f"before: {self.x}, {self.y}")
        print("traveling to enemy at pos: ", enemy_x, enemy_y)
        while self.y > 0:
            self.y -= self.velocity

            self.screen.blit(self.image, (self.x, self.y))
            if self.x == enemy_x + 20 or self.y == enemy_y + 20:
                print("collision detected")
        pygame.display.flip()
