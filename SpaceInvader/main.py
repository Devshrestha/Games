import pygame
import time
import random
from player import player_ship
from simple_opponent import low


# variable used
display_width = 600
display_height = 700
jet_width = 70
jet_height = 80
back = [None]*62
x_position = frame_count = b_count = back_counter = 0
p_bullet_x = []
p_bullet_y = []
game_rate = 30
a = 0
# defining colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (10, 10, 250)
yellow = (250, 250, 10)
orange = (255, 133, 52)
red = (240, 10, 10)
# initializing
# pylint: disable=no-member
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Spacce Invader 2150')
clock = pygame.time.Clock()


# loading images
def load_background():
    global back
    for i in range(len(back)):
        image_name = "resorces//"+str(i)+'.gif'
        back[i] = pygame.image.load(image_name)

# function defined


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text, locx, locy, w, h, size, color=black):
    x = locx+w/2
    y = locy+h/2

    message_font = pygame.font.SysFont('Alef.ttf', size)
    TextSurf, TextRect = text_objects(text, message_font, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


def soft_set():
    global x_position, frame_count, b_count, back_counter
    x_position = frame_count = b_count = back_counter = 0
    player.draw_position_x = 265


def hard_set():
    pass


def opponet_fire(fire_list, object):
    global a
    h = object.img_height
    # add new bullet to randomly to random no of enemy
    if frame_count % 30 == 0:
        for i in range(len(object.the_wave)):
            if i in fire_list:
                object.ol[i].append(object.the_wave[i][:2])
                object.ol[i].append(object.the_wave[i][:2])

    # display enemy left and right bullet
    for i in range(len(object.the_wave)):
        # for left side
        for j in range(len(object.ol[i])):
            if object.ol[i][j][1] < 1000:
                pygame.draw.line(gameDisplay, red,
                                 (object.ol[i][j][0], object.ol[i][j][1]+h), (object.ol[i][j][0], object.ol[i][j][1]+5+h), 3)
        # for right side
        for j in range(len(object.ol2[i])):
            if object.ol2[i][j][1] < 1000:
                pygame.draw.line(gameDisplay, red,
                                 (object.ol2[i][j][0]+h, object.ol2[i][j][1]+h), (object.ol2[i][j][0]+h, object.ol2[i][j][1]+5+h), 3)
    # collision check of enemy bullets with player
    for i in range(len(object.the_wave)):
        for j in range(len(object.ol[i])):
            if object.ol[i][j][1] < 1000:
                if object.ol[i][j][1] < player.draw_position_y+player.img_height and object.ol[i][j][1] >= player.draw_position_y:
                    if object.ol[i][j][0] < player.draw_position_x+player.img_width and object.ol[i][j][0] >= player.draw_position_x:
                        player.health -= 5
                        object.ol[i][j][1] = 1100

                    if object.ol2[i][j][0]+object.img_width < player.draw_position_x+player.img_width and object.ol2[i][j][0]+object.img_width >= player.draw_position_x:
                        player.health -= 5
                        object.ol2[i][j][1] = 1100

    # update the position of bullet with every frame
    for i in range(len(object.the_wave)):
        for j in range(len(object.ol[i])):
            object.ol[i][j][1] = object.ol[i][j][1]+5


def draw_simple_opponent(object):
    global p_bullet_y
    temp = []
    o_fire = []
    for i in range(len(object.the_wave)):
        if object.the_wave[i][2] > 0:
            gameDisplay.blit(
                object.img, (object.the_wave[i][0], object.the_wave[i][1]))

    if frame_count % 12 == 0:
        object.strafe()
    for i in range(len(object.the_wave)):
        object.the_wave[i][0] = object.the_wave[i][0]+object.strafe_value

    damage = object.collision_check(p_bullet_x, p_bullet_y)
    for i in damage:
        if i not in temp:
            temp.append(i)
    object.damage_enemy(temp, player.bullet_count)
    for i in range(len(temp)):
        a = temp[i][1]
        p_bullet_y[a] = -100
    if frame_count % int(1.5*game_rate) == 0:
        o_fire = object.wave_fire()

    opponet_fire(o_fire.copy(), object)


def player_bullets(pos, pos_y, step):
    dis = 5  # if changed must also tweek in simple_opponnent collision()
    l = 10

    for i in range(len(pos_y)):
        pos_y[i] -= 5

    player.fire()
    no = player.bullet_count
    if no == 1:

        if len(pos) > 16:

            for i in range(len(pos)-16, len(pos)):
                pygame.draw.line(gameDisplay, yellow,
                                 (pos[i], pos_y[i] - dis), (pos[i], pos_y[i] - dis-l), 3)

        else:

            for i in range(len(pos)):
                pygame.draw.line(gameDisplay, yellow,
                                 (pos[i], pos_y[i] - dis), (pos[i], pos_y[i] - dis-l), 3)

    if no == 2:
        if len(pos) > 16:
            for i in range(len(pos)-16, len(pos)):
                pygame.draw.line(gameDisplay, orange,
                                 (pos[i]-2, pos_y[i] - dis), (pos[i]-2, pos_y[i] - dis-l), 3)
            for i in range(len(pos)-16, len(pos)):
                pygame.draw.line(gameDisplay, orange,
                                 (pos[i]+2, pos_y[i] - dis), (pos[i]+2, pos_y[i] - dis-l), 3)
        else:

            for i in range(len(pos)):
                pygame.draw.line(gameDisplay, orange,
                                 (pos[i]-2, pos_y[i] - dis), (pos[i]-2, pos_y[i] - dis-l), 3)
            for i in range(len(pos)):
                pygame.draw.line(gameDisplay, orange,
                                 (pos[i]+2, pos_y[i] - dis), (pos[i]+2, pos_y[i] - dis-l), 3)


def is_colliding():
    collison = False
    if player.draw_position_x < 0:
        collison = True
    if player.draw_position_x > (display_width-player.img_width):
        collison = True

    if collison:
        if player.lives < 0:
            hard_set()
        else:
            player.lives -= 1
            soft_set()


def game_loop():
    global back_counter, x_position, p_bullet, frame_count, b_count

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_position = -5
                if event.key == pygame.K_RIGHT:
                    x_position = 5
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    x_position = 0
        # player side strafe
        player.draw_position_x = player.draw_position_x+x_position

        gameDisplay.blit(back[back_counter], (0, 0))
        gameDisplay.blit(player.player_img,
                         (player.draw_position_x, player.draw_position_y))

        draw_simple_opponent(wave)
        if b_count % (1*game_rate) == 0:
            p_bullet_x.append(
                player.draw_position_x+(player.img_width/2))
            p_bullet_y.append(600)

        player_bullets(p_bullet_x, p_bullet_y, frame_count)
        # create a background gif
        back_counter += 1
        if back_counter > 61:
            back_counter = 0
        frame_count += 1
        b_count += 1
        # collison check for player
        is_colliding()
        pygame.display.update()
        clock.tick(60)


load_background()
wave = low()
wave.spawn_wave()
wave.pattern()
player = player_ship()
game_loop()
