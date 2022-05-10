import pygame
from sys import exit

from tank import Tank
from obstacle import obstacle


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

    # surf_obstacle = pygame.image.load('assets/obstacle.png').convert_alpha()
    # rect_obstacle1 = surf_obstacle.get_rect(topleft=(100, 1))

    # make a group with all obstacles. xpos and ypos will be topleft 
    # location of rect
    obstacles = pygame.sprite.Group()
    obstacles.add(obstacle(100, 1, screen, 'assets/obstacle.png'))

    # make 1 single group per playerTank
    playerTank_1 = pygame.sprite.GroupSingle()
    playerTank_1.add(Tank(75, 535, screen, 'assets/playertank.png', obstacles, 0))
    
    playerTank_2 = pygame.sprite.GroupSingle()
    playerTank_2.add(Tank(1125, 535, screen, 'assets/enemytank.png', obstacles, 0))

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
        # screen.blit(surf_obstacle, rect_obstacle1)

        # update and draw the player tanks
        playerTank_1.draw(screen)
        playerTank_1.update(1)
        
        playerTank_2.draw(screen)
        playerTank_2.update(2)

        # draw all the obstacles
        obstacles.draw(screen)

        # update display every iteration
        pygame.display.update()

        # maximum of 60 fps
        clock.tick(60)


main()
