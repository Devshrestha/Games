import pygame


#pylint: disable=no-member

# variable used
display_height = 630
display_width = 600

# initialising
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mine Sweeper')
clock = pygame.time.Clock()


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)


game_loop()
