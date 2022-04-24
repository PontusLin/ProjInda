import pygame
#a class for the tank in pygame

class tank:
    def __init__(self, xpos, ypos, screen, assetPicture):
        self.screen = screen
        self.xPos = xpos
        self.yPos = ypos 
        self.velocity = 0
        self.health = 3
        self.surf_tank = pygame.image.load(assetPicture).convert_alpha()
        self.rect_tank = self.surf_tank.get_rect(midbottom = (self.xPos, self.yPos))
        
    def move(self, directionX, directionY):
        self.rect_tank.x += directionX
        self.rect_tank.y += directionY
    
    def decrementHealth(init):
        health -= 1;
        if health < 1:
            pass # Game over, You won/lose ... blablabla
    
    def blit(self):
        # draw the tank to the screen
        self.screen.blit(self.surf_tank, self.rect_tank)

    def shoot(self):
        pass
    
    
    

    
        
        
        
        