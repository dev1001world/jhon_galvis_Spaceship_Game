import random
from game.components.enemys.enemy import Enemy
from game.components.enemys.enemy_2 import EnemyTwo
from game.components.enemys.enemy_3 import EnemyThree
#random_enemy = random.randint(1,10)
class Enemy_mangener:
    def __init__(self):
        self.enemies = []
    def update(self,game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies,game)
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    def add_enemy(self):
        if len(self.enemies) < 10:
            enemys_ships = [Enemy(), EnemyTwo(), EnemyThree()]
            self.enemies.append(enemys_ships[random.randint(0,2)])