import pygame
from core.game_object import GameObject
from core.projectile import Projectile


class Rocket(GameObject, pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, w, h, screen) -> None:
        super().__init__(image_path, screen, x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 1
        self.projectiles: list[int] = []
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

        self.update_position(self.x, self.y)

    def shoot(self, enemy_rs) -> bool:
        """shoots a projectile when the FIRE key is pressed

        Args:
            enemy_rs (List[rect]): a list of all enemy positions based on the co ordinates of their respective rects
        """
        projectile = Projectile(self.x, self.y, self.screen)
        self.projectiles.append(projectile)

        for projectile in self.projectiles:
            if projectile.y < 0:
                self.projectiles.remove(projectile)
            return projectile.travel(enemy_rs)
