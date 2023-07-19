import pygame,random
from pygame.sprite import Sprite
from game.components.enemy.enemy import Enemy
from game.utils.constants import ENEMY_2, SHIP_HEIGHT, SHIP_WIDTH, SCREEN_WIDTH
from game.components.bullet.bullet import Bullet
class EnemyTwo(Enemy, Sprite):
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
    def shoot(self, manager_bullet):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            manager_bullet.add_bullet(bullet)
            self.shooting_time += random.randint(1000,2000)