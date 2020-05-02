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
x_position=frame_count=b_count=back_counter = 0
p_bullet_x = []
p_bullet_y = []

# defining colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (10, 10, 250)
yellow = (250, 250, 10)
orange=(255,133,52)
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
    global x_position,frame_count,b_count,back_counter 
    x_position=frame_count=b_count=back_counter = 0
    player.draw_position_x=265



def hard_set():
    pass

def draw_simple_opponent():
    gameDisplay.blit(wave.img,(150,50))
    gameDisplay.blit(wave.img,(350,50))
    gameDisplay.blit(wave.img,(250,50))
def player_bullets(pos, pos_y, step):
    dis =5
    l = 10
  
    for i in range(len(pos_y)):
        pos_y[i] -= 5
        
    player.fire()
    no = player.bullet_count
    if no == 1:

        if len(pos)>16:
            for i in range(len(pos)-16,len(pos)):
                pygame.draw.line(gameDisplay, yellow,
                         (pos[i], pos_y[i] - dis), (pos[i], pos_y[i] - dis-l), 3)
        else:

            for i in range(len(pos)):
                pygame.draw.line(gameDisplay, yellow,
                         (pos[i], pos_y[i] - dis), (pos[i], pos_y[i] - dis-l), 3)

    if no ==2:
        if len(pos)>16:
            for i in range(len(pos)-16,len(pos)):
                pygame.draw.line(gameDisplay, orange,
                         (pos[i]-2, pos_y[i] - dis), (pos[i]-2, pos_y[i] - dis-l), 3)
            for i in range(len(pos)-16,len(pos)):
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
    global back_counter, x_position, p_bullet,frame_count,b_count
    
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
        draw_simple_opponent()
        if b_count % 8 == 0:
            p_bullet_x.append(
                player.draw_position_x+(player.img_width/2))
            p_bullet_y.append(600)
        player_bullets(p_bullet_x, p_bullet_y, frame_count)
        # create a background gif
        back_counter += 1
        if back_counter > 61:
            back_counter = 0

        frame_count += 1
        b_count+=1
        # collison check for player
        is_colliding()
        pygame.display.update()
        clock.tick(60)


load_background()
wave=low()
player = player_ship()
game_loop()
