import random
from game.components.enemy.enemy import Enemy
from game.components.enemy.enemy_2 import EnemyTwo
from game.components.enemy.enemy_3 import EnemyThree
class EnemyMangener:
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
        if len(self.enemies) < 5:
            enemy_ships = [Enemy(), EnemyTwo(), EnemyThree()]
            self.enemies.append(enemy_ships[random.randint(0,2)])
    def remove_enemy(self):
        self.enemies=[]