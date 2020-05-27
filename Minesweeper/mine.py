import random
import pygame


class mines:

    def __init__(self):
        self.hi = 15
        self.wi = 15
        self.no_mine = 15
        self.no_flag = self.no_mine
        self.grid = [[0 for i in range(self.wi)] for j in range(self.hi)]
        self.grid_show = [[0 for i in range(self.wi)] for j in range(self.hi)]
        self.load_images()
        self.generate_mine()

    def load_images(self):
        self.empty = pygame.image.load('resources/empty.png')
        self.bomb_trig = pygame.image.load('resources/bomb_tri.jpg')
        self.bomb = pygame.image.load('resources/bomb.jpg')
        self.one = pygame.image.load('resources/one.png')
        self.two = pygame.image.load('resources/two.png')
        self.three = pygame.image.load('resources/three.png')
        self.four = pygame.image.load('resources/four.png')
        self.five = pygame.image.load('resources/five.png')
        self.six = pygame.image.load('resources/six.png')
        self.seven = pygame.image.load('resources/seven.png')
        self.eight = pygame.image.load('resources/eight.png')
        self.flag = pygame.image.load('resources/flag.jpg')
        self.hidden = pygame.image.load('resources/hidden.jpg')

    def generate_mine(self):
        self.taken_place = []
        place = []
        turn = 0
        while turn < self.no_mine:
            a = random.randrange(0, self.hi*self.wi)
            if a not in place:
                place.append(a)
                self.taken_place.append([a // self.wi, a % self.wi])
                turn += 1

        for i in range(self.no_mine):
            self.grid[self.taken_place[i][0]][self.taken_place[i][1]] = 9

        self.calculate_values()

    def add(self, a, b):
        try:

            if a != 0 and b != 0:
                self.grid[a-1][b-1] += 1
        except IndexError:
            pass
        try:
            if a != 0:
                self.grid[a-1][b] += 1
        except IndexError:
            pass
        try:
            if a != 0:
                self.grid[a-1][b+1] += 1
        except IndexError:
            pass
        try:
            if b != 0:
                self.grid[a][b-1] += 1
        except IndexError:
            pass
        try:
            self.grid[a][b+1] += 1
        except IndexError:
            pass
        try:
            if b != 0:
                self.grid[a+1][b-1] += 1
        except IndexError:
            pass
        try:
            self.grid[a+1][b] += 1
        except IndexError:
            pass
        try:
            self.grid[a+1][b+1] += 1
        except IndexError:
            pass

    def calculate_values(self):
        for i in range(self.wi):
            for j in range(self.hi):
                if self.grid[i][j] > 8:
                    self.add(i, j)

    def print_grid(self):
        for i in range(self.wi):
            print('\n')
            for j in range(self.hi):
                print(self.grid[i][j], end=' | ')


if __name__ == "__main__":
    a = mines()
    a.print_grid()
