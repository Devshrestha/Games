import pygame
import random
#pylint: disable=no-member

class low():

    def __init__(self):
        self.img=pygame.image.load('resorces/simple.png')

    def get_pattern(self,number):
        pass

    def spawn_wave(self):
        self.no = random.randint(5,9)
        self.get_pattern(self.no)