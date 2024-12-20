import pygame
from core.game_object import GameObject
from random import randint, choice


class Enemy(GameObject, pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, w, h, screen):
        super().__init__(image_path, screen, x, y, w, h)
        self.x_pos = x
        self.y_pos = y
        self.w = w
        self.h = h
        self.rect = self.image.get_frect(topleft=(self.x_pos, self.y_pos))

        # index 0: x velocity , index 1: y velocity
        self.velocity = [randint(1, 5), randint(1, 5)]

        self.choice = choice(["up", "down", "left", "right"])

    # TODO implement attack
    def attack():
        pass

    def random_move(self):
        match self.choice:
            case "up":
                self.y_pos -= self.velocity[1]
            case "down":
                self.y_pos += self.velocity[1]
            case "left":
                self.x_pos -= self.velocity[0]
            case "right":
                self.x_pos += self.velocity[0]

        self.update_position(self.x_pos, self.y_pos)

        # reversing velocity if enemy position will go off screen
        if self.x_pos < 0 or self.x_pos > self.screen.get_width() - self.w:
            self.velocity[0] *= -1
        if self.y_pos < 0 or self.y_pos > self.screen.get_height() - self.h:
            self.velocity[1] *= -1

        pygame.display.flip()

        return

    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)
        pygame.display.flip()

        return
