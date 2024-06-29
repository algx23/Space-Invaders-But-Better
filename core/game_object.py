import os
import pygame

# from core.rocket import Rocket


class GameObject:
    """all ,,entities" in this game will be considered gameObject
    initialisation to load the image, and if needed, resize it, and with a draw
    function that blits the image to the required position in the screen
    initialisation to load the image, and if needed, resize it, and with a draw
    function that blits the image to the required position in the screen"""

    def __init__(self, image_path, screen, x, y, w=None, h=None):
        image_path = image_path
        self.image = pygame.image.load(
            os.path.join("assets\\images", f"{image_path}")
        ).convert_alpha()
        self.x = x
        self.y = y
        self.screen = screen

        if w and h:
            self.image = pygame.transform.scale(self.image, (w, h))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        return
