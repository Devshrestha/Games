import pygame
from pygame.constants import *
import random
import time

pygame.font.init()
# variable used
display_width = 600
display_height = 640
lvl = [0.1, 0.06, 0.05, 0.04, 0.02]
prev_body = []
prev_food = None
is_added = True
eaten = True
food = [None, None]
score = 0
change = (1, -1)
food_counter = 0
special_draw = False
body = [[30, 55]]
l = 1
fre = 10
glow = 0
selected = 1
#pylint: disable=no-member

# colors
white = (255, 255, 255)
back = (10, 10, 25)
red = (200, 10, 10)
green = (10, 200, 10)
black = (10, 10, 10)
dark_grey = (77, 77, 77)
grey = (102, 102, 102)
light_grey = (128, 128, 128)
yellow = (255, 255, 0)
grey_green = (136, 221, 136)
active_green = (70, 240, 70)
grey_red = (203, 77, 77)
active_red = (230, 25, 25)
dark_yellow = (179, 179, 77)
# special colors
sel_color1 = (128, 128, 128)
sel_color2 = (128, 128, 128)
sel_color3 = (128, 128, 128)
sel_color4 = (128, 128, 128)
# initailising pygame display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# functions


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


def score_display():
    global score, body, food_counter

    pygame.draw.rect(gameDisplay, white, (0, 610, display_width, 30))
    message_display("Score:", 0, 600, 90, 50, 30)
    message_display(str(score), 0, 600, 200, 50, 30)


def redefine():
    global body, change, eaten, food, food_counter, score
    body = [[30, 55]]
    change = (1, -1)
    eaten = True
    food = [None, None]
    food_counter = 0
    score = 0


def lvl_assign(x):
    global l, fre, sel_color1, sel_color2, sel_color3, sel_color4
    l = x
    fre = 14-((x+1)*2)
    if x == 0:
        sel_color1 = (249, 249, 184)
        sel_color2 = (128, 128, 128)
        sel_color3 = (128, 128, 128)
        sel_color4 = (128, 128, 128)
    elif x == 1:
        sel_color2 = (249, 249, 184)
        sel_color1 = (128, 128, 128)
        sel_color3 = (128, 128, 128)
        sel_color4 = (128, 128, 128)
    elif x == 2:
        sel_color3 = (249, 249, 184)
        sel_color2 = (128, 128, 128)
        sel_color1 = (128, 128, 128)
        sel_color4 = (128, 128, 128)
    elif x == 3:
        sel_color4 = (249, 249, 184)
        sel_color2 = (128, 128, 128)
        sel_color3 = (128, 128, 128)
        sel_color1 = (128, 128, 128)


def collison_check(parts):
    mid_head = (parts[0][0])*5, (parts[0][1])*5
    mid_parts = []
    # border collison check
    # vertically off limits
    if mid_head[0] < 0:
        time.sleep(1.5)
        redefine()
    elif mid_head[0] == 300:
        time.sleep(1.5)
        redefine()
    # horizontally off limits
    if mid_head[1] < 0:
        time.sleep(1.5)
        redefine()
    elif mid_head[1] > 300:
        time.sleep(1.5)
        redefine()

    # body collison
    for i in range(len(parts)):
        mid_parts.append(None)
        mid_parts[i] = (parts[i][0])*5, (parts[i][1])*5
    for i in range(1, len(parts)):
        if mid_parts[i] == mid_head:
            time.sleep(1.5)
            redefine()


def quiting():
    pygame.quit()
    quit()


def square(snake):
    head = snake[0]
    snake_queue = snake[1:]
    size = 10
    pygame.draw.rect(gameDisplay, green,
                     pygame.Rect((head[0]*size, head[1]*size), (size, size)))

    for i in range(len(snake_queue)):
        pygame.draw.rect(gameDisplay, white,
                         ((snake_queue[i][0]*size)+1, (snake_queue[i][1]*size)+1, size-2, size-2))


def is_eaten(body):
    global eaten, food, is_added, prev_food, special_draw, food_counter, score
    s = 5
    mid_food = (food[0])*s, (food[1])*s
    mid_head = (body[0][0])*s, (body[0][1])*s

    if mid_head == mid_food:
        prev_food = mid_head
        is_added = False
        eaten = True
        sp = food_counter//fre
        score = ((food_counter-sp)*(l+1)+(sp*10))
        if special_draw:
            special_draw = False


def food_draw():
    global eaten, body, food, food_counter, special_draw, glow
    size = 10
    glow += 1
    if eaten:
        while True:
            food[0] = random.randint(0, 58)
            food[1] = random.randint(0, 58)
            if food not in body:
                food_counter += 1
                break
        eaten = False
    if food_counter % fre == 0:
        if glow % 5 == 0:
            pygame.draw.circle(gameDisplay, yellow,
                               ((food[0]*10)+5, (food[1]*10)+5), size//2)
        else:
            pygame.draw.circle(gameDisplay, dark_yellow,
                               ((food[0]*10)+5, (food[1]*10)+5), size//2)
        special_draw = True

    else:
        pygame.draw.circle(gameDisplay, red,
                           ((food[0]*10)+5, (food[1]*10)+5), size//2)


def button(msg, x, y, w, h, ic, ac, pc, size, action, val=None, fg=black):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0]:
            pygame.draw.rect(gameDisplay, pc, (x, y, w, h))
            if action == lvl_assign:
                action(val)
            else:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("arial.ttf", size)
    textSurf, textRect = text_objects(msg, smallText, fg)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def change_angle(head, cor, direction):
    head[cor] = head[cor]+(direction)

    return head.copy()


def pause_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break

        gameDisplay.fill(back)
        message_font = pygame.font.SysFont('Alef.ttf', 100)
        TextSurf, TextRect = text_objects('Pause Menu', message_font, white)
        TextRect.center = ((display_width/2), (display_height*(1/3)))
        gameDisplay.blit(TextSurf, TextRect)

        button('Main menu', 200, 350, 200, 50, sel_color3,
               grey, dark_grey, 25, game_intro)

        button('Resume', 150, 550, 100, 50, grey_green,
               active_green, dark_grey, 25, game_loop)

        button('Exit', 350, 550, 100, 50, grey_red,
               active_red, dark_grey, 25, quiting)

        pygame.display.update()


def game_intro():
    redefine()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break
        gameDisplay.fill(back)
        message_font = pygame.font.SysFont('Alef.ttf', 115)
        TextSurf, TextRect = text_objects('Snake Game', message_font, white)
        TextRect.center = ((display_width/2), (display_height*(1/3)))
        gameDisplay.blit(TextSurf, TextRect)

        # button(msg,x,y,w,h,ic,ac)
        message_display('Choose lvl:', 40, 400, 50, 50, 30, white)
        button('Easy', 40, 450, 100, 50, sel_color1,
               grey, dark_grey, 25, lvl_assign, 0)
        button('Medium', 180, 450, 100, 50, sel_color2,
               grey, dark_grey, 25, lvl_assign, 1)
        button('Hard', 320, 450, 100, 50, sel_color3,
               grey, dark_grey, 25, lvl_assign, 2)
        button('Expert', 460, 450, 100, 50, sel_color4,
               grey, dark_grey, 25, lvl_assign, 3)
        button('Start', 150, 550, 100, 50, grey_green,
               active_green, dark_grey, 25, game_loop)
        button('Exit', 350, 550, 100, 50, grey_red,
               active_red, dark_grey, 25, quiting)

        pygame.display.update()


def game_loop():
    global body, prev_body, change, prev_food, is_added

    while True:
        time.sleep(lvl[l])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    pause_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if change != (0, 1):
                        change = (0, -1)
                elif event.key == pygame.K_RIGHT:
                    if change != (0, -1):
                        change = (0, 1)
                elif event.key == pygame.K_UP:
                    if change != (1, 1):
                        change = (1, -1)
                elif event.key == pygame.K_DOWN:
                    if change != (1, -1):
                        change = (1, 1)

        gameDisplay.fill(back)

        food_draw()
        prev_body = body.copy()

        body[0] = change_angle(body[0][:], change[0], change[1])
        for i in range(len(prev_body)-1):
            body[i+1] = prev_body[i][:]
        is_eaten(body)
        square(body)
        collison_check(body)
        if not is_added:
            mid_end = (body[-1][0])*5, (body[-1][1])*5
            if mid_end == prev_food:
                body.append((prev_food[0]/5, prev_food[1]/5))
                is_added = True

        score_display()
        pygame.display.update()


game_intro()
game_loop()
