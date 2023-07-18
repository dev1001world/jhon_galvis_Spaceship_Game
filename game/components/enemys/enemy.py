from typing import Any
import pygame, random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SHIP_WIDTH, SHIP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullet.bullet import Bullet
class Enemy(Sprite): 
    POS_Y= 10 
    SPEED_X = 1
    SPEED_Y = 1
    MOVE_X = {0: 'left', 1:'right'}
    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1,SCREEN_WIDTH)
        self.rect.y = self.POS_Y
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOVE_X[random.randint(0,1)]
        self.move_for_x = random.randint(50, 100)
        self.step = 0
        self.type = 'enemy'
        self.shooting_time = 1000
    def update(self, enemies,game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet)
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)
        
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement_x()
    def shoot(self, manager_bullet):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            manager_bullet.add_bullet(bullet)
            self.shooting_time += random.randint(2000,3000)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def change_movement_x(self):
        self.step += 1
        if (self.step >= self.move_for_x and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH-SHIP_WIDTH):
            self.movement_x = 'left'
            self.step = 0
        if (self.step >= self.move_for_x and self.movement_x == 'left') or (self.rect.x <= 0):
            self.movement_x = 'right'
            self.step = 0