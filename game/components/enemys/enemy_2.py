import pygame
from pygame.sprite import Sprite
from game.components.enemys.enemy import Enemy
from game.utils.constants import ENEMY_2, SHIP_HEIGHT, SHIP_WIDTH, SCREEN_WIDTH

class Enemy_two(Enemy, Sprite):
    SPEED_Y = 0.5
    SPEED_X = 8
    def __init__(self):
        super().__init__()
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_HEIGHT))
    def change_movement_x(self):
        if self.rect.x >= SCREEN_WIDTH-SHIP_WIDTH:
                self.movement_x = 'left'
                self.step = 0
        if self.rect.x <= 0:
                self.movement_x = 'right'
                self.step = 0