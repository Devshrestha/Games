import pygame
import random
#pylint: disable=no-member


class med:

    def __init__(self):
        self.img = pygame.image.load('resorces/medium.png')
        self.display_width = 600
        self.display_height = 700
        self.img_width = 70
        self.img_height = 80
        self.health = 60
        self.x_position = []
        self.spawn_pattern()

    def spawn_pattern(self):
        self.no = random.randint(2, 3)
        x = random.choice([80, 100, 120])
        self.y_position = random.choice([50, 100, 150])
        if self.no == 2:
            a1 = x
            a2 = self.display_width - x-self.img_width
            self.x_position.append(a1)
            self.x_position.append(a2)

        elif self.no == 3:
            a1 = 265
            a2 = x
            a3 = self.display_width - x-self.img_width
            self.x_position.append(a1)
            self.x_position.append(a2)
            self.x_position.append(a3)
