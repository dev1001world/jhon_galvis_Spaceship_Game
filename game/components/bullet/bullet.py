from typing import Any
import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT
class Bullet(Sprite):
    BULLETS_SIZE = pygame.transform.scale(BULLET,(10,20))
    BULLETS_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY,(10,32))
    BULLETS = {
    'player':BULLETS_SIZE,
    'enemy':BULLETS_SIZE_ENEMY
    }
    SPEED = 20
    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type
    def update(self,bullets):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)
    def draw(self,screen):
        screen.blit(self.image, self.rect)