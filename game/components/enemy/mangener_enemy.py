import random
from game.components.enemy.enemy import Enemy
from game.components.enemy.enemy_2 import EnemyTwo
from game.components.enemy.enemy_3 import EnemyThree
from game.components.enemy.enemy_rock import EnemyRock
class EnemyMangener:
    def __init__(self):
        self.enemies = []
        self.rock = []
    def update(self,game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies,game)
        for rock in self.rock:
            rock.update(self.rock,game)
                            
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for rock in self.rock:
            rock.draw(screen)
    def add_enemy(self):
        if len(self.enemies) < 5:
            enemy_ships = [Enemy(), EnemyTwo(), EnemyThree()]
            self.enemies.append(enemy_ships[random.randint(0,2)])
        if len(self.rock) < 2:
            enemy_rock = EnemyRock()
            self.rock.append(enemy_rock)

    def remove_enemy(self):
        self.enemies=[]
        self.rock = []