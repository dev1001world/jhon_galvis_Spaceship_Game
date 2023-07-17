import random
from game.components.enemys.enemy import Enemy
from game.components.enemys.enemy_2 import Enemy_two
from game.components.enemys.enemy_3 import Enemy_three
class Enemy_mangener:
    def __init__(self):
        self.enemies = []
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    def add_enemy(self):
        if len(self.enemies) < 10:
            enemys_ships = [Enemy(), Enemy_two(), Enemy_three()]
            self.enemies.append(enemys_ships[random.randint(0,2)])

    