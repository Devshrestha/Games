import pygame
import random
# pylint: disable=no-member


class low():

    def __init__(self):
        self.stage = [pygame.image.load('resorces/simple.png'),pygame.image.load('resorces/simple_b1.png'),pygame.image.load('resorces/simple_b2.png'),pygame.image.load('resorces/simple_b3.png')]
        self.after_end=[pygame.image.load('resorces/fire_simple.png'),pygame.image.load('resorces/smoke_simple.png')]
        self.img = self.stage[0]
        self.display_width = 600
        self.display_height = 700
        self.img_width = 60
        self.img_height = 60
        self.starfe_stage = 0
        self.strafe_value = 0
        self.blast=[]

    def strafe(self):
        if self.starfe_stage in [-1, 0, 1]:
            self.strafe_value = random.choice([-1, 1])
            if self.starfe_stage == 0:
                if self.strafe_value == 1:
                    self.starfe_stage = 1
                if self.strafe_value == -1:
                    self.starfe_stage = -1
            elif self.starfe_stage == -1:
                if self.strafe_value == -1:
                    self.starfe_stage = -2
                if self.strafe_value == 1:
                    self.starfe_stage = 0
            elif self.starfe_stage == 1:
                if self.strafe_value == -1:
                    self.starfe_stage = 0
                if self.strafe_value == 1:
                    self.starfe_stage = 2
        elif self.starfe_stage in [-2, 2]:
            if self.starfe_stage == -2:
                self.strafe_value = 2
                self.starfe_stage = 0
            if self.starfe_stage == 2:
                self.strafe_value = -2
                self.starfe_stage = 0

    def pattern_C(self):
        self.layers = (self.no//2)+1
        gap = 40
        self.head = [(self.display_width-self.img_width)/2, 30, 20]
        self.lay2_1 = [(self.display_width-self.img_width) /
                       2-(gap*2), gap*2, 20]
        self.lay2_2 = [(self.display_width-self.img_width) /
                       2+(gap*2), gap*2, 20]
        self.the_wave = [self.head, self.lay2_1, self.lay2_2]
        self.ol = [random.choice([[self.head[:2]], [[0, 1000]], [[0, 1000]]]),
                   random.choice([[self.lay2_1[:2]], [[0, 1000]], [[0, 1000]]]), random.choice([[self.lay2_2[:2]], [[0, 1000]], [[0, 1000]]])]
        if self.layers > 2:
            self.lay3_1 = [(self.display_width-self.img_width) /
                           2-(gap*4), gap*4, 20]
            self.the_wave.append(self.lay3_1)

            self.lay3_2 = [(self.display_width-self.img_width) /
                           2+(gap*4), gap*4, 20]
            self.the_wave.append(self.lay3_2)
            self.ol.append(random.choice(
                [[self.lay3_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay3_2[:2]], [[0, 1000]], [[0, 1000]]]))

        if self.layers > 3:
            self.lay4_1 = [(self.display_width-self.img_width) /
                           2-(gap*6), gap*6, 20]
            self.the_wave.append(self.lay4_1)
            self.lay4_2 = [(self.display_width-self.img_width) /
                           2+(gap*6), gap*6, 20]
            self.the_wave.append(self.lay4_2)
            self.ol.append(random.choice(
                [[self.lay4_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay4_2[:2]], [[0, 1000]], [[0, 1000]]]))

            self.ol2 = self.ol.copy()

    def pattern_T(self):
        self.layers = (self.no//2)+1
        gap = 40
        self.head = [(self.display_width-self.img_width)/2, gap*(self.no), 20]
        self.lay2_1 = [(self.display_width-self.img_width) /
                       2-(gap*2), gap*(self.no-2), 20]
        self.lay2_2 = [(self.display_width-self.img_width) /
                       2+(gap*2), gap*(self.no-2), 20]
        self.the_wave = [self.head, self.lay2_1, self.lay2_2]
        self.ol = [random.choice([[self.head[:2]], [[0, 1000]], [[0, 1000]]]),
                   random.choice([[self.lay2_1[:2]], [[0, 1000]], [[0, 1000]]]), random.choice([[self.lay2_2[:2]], [[0, 1000]], [[0, 1000]]])]
        if self.layers > 2:
            self.lay3_1 = [(self.display_width-self.img_width) /
                           2-(gap*4), gap*(self.no-4), 20]
            self.the_wave.append(self.lay3_1)
            self.lay3_2 = [(self.display_width-self.img_width) /
                           2+(gap*4), gap*(self.no-4), 20]
            self.the_wave.append(self.lay3_2)
            self.ol.append(random.choice(
                [[self.lay3_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay3_2[:2]], [[0, 1000]], [[0, 1000]]]))
        if self.layers > 3:
            self.lay4_1 = [(self.display_width-self.img_width) /
                           2-(gap*6), gap*(self.no-6), 20]
            self.the_wave.append(self.lay4_1)
            self.lay4_2 = [(self.display_width-self.img_width) /
                           2+(gap*6), gap*(self.no-6), 20]
            self.the_wave.append(self.lay4_2)
            self.ol.append(random.choice(
                [[self.lay4_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay4_2[:2]], [[0, 1000]], [[0, 1000]]]))

        self.ol2 = self.ol.copy()

    def pattern_Z(self):
        self.layers = (self.no//2)+1
        gap = 40
        self.head = [(self.display_width-self.img_width)/2, 120, 20]
        self.lay2_1 = [(self.display_width-self.img_width) /
                       2-(gap*2), 60, 20]
        self.lay2_2 = [(self.display_width-self.img_width) /
                       2+(gap*2), 60, 20]
        self.the_wave = [self.head, self.lay2_1, self.lay2_2]
        self.ol = [random.choice([[self.head[:2]], [[0, 1000]], [[0, 1000]]]),
                   random.choice([[self.lay2_1[:2]], [[0, 1000]], [[0, 1000]]]), random.choice([[self.lay2_2[:2]], [[0, 1000]], [[0, 1000]]])]
        if self.layers > 2:
            self.lay3_1 = [(self.display_width-self.img_width) /
                           2-(gap*4), 120, 20]
            self.the_wave.append(self.lay3_1)
            self.lay3_2 = [(self.display_width-self.img_width) /
                           2+(gap*4), 120, 20]
            self.the_wave.append(self.lay3_2)
            self.ol.append(random.choice(
                [[self.lay3_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay3_2[:2]], [[0, 1000]], [[0, 1000]]]))
        if self.layers > 3:
            self.lay4_1 = [(self.display_width-self.img_width) /
                           2-(gap*6), 60, 20]
            self.lay4_2 = [(self.display_width-self.img_width) /
                           2+(gap*6), 60, 20]
            self.the_wave.append(self.lay4_1)
            self.the_wave.append(self.lay4_2)
            self.ol.append(random.choice(
                [[self.lay4_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay4_2[:2]], [[0, 1000]], [[0, 1000]]]))

        self.ol2 = self.ol.copy()

    def pattern_S(self):
        self.layers = (self.no//2)+1
        gap = 40
        self.head = [(self.display_width-self.img_width)/2, 60, 20]
        self.lay2_1 = [(self.display_width-self.img_width) /
                       2-(gap*2), 60, 20]
        self.lay2_2 = [(self.display_width-self.img_width) /
                       2+(gap*2), 60, 20]
        self.the_wave = [self.head, self.lay2_1, self.lay2_2]
        self.ol = [random.choice([[self.head[:2]], [[0, 1000]], [[0, 1000]]]),
                   random.choice([[self.lay2_1[:2]], [[0, 1000]], [[0, 1000]]]), random.choice([[self.lay2_2[:2]], [[0, 1000]], [[0, 1000]]])]
        if self.layers > 2:
            self.lay3_1 = [(self.display_width-self.img_width) /
                           2-(gap*4), 60, 20]
            self.the_wave.append(self.lay3_1)
            self.lay3_2 = [(self.display_width-self.img_width) /
                           2+(gap*4), 60, 20]
            self.the_wave.append(self.lay3_2)
            self.ol.append(random.choice(
                [[self.lay3_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay3_2[:2]], [[0, 1000]], [[0, 1000]]]))
        if self.layers > 3:
            self.lay4_1 = [(self.display_width-self.img_width) /
                           2-(gap*6), 60, 20]
            self.the_wave.append(self.lay4_1)
            self.lay4_2 = [(self.display_width-self.img_width) /
                           2+(gap*6), 60, 20]
            self.the_wave.append(self.lay4_2)
            self.ol.append(random.choice(
                [[self.lay4_1[:2]], [[0, 1000]], [[0, 1000]]]))
            self.ol.append(random.choice(
                [[self.lay4_2[:2]], [[0, 1000]], [[0, 1000]]]))

        self.ol2 = self.ol.copy()

    def get_pattern(self, number):
        patt = [self.pattern_C, self.pattern_T, self.pattern_Z, self.pattern_S]
        self.pattern = random.choice(patt)
        #self.pattern = self.pattern_C
        return

    def draw_check(self):
        a = []
        temp = []
        temp2 = []
        for i in range(len(self.the_wave)):
            if self.the_wave[i][2] > 0:
                a.append(i)

        for i in range(len(self.the_wave)):
            if i in a:
                temp.append(self.the_wave[i])
                # temp2.append(self.opponent_fire_list[i])

        self.the_wave = temp
        #self.opponent_fire_list = temp2

    def wave_fire(self):
        a_list = []
        fire_num = random.randint(0, len(self.the_wave))
        for _ in range(fire_num):
            while True:
                a = random.randint(0, fire_num)
                if a not in a_list:
                    a_list.append(a)
                    break

        return a_list

    def damage_enemy(self, array, no):

        for j in range(len(array)):
            a = array[j][0]
            self.the_wave[a][2] = self.the_wave[a][2]-5*(no)
            if self.the_wave[a][2]==0:
                if self.the_wave[a] not in self.blast:
                    self.blast.append([self.the_wave[a],2,0])
          

        self.draw_check()

    def spawn_wave(self):
        self.no = random.choice([3,  5, 5, 5,  7, 7])
        self.get_pattern(self.no)

    def collision_check(self, bullet_x, bullet_y):
        dis = 5
        l = 10
        intersect = []
        for k in range(len(self.the_wave)):
            if True:  # add distroyed condition here
                a = []
                b = []

                for i in range(len(bullet_y)):
                    y = bullet_y[i]-l-dis
                    if y > self.the_wave[k][1] and y < self.the_wave[k][1]+self.img_height:
                        if i not in b:
                            b.append(i)
                for j in range(len(bullet_x)):
                    x = bullet_x[j]
                    if x < self.the_wave[k][0]+self.img_width and x > self.the_wave[k][0]:
                        if j not in a:
                            a.append(j)

                for i in range(len(a)):
                    if a[i] in b and a[i] not in intersect:
                        intersect.append([k, a[i]])
                for i in range(len(b)):
                    if b[i] in a and b[i] not in intersect:
                        intersect.append([k, b[i]])

        return intersect


if __name__ == "__main__":

    a = low()
    a.spawn_wave()
    a.pattern()
    print(a.no, a.head)
