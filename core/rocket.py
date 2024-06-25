import pygame
from core.game_object import GameObject


class Rocket(GameObject):
    def __init__(self, image_path, x, y, w, h):
        super().__init__(image_path, x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 1

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and (self.y - (0.5 * self.speed)) > 0:
            self.y -= self.speed
        if key[pygame.K_DOWN] and (self.y + (0.5 * self.speed)) < (400 - self.w):
            self.y += self.speed
        if key[pygame.K_LEFT] and (self.x - (0.5 * self.speed)) > 0:
            self.x -= self.speed
        if key[pygame.K_RIGHT] and (self.x + (0.5 * self.speed)) < (600 - self.w):
            self.x += self.speed
