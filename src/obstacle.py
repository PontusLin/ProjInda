import pygame


class Obstacle(pygame.sprite.Sprite):
    
    # create an obstacle. Obstacles are fixed and their only
    # attribute is that the player cannot travel through them
    def __init__(self, xpos, ypos, screen, assetPicture):
        super().__init__()
        self.screen = screen
        self.xPos = xpos
        self.yPos = ypos
        self.image = pygame.image.load(assetPicture).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.xPos, self.yPos))
