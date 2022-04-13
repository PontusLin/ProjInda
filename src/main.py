import pygame
from sys import exit
import random

# variables
(width, height) = (1000, 600)
background_color = (100,100,200)


# main class
def main():
    # initialize pygame
    pygame.init()
    
    # create basic screen
    font = pygame.font.Font(None, 40)
    screen = pygame.display.set_mode((width, height))
    surf_background = pygame.Surface(screen.get_size())
    surf_welcome = font.render('Welcome to TANKS!',False, 'Green')
    
    pygame.display.set_caption('Tanks')
    
    
    # create clock object to ensure good fps
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
        
        # draw screen 
        screen.blit(surf_background, (0,0))
        screen.fill(background_color)
        screen.blit(surf_welcome, (100, 50))
        
        # update display every iteration
        pygame.display.update()
        
        # maximum of 60 fps
        clock.tick(60)
        
main()
    
    
    