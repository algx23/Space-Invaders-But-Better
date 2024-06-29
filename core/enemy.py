from core.game_object import GameObject
from random import randint


class Enemy(GameObject):
    def __init__(self, image_path, x, y, w, h, screen):
        super().__init__(image_path, screen, x, y, w, h)
        self.x_pos = x
        self.y_pos = y
        self.x_velocity = randint(1, 5)
        self.y_velocity = randint(1, 5)

        print("position: ", self.x_pos, self.y_pos)
        print("velocity: ", self.x_velocity, self.y_velocity)

    def attack():
        return

    def random_move():
        return
