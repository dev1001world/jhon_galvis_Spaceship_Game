import pygame
from pygame.sprite import Sprite
from game.components.enemys.enemy import Enemy
from game.utils.constants import ENEMY_3, SHIP_HEIGHT, SHIP_WIDTH, SCREEN_WIDTH
class EnemyThree(Enemy, Sprite):
    SPEED_Y = 15
    SPEED_X = 1
    def __init__(self):
        super().__init__()
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_HEIGHT))
    def change_movement_x(self):
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0