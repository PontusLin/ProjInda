import pygame
import math
#a class for the tank in pygame


class tank(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, screen, assetPicture, obstacle_group):
        super().__init__()
        self.screen = screen
        self.xPos = xpos
        self.obstacle_group = obstacle_group
        self.yPos = ypos
        self.velocity = 0
        self.health = 3
        self.image = pygame.image.load(assetPicture).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.xPos, self.yPos))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move(0, -3)
        if keys[pygame.K_DOWN]:
            self.move(0, 3)
        if keys[pygame.K_LEFT]:
            self.move(-3, 0)
        if keys[pygame.K_RIGHT]:
            self.move(3, 0)

    # Moves the player in the specified direction.
    def move(self, directionX, directionY):
        
        self.moveX(directionX)
        self.moveY(directionY)

        #collision_list = pygame.sprite.spritecollide(self, self.obstacle_group, False)
        # if player goes outside the screen,
        # have the player re appear on the other side
        if self.rect.x > 1230:
            self.rect.x = -30
        if self.rect.x < -30:
            self.rect.x = 1230

        if self.rect.y > 830:
            self.rect.y = -30
        if self.rect.y < -30:
            self.rect.y = 830

    # blit is not needed when using sprite
    def update(self):
        self.player_input()

    # this method moves the player in a horizontal direction
    def moveX(self, horizontal_speed):
        # creates a copy of the player rect and moves it to where the player will
        # move. Then checks if they will collide. if not -> move the player there
        copy_of_rect = pygame.Rect.copy(self.rect)
        copy_of_rect.x += horizontal_speed
        for obstacle_sprite in self.obstacle_group:
            if(obstacle_sprite.rect.colliderect(copy_of_rect)):
                print('collision')
                return
        else:
            self.rect.x += horizontal_speed
    
    # exactly the same as moveX, but for the Y composant.
    def moveY(self, vertical_speed):
        copy_of_rect = pygame.Rect.copy(self.rect)
        copy_of_rect.y += vertical_speed
        for obstacle_sprite in self.obstacle_group:
            if(obstacle_sprite.rect.colliderect(copy_of_rect)):
                print('collision')
                return
        else:
            self.rect.y += vertical_speed
    """
    def shoot(self):
        pass
    """
    
    
    

    
        
        
        
        