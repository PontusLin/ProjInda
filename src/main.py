import pygame
from sys import exit
import random

# variables
(width, height) = (1200, 800)
background_color = (100,100,200)


# main class
def main():
    # initialize pygame
    pygame.init()
    
    # create basic screen
    font = pygame.font.Font(None, 40)
    screen = pygame.display.set_mode((width, height))
    surf_background = pygame.Surface(screen.get_size())
    #surf_welcome = font.render('Welcome to TANKS!',False, 'Green')
    surf_playertank = pygame.image.load('assets/playertank.png').convert_alpha()
    rect_playertank = surf_playertank.get_rect(midbottom = (200, 300))
    
    surf_enemytank = pygame.image.load('assets/enemytank.png').convert_alpha()
    rect_enemytank = surf_enemytank.get_rect(midbottom = (1000, 300))
    
    pygame.display.set_caption('Tanks')
    
    
    # create clock object to ensure good fps
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_RIGHT]:
            pass
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        # draw screen 
        screen.blit(surf_background, (0,0))
        screen.fill(background_color)
        #screen.blit(surf_welcome, (100, 50))
        screen.blit(surf_playertank, rect_playertank)
        screen.blit(surf_enemytank, rect_enemytank)
        
        # update display every iteration
        pygame.display.update()
        
        # maximum of 60 fps
        clock.tick(60)
            
main()
    
    
    