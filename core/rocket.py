import pygame
from core.game_object import GameObject
from core.projectile import Projectile


class Rocket(GameObject):
    def __init__(self, image_path, x, y, w, h, screen):
        super().__init__(image_path, screen, x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 1
        self.projectiles = []
        self.screen = screen

    def move(self) -> None:
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and (self.y - (0.5 * self.speed)) > 0:
            self.y -= self.speed
        if key[pygame.K_DOWN] and (self.y + (0.5 * self.speed)) < (400 - self.w):
            self.y += self.speed
        if key[pygame.K_LEFT] and (self.x - (0.5 * self.speed)) > 0:
            self.x -= self.speed
        if key[pygame.K_RIGHT] and (self.x + (0.5 * self.speed)) < (600 - self.w):
            self.x += self.speed

    def shoot(self, enemy_r) -> None:
        # self.x = self.x + self.w // 2
        projectile = Projectile(self.x, self.y, self.screen)
        projectile.travel(enemy_r)
