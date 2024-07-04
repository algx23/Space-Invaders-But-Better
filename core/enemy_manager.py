import pygame
from random import randint
from core.enemy import Enemy


class EnemyManager:

    def __init__(self, screen, enemy_img_path, w, h):
        self.screen = screen
        self.enemy_img_path = enemy_img_path
        self.w = w
        self.h = h
        self.enemies = []

    def createEnemies(self):
        """creates enemies"""
        x = randint(10, self.screen.get_width() - 30)
        y = randint(10, self.screen.get_height() - 30)

        enemy = Enemy("enemy.png", x, y, 20, 20, self.screen)
        self.enemies.append(enemy)

    def drawEnemies(self):
        """draws enemies from enemy list onto the screen"""
        for enemy in self.enemies:
            enemy.random_move()
            enemy.draw()

    def getEnemyRects(self):
        """gets the rect and dimensions of each enemy
        Returns:
            List[Rect]: returns a list of each enemy's Rect
        """
        enemy_rs = []
        for enemy in self.enemies:
            enemy_rs.append(pygame.Rect(enemy.x, enemy.y, enemy.w, enemy.h))

        return enemy_rs
