import pygame
from sys import exit
import random

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
    
    playerTank = tank(75, 535, screen, 'assets/playertank.png')
    
    surf_playertank = pygame.image.load('assets/playertank.png').convert_alpha()
    rect_playertank = surf_playertank.get_rect(midbottom = (75, 535))
    
    surf_enemytank = pygame.image.load('assets/enemytank.png').convert_alpha()
    rect_enemytank = surf_enemytank.get_rect(midbottom = (1000, 320))
    
    surf_obstacle = pygame.image.load('assets/obstacle.png').convert_alpha()
    rect_obstacle1 = surf_obstacle.get_rect(topleft = (100, 1))
    
    
    
    
    # create clock object to ensure good fps
    clock = pygame.time.Clock()
    
    running = True
    # main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
       
       # Handle key input
        keys = pygame.key.get_pressed()

        # Check if any keys are pressed
        if keys[pygame.K_LEFT]:
            playerTank.move(-3, 0)
        if keys[pygame.K_RIGHT]:
            playerTank.move(3, 0)
        if keys[pygame.K_UP]:
            playerTank.move(0, -3)
        if keys[pygame.K_DOWN]:
            playerTank.move(0, 3)
        
        # draw screen 
        screen.blit(surf_background, (0,0))
        playerTank.blit()
        #screen.blit(surf_playertank, rect_playertank)
        screen.blit(surf_enemytank, rect_enemytank)
        screen.blit(surf_obstacle, rect_obstacle1)
        
        
        # update display every iteration
        pygame.display.update()
        
        # maximum of 60 fps
        clock.tick(60)

main()
    
    
    