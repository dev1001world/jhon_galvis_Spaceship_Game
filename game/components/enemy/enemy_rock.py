import pygame,random
from pygame.sprite import Sprite
from game.components.enemy.enemy import Enemy
from game.utils.constants import ENEMY_ROCK, SHIP_HEIGHT, SHIP_WIDTH, SCREEN_WIDTH

class EnemyRock(Enemy, Sprite):
    SPEED_Y = random.randint(1,10)
    SPEED_X = random.randint(1,10)
    def __init__(self):
        super().__init__()
        self.image = ENEMY_ROCK
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_HEIGHT))
        self.shooting_time = 0
    def change_movement_x(self):
        if self.rect.x >= SCREEN_WIDTH-SHIP_WIDTH:
                self.movement_x = 'left'
                self.step = 0
        if self.rect.x <= 0:
                self.movement_x = 'right'
                self.step = 0
    def shoot(self, manager_bullet):#falta modificar para que dispare sin que se bug
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            self.shooting_time += random.randint(2000,3000)