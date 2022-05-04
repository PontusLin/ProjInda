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
        # first check if colliding with something
        collision_list = pygame.sprite.spritecollide(self, self.obstacle_group, False)
        
        if collision_list:
            for obstacle in collision_list:
                # blah blah
                if directionX > 0:
                    self.rect.right = obstacle.rect.left
                if directionX < 0:
                    self.rect.left = obstacle.rect.right
                if directionY > 0:
                    self.rect.bottom = obstacle.rect.top
                if directionY < 0:
                    self.rect.top = obstacle.rect.bottom
        else:
            self.rect.x += directionX
            self.rect.y += directionY
            # if player goes outside the screen,
            # have the player re appear on the other side
            if self.rect.x > 1200:
                self.rect.x = 0
            if self.rect.x < 0:
                self.rect.x = 1200

            if self.rect.y > 800:
                self.rect.y = 0
            if self.rect.y < 0:
                self.rect.y = 800

    # blit is not needed when using sprite
    def update(self):
        self.player_input()

    """
    def shoot(self):
        pass
    """
    
    
    

    
        
        
        
        