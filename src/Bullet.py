import pygame
import math

"""
    This class represents the bullets in the Tank game. A bullet is shot by 
    a player tank. It spawns at the tank's center's coordinates and travels in the
    direction the tank is facing. 

    When a bullet exits the screen, it is destroyed using the destroy() function.
"""


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

    # if bullet exits screen, stop rendering it
    def destroy(self):
        if self.rect.x <= -100 or self.rect.x > 1300:
            self.kill()
        if self.rect.y <= -100 or self.rect.y > 900:
            self.kill()
        if self.speed < 5:
            self.kill()

    # if a bullet collides with a wall, have it bounce
    # a bouncing bullet changes direction and slows down a bit
    def bounce(self):
        self.speed = self.speed * 0.8
        self.direction = self.direction * (-1)
