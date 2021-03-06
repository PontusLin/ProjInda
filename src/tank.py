import pygame
import math
from pygame import mixer
from Bullet import Bullet
from turtle import speed

"""
    This class represents the tank in the Tank game. A tank is controlled by the player
    and can shoot, rotate and travel in the direction it is facing.
    A tank can also shoot(with a certain cooldown). When a tank is hit by an enemy's bullet,
    its lives are decremented by 1.

    The tanks' bullets are stored in a sprite group, in the tank class.
    This sprite group is accessed by the main method via a get method.
"""


class Tank(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, screen, assetPicture, obstacle_group, angle):
        super().__init__()
        self.screen = screen
        self.xPos = xpos
        self.yPos = ypos
        
        # sprite groups. Obstacles are used to 
        # handle collisions in the moveX and moveY functions
        self.obstacle_group = obstacle_group
        self.bullet_group = pygame.sprite.Group()

        # fields related to shooting and movement
        self.cooldown_tracker = 0
        self.velocity = 2.5
        self.angle = angle
        self.rotAngle = 0
        self.health = 3
        # image and rects
        self.og_image = pygame.image.load(assetPicture).convert_alpha()
        self.image = self.og_image
        self.rect = self.image.get_rect(midbottom=(self.xPos, self.yPos))
        self.rotate(angle)     
        # sounds
        self.shoot_sound = mixer.Sound('assets/shoot.wav')

    # Moves the player in the specified direction.
    def move(self, offset):

        self.moveX(offset)
        self.moveY(offset)

        # if player goes outside the screen,
        # have the player re appear on the other side
        if self.rect.x > 1230:
            self.rect.x = -30
        if self.rect.x < -30:
            self.rect.x = 1230

    # this method moves the player in a horizontal direction
    def moveX(self, offset):
        # creates a copy of the player rect and moves it to where the player will
        # move. Then checks if they will collide. 
        # if not -> move the player there
        
        copy_of_rect = pygame.Rect.copy(self.rect)
        copy_of_rect.x += offset*self.velocity*math.cos(math.radians(-self.angle))
        # verify that the rect copy doesn't collide with any obstacle
        for obstacle_sprite in self.obstacle_group:
            if(obstacle_sprite.rect.colliderect(copy_of_rect)):
                return
        else:
            self.rect.x += offset*self.velocity*math.cos(math.radians(-self.angle))
            self.xPos += offset*self.velocity*math.cos(math.radians(-self.angle))

    # exactly the same as moveX, but for the Y composant.
    def moveY(self, offset):
        copy_of_rect = pygame.Rect.copy(self.rect)
        copy_of_rect.y += offset*self.velocity*math.sin(math.radians(-self.angle))

        if copy_of_rect.y < -20:
            return
        elif copy_of_rect.y > 720:
            return
        for obstacle_sprite in self.obstacle_group:
            if(obstacle_sprite.rect.colliderect(copy_of_rect)):
                return
        else:
            self.rect.y += offset*self.velocity*math.sin(math.radians(-self.angle))
            self.yPos = offset*self.velocity*math.sin(math.radians(-self.angle))

    # Rotate the tank as the rotate angle field is
    def rotate(self, target_rotation):

        if abs(target_rotation) < 0.2:
            return
        # check if the rotation angle you want to apply
        # will lead to a collision or not. if so: try with half the angle
        imminent_collision = self.test_rotation_for_collisions(target_rotation)
        if imminent_collision:
            self.rotate(target_rotation/2)

        else:
            self.apply_rotation(target_rotation)

    # test if rotation will lead to collision or not
    # returns true if collision occurs
    def test_rotation_for_collisions(self, target_rotation_angle):
        copys_angle = self.angle
        image_copy = pygame.transform.rotate(self.og_image, copys_angle).convert_alpha()
        copys_angle = self.angle + self.rotAngle
        copy_rect = image_copy.get_rect(center=self.rect.center)

        # tests if the fictional rect will colide with any obstacle
        for obstacle_sprite in self.obstacle_group:
            if(obstacle_sprite.rect.colliderect(copy_rect)):
                return True

    # apply rotation with the sought rotation_angle
    def apply_rotation(self, rotation_angle):
        self.image = pygame.transform.rotate(self.og_image, self.angle).convert_alpha()
        self.angle += rotation_angle

        self.angle = self.angle % 360
        if self.angle < 0:
            self.angle += 360

        self.rect = self.image.get_rect(center=self.rect.center)

    # track how long time has passed since 
    # the player called shoot last. If more than 300 ms,
    # enough time has passed -> set cooldown_tracker to 0
    def shot_tracker(self, value):
        self.cooldown_tracker += value
        if self.cooldown_tracker > 300:
            self.cooldown_tracker = 0

    # shoot adds a bullet if enough time
    # has passed since the function was called lastly
    def shoot(self):
        if self.cooldown_tracker == 0:
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.angle, self.screen)
            self.bullet_group.add(bullet)
            self.shoot_sound.play()

    # return the tanks' bullets. Used in main method 
    # to draw the bullets
    def get_bullets(self):
        return self.bullet_group

    # reduce lives if hit by enemy bullet
    def reduce_lives(self):
        self.health -= 1

    # return health remaining (used in main class for drawing them)
    def get_health(self):
        return self.health
