import pygame
from mine import mines


#pylint: disable=no-member

# variable used
display_height = 780
display_width = 750
# initialising
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mine Sweeper')
clock = pygame.time.Clock()


def draw_grid():
    for i in range(values.wi):
        for j in range(values.hi):
            if values.grid_show[i][j] == 1:
                if values.grid[i][j] == 0:
                    gameDisplay.blit(values.empty, (i*50, j*50))
                elif values.grid[i][j] == 1:
                    gameDisplay.blit(values.one, (i*50, j*50))
                elif values.grid[i][j] == 2:
                    gameDisplay.blit(values.two, (i*50, j*50))
                elif values.grid[i][j] == 3:
                    gameDisplay.blit(values.three, (i*50, j*50))
                elif values.grid[i][j] == 4:
                    gameDisplay.blit(values.four, (i*50, j*50))
                elif values.grid[i][j] == 5:
                    gameDisplay.blit(values.five, (i*50, j*50))
                elif values.grid[i][j] == 6:
                    gameDisplay.blit(values.six, (i*50, j*50))
                elif values.grid[i][j] == 7:
                    gameDisplay.blit(values.seven, (i*50, j*50))
                elif values.grid[i][j] == 8:
                    gameDisplay.blit(values.eight, (i*50, j*50))
                elif values.grid[i][j] > 8:
                    gameDisplay.blit(values.bomb, (i*50, j*50))
            elif values.grid_show[i][j] == 0:
                gameDisplay.blit(values.hidden, (i*50, j*50))
            elif values.grid_show[i][j] == 2:
                gameDisplay.blit(values.flag, (i*50, j*50))


def reveal_right(i, j, stage):
    if j < 10:
        pass
    else:
        return


def mouse_press(side):
    loc = pygame.mouse.get_pos()
    x = loc[0]//50
    y = loc[1]//50
    if side == 1:
        if values.grid_show[x][y] == 0:
            values.grid_show[x][y] = 1
            reveal_right(i, j, 1)
    if side == 3:

        if values.grid_show[x][y] == 0:
            if values.no_flag > 0:
                values.grid_show[x][y] = 2
                values.no_flag -= 1
        elif values.grid_show[x][y] == 2:
            values.grid_show[x][y] = 0
            values.no_flag += 1
    return


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press(event.button)

        draw_grid()
        pygame.display.update()
        clock.tick(60)


values = mines()

game_loop()
