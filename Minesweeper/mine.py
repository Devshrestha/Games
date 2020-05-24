import random


class mines:

    def __init__(self):
        self.hi = 10
        self.wi = 10
        self.no_mine = 10
        self.grid = [[" " for i in range(self.wi)] for j in range(self.hi)]

        self.generate_mine()

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
            self.grid[self.taken_place[i][0]][self.taken_place[i][1]] = 'x'

    def print_grid(self):
        for i in range(self.wi):
            print('\n')
            for j in range(self.hi):
                print(self.grid[i][j], end=' | ')


if __name__ == "__main__":
    a = mines()
    a.print_grid()
