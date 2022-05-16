import pygame

# Lives are static and their only function is to be displayed in the top of the screen for each player
class lives(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos, screen, assetpicture):
        super().__init__()
        self.screen = screen
        self.xPos = xpos
        self.yPos = ypos
        self.image = pygame.image.load(assetpicture).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.xPos, self.yPos))
        