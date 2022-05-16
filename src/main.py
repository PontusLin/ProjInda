import pygame
from sys import exit

from tank import Tank
from obstacle import Obstacle


# variables
(width, height) = (1200, 800)

# Help function to create text objects, that will say the surface and the associated rectangle
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


# Startscreen
def startScreen(screen, clock):
    
    # create basic fonts
    largeText = pygame.font.Font('freesansbold.ttf',115)
    smallText = pygame.font.Font('freesansbold.ttf', 50)
    
    # create text element 'TANKS!'
    TextSurf, TextRect = text_objects("TANKS!", largeText)
    TextRect.center = (width/2, height/4)
    
    # Create 'buttons'
    button_play_surf, button_play_rect = text_objects("Play", smallText)
    button_play_rect.center = (width/2, height/2)
    
    button_quit_surf, button_quit_rect = text_objects("Quit", smallText)
    button_quit_rect.center = (width/2, height/1.5)
    
    # Create assets to blit on screen
    surf_tank1 = pygame.image.load('assets/playertank.png').convert_alpha()
    rect_tank1 = surf_tank1.get_rect(center=(200, 700))
    
    surf_tank2 = pygame.image.load('assets/enemytank.png').convert_alpha()
    rect_tank2 = surf_tank2.get_rect(center=(1000, 700))
    
    surf_bullet = pygame.image.load('assets/redBulletSmaller.png').convert_alpha()
    rect_bullet1 = surf_bullet.get_rect(center = (270, 700))
    rect_bullet2 = surf_bullet.get_rect(center = (300, 700))
    rect_bullet3 = surf_bullet.get_rect(center = (330, 700))
    
    # backgroundcolor white for now
    background_color = (255, 255, 255)
    
    # Loop until play- or quit button is clicked
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            # create mouse object
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the mouse, when clicked is inside the play or quit rectangle, do an operation
                if button_play_rect.topleft[0] -5 <= mouse[0] <= button_play_rect.topright[0] + 5 and button_play_rect.topleft[1] - 5 <= mouse[1] <= button_play_rect.bottomleft[1] + 5:
                    intro = False
                if button_quit_rect.topleft[0] -5 <= mouse[0] <= button_quit_rect.topright[0] + 5 and button_quit_rect.topleft[1] - 5 <= mouse[1] <= button_quit_rect.bottomleft[1] + 5:
                    pygame.QUIT()
                    exit()
                    
                    
        # Draw everything onto the screen
        screen.fill(background_color)
        screen.blit(TextSurf, TextRect)
        screen.blit(button_play_surf, button_play_rect)
        screen.blit(button_quit_surf, button_quit_rect)
        screen.blit(surf_tank1, rect_tank1)
        screen.blit(surf_tank2, rect_tank2)
        screen.blit(surf_bullet, rect_bullet1)
        screen.blit(surf_bullet, rect_bullet2)
        screen.blit(surf_bullet, rect_bullet3)
        
        pygame.display.update()
        clock.tick(60)

# main class
def main():
    # initialize pygame
    pygame.init()

    # create basic screen
    screen = pygame.display.set_mode((width, height))
    surf_background = pygame.image.load('assets/background.png').convert_alpha()
    pygame.display.set_caption('Tanks')


    # make a group with all obstacles. xpos and ypos will be topleft 
    # location of rect
    obstacles = pygame.sprite.Group()
    obstacles.add(Obstacle(100, 1, screen, 'assets/obstacle.png'))
         

    # create player tanks and each to their own single sprite group
    player_1 = Tank(75, 535, screen, 'assets/playertank.png', obstacles, 0)
    playerTank_1 = pygame.sprite.GroupSingle()
    playerTank_1.add(player_1)
    
    player_2 = Tank(1125, 535, screen, 'assets/enemytank.png', obstacles, 0)
    playerTank_2 = pygame.sprite.GroupSingle()
    playerTank_2.add(player_2)

    
    # create clock object to ensure good fps
    # Create two clocks to control rate of fire of both tanks
    clock = pygame.time.Clock()
    clock_2 = pygame.time.Clock()

    # Initialize the startscreen
    startScreen(screen, clock)
    running = True
    # main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
        
        # Handle player input. the methods called are found
        # in the tank class
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_1.move(1)
        if keys[pygame.K_DOWN]:
            player_1.move(-1)
        if keys[pygame.K_LEFT]:
            player_1.rotAngle = 2
            player_1.rotate()
        if keys[pygame.K_RIGHT]:
            player_1.rotAngle = -2
            player_1.rotate()
        # when player 1 shoots, measure the time past since
        # player 1 shot last time
        if keys[pygame.K_SPACE]:
            player_1.shot_tracker(clock.get_time())
            player_1.shoot()
        if keys[pygame.K_a]:
            player_2.rotAngle = 2
            player_2.rotate()
        if keys[pygame.K_w]:
            player_2.move(1)
        if keys[pygame.K_d]:
            player_2.rotAngle = -2
            player_2.rotate()
        if keys[pygame.K_s]:
            player_2.move(-1)
        # when player 2 shoots, measure the time past since
        # player 2 shot last time
        if keys[pygame.K_v]:
            player_2.shot_tracker(clock_2.get_time())
            player_2.shoot()
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
        
        # getthe tanks' bullets, that are stored
        # as fields in the tank objects.
        tank1_bullets = player_1.get_bullets()
        tank2_bullets = player_2.get_bullets()

        tank1_bullets.draw(screen)
        tank1_bullets.update()
        tank2_bullets = player_2.get_bullets()
        tank2_bullets.draw(screen)
        tank2_bullets.update()
        
        # if a bullet collides with an obstacle, kill it (take it away)
        pygame.sprite.groupcollide(tank1_bullets, obstacles, True, False)
        pygame.sprite.groupcollide(tank2_bullets, obstacles, True, False)

        # if a tank is hit by the opponent's bullet,
        # kill the bullet but not the tank
        tank1_hit = pygame.sprite.groupcollide(playerTank_1, tank2_bullets, False, True)
        tank2_hit = pygame.sprite.groupcollide(playerTank_2, tank1_bullets, False, True)

        # if a tank is hit, reduce the lives of the tank by 1
        if tank1_hit:
            playerTank_1.sprite.reduce_lives()

        if tank2_hit:
            playerTank_2.sprite.reduce_lives()

        # update display every iteration
        pygame.display.update()

        # maximum of 60 fps
        clock.tick(60)
        clock_2.tick(60)


main()
