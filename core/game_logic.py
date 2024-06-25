import pygame
import os


class Game:

    def __init__(self):
        self.background = pygame.image.load(
            os.path.join("assets", "background.jpg")
        ).convert_alpha()

        self.rocket = pygame.image.load(
            os.path.join("assets", "rocket.png")
        ).convert_alpha()
        self.background = pygame.transform.scale(self.background, (800, 800))
        self.rocket = pygame.transform.scale(self.rocket, (100, 100))
