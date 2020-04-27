import pygame
import time
from gameplay import game

#pylint: disable=no-member

pygame.font.init()
# variable used
display_width = 290
display_height = 340
marker = 0
mode = 0

# declaring colors
white = (255, 255, 255)
black = (0, 0, 0)
lime = (153, 255, 153)
light_green = (159, 255, 128)
intro_back = (236, 255, 230)
green = (94, 232, 48)
# initialising pygame window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TicTacToe')
clock = pygame.time.Clock()


class functions:
    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, width_centre, height_center, size):

        message_font = pygame.font.SysFont('Alef.ttf', size)
        TextSurf, TextRect = self.text_objects(text, message_font)
        TextRect.center = ((width_centre), (height_center))
        gameDisplay.blit(TextSurf, TextRect)

    def button(self, message, x, y, hi, wi, ic, ac, pc, size, action, val=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        x = x/2
        y = y/2

        if x+wi > mouse[0] > x and y+hi > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, wi, hi))
            if click[0]:
                pygame.draw.rect(gameDisplay, pc, (x, y, wi, hi))
                action(val)
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, wi, hi))
        self.message_display(message, x+(wi/2), y+(hi/2), size)


def assign(a):
    def wait():
        gameDisplay.fill(light_green)
        pygame.display.update()
        time.sleep(1)
        game_loop()
    global marker, mode
    if a == 0:
        mode = 1
    elif a == 1:
        mode = 2
    elif a == 2:
        marker = 1
    elif a == 3:
        marker = 2
    if marker and mode:
        wait()


def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(intro_back)
        # intro text
        func.message_display("Choose mode:", 90, 50, 30)
        func.button('PVP', 95, 155, 30, 80, lime,
                    light_green, green, 20, assign, 0)
        func.button('PVC', 310, 155, 30, 80, lime,
                    light_green, green, 20, assign, 1)

        func.message_display('Palyer 1 marker:', 100, 150, 30)
        func.button('X', 95, 355, 30, 80, lime,
                    light_green, green, 20, assign, 2)
        func.button('O', 310, 355, 30, 80, lime,
                    light_green, green, 20, assign, 3)

        pygame.display.update()
        clock.tick(60)


def game_loop():
    global mode, marker
    app = game(mode, marker)
    st = 5
    cs = (display_width-(4*st))/3

    def update(a):
        if app.playing:
            if mode == 1:
                app.update(a[0], a[1])
            else:
                app.ai_update(a[0], a[1])

    def print_grid():
        # creating spaces in lines to be buttons
        val = app.grid
        for i in range(3):
            for j in range(3):
                func.button(val[j][i], (st*(i+1)+cs*i)*2, (st*(j+1)+cs*j)
                            * 2, cs, cs, white, white, white, 80, update, (j, i))

        # vertical
        pygame.draw.line(gameDisplay, (0, 0, 0),
                         (cs+st, 0), (cs+st, cs*3+st*3), st)
        pygame.draw.line(gameDisplay, (0, 0, 0),
                         (cs*2+st*3, 0), (cs*2+st*3, cs*3+st*3), st)
        # horizontal
        pygame.draw.line(gameDisplay, (0, 0, 0),
                         (0, cs+st), (cs*3+st*3, cs+st), st)
        pygame.draw.line(gameDisplay, (0, 0, 0),
                         (0, cs*2+st*3), (cs*3+st*3, cs*2+st*3), st)

    def get_status():
        msg = app.stat
        func.message_display(msg, ((display_height-200)/2), 315, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        print_grid()
        get_status()

        pygame.display.update()
        clock.tick(60)


func = functions()
game_intro()
