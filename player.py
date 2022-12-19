import pygame
from laser import Laser                                                 #lesson2

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint

        self.ready = True                                               #lesson2
        self.laser_time = 0                                             #lesson2
        self.laser_cooldown = 600                                       #lesson2

        self.lasers = pygame.sprite.Group()                             #lesson2
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:                         #lesson2
            self.shoot_laser()
            self.ready = False                                          #lesson2
            self.laser_time = pygame.time.get_ticks()                   #lesson2
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()                      #lesson2
            if current_time - self.laser_time >= self.laser_cooldown:   #lesson2
                self.ready = True                                       #lesson2
    def update(self):
        self.get_input()
        self.constrait()
        self.recharge()
        self.lasers.update()                                            #lesson2
    def constrait(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom))
