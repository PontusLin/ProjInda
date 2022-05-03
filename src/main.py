import pygame
from sys import exit
from tank import tank

# variables
(width, height) = (1200, 800)

# main class


def main():
    # initialize pygame
    pygame.init()

    # create basic screen
    font = pygame.font.Font(None, 40)
    screen = pygame.display.set_mode((width, height))
    surf_background = pygame.image.load('assets/background.png').convert_alpha()
    pygame.display.set_caption('Tanks')

    surf_obstacle = pygame.image.load('assets/obstacle.png').convert_alpha()
    rect_obstacle1 = surf_obstacle.get_rect(topleft=(100, 1))

    # make 1 single group per playerTank
    playerTank_1 = pygame.sprite.GroupSingle()
    playerTank_1.add(tank(75, 535, screen, 'assets/playertank.png'))

    # create clock object to ensure good fps
    clock = pygame.time.Clock()

    running = True
    # main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()

        # draw screen
        screen.blit(surf_background, (0, 0))

        # blit obstacle (will be sprite later)
        screen.blit(surf_obstacle, rect_obstacle1)

        # update and draw the player tanks
        playerTank_1.draw(screen)
        playerTank_1.update()

        # update display every iteration
        pygame.display.update()

        # maximum of 60 fps
        clock.tick(60)

main()