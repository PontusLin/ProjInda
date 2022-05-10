import pygame
import math
from turtle import speed
#a class for the tank in pygame


class tank(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, screen, assetPicture, obstacle_group):
        super().__init__()
        self.screen = screen
        self.xPos = xpos
        self.yPos = ypos
        self.obstacle_group = obstacle_group
        
        self.velocity = 0
        self.health = 3
        
        self.angle = 0;
        self.rotAngle = 0;
        
        self.og_image = pygame.image.load(assetPicture).convert_alpha()
        self.image = self.og_image
        self.rect = self.image.get_rect(midbottom=(self.xPos, self.yPos))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move(1)
        if keys[pygame.K_DOWN]:
            self.move(-1)
        if keys[pygame.K_LEFT]:
            self.rotAngle = 2
            self.rotate()
        if keys[pygame.K_RIGHT]:
            self.rotAngle = -2
            self.rotate()

    # Moves the player in the specified direction.
    def move(self, offset):
        
        self.moveX(offset)
        self.moveY(offset)

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
    def moveX(self, offset):
        # creates a copy of the player rect and moves it to where the player will
        # move. Then checks if they will collide. if not -> move the player there
        speed = 2
        
        copy_of_rect = pygame.Rect.copy(self.rect)
        copy_of_rect.x += offset*speed*math.cos(math.radians(-self.angle))
        for obstacle_sprite in self.obstacle_group:
            if(obstacle_sprite.rect.colliderect(copy_of_rect)):
                print('collision')
                return
        else:
            self.rect.x += offset*speed*math.cos(math.radians(-self.angle))
    
    # exactly the same as moveX, but for the Y composant.
    def moveY(self, offset):
        speed = 2
        copy_of_rect = pygame.Rect.copy(self.rect)
        copy_of_rect.y += offset*speed*math.sin(math.radians(-self.angle))
        for obstacle_sprite in self.obstacle_group:
            if(obstacle_sprite.rect.colliderect(copy_of_rect)):
                print('collision')
                return
        else:
            self.rect.y += offset*speed*math.sin(math.radians(-self.angle))
    
    def shoot(self):
        pass
    
     # Rotate the tank as the rotate angle field is
    def rotate(self):
        self.image = pygame.transform.rotate(self.og_image, self.angle)
        self.angle += self.rotAngle;
        self.angle = self.angle % 360;
        if self.angle < 0:
            self.angle += 360
        self.rect = self.image.get_rect(center = self.rect.center)
        
    
    
    

    
        
        
        
        