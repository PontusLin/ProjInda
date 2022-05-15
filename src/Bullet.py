import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, direction, screen):
        super().__init__()
        # location and direction
        self.x_pos = xpos
        self.y_pos = ypos
        self.screen = screen
        self.speed = 10
        self.direction = direction
    
        # image and rect
        self.og_image = pygame.image.load('assets/redBulletSmaller.png').convert_alpha()
        self.image = pygame.transform.rotate(self.og_image, self.direction).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x_pos + 55*math.cos(math.radians(-direction)), self.y_pos + 55*math.sin(math.radians(-direction))))
 
    def update(self):
        self.rect.y += self.speed*math.sin(math.radians(-self.direction))
        self.rect.x += self.speed*math.cos(math.radians(-self.direction))
        self.destroy()
    
    def get_player(self):
        return self.player_number

    # if bullet exits screen, stop rendering it
    def destroy(self):
        if self.rect.x <= -100 or self.rect.x > 1300:
            self.kill()
        if self.rect.y <= -100 or self.rect.y > 900:
            self.kill()
