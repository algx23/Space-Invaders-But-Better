import pygame
from core.game_object import GameObject


class Projectile(GameObject):

    def __init__(self, rocket, screen):
        super().__init__("projectile.png", rocket.x, rocket.y, 30, 30)

        self.state = 0
        self.velocity = 3
        self.rocket = rocket
        self.screen = screen
        self.x = rocket.x
        self.y = rocket.y

    def travel(self, screen):
        while self.y - self.velocity >= 0:
            self.y -= self.velocity
            print(self.y)
            screen.blit(self.image, (self.x, self.y))
        print("finished")
        return
