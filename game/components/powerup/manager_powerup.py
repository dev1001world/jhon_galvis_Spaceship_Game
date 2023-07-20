import pygame,random
from game.components.powerup.shield import Shield 
from game.components.powerup.tnt import Tnt
from game.utils.constants import SPACESHIP_SHIELD

TIME_RANDOM = random.randint(5000,10000)
class PowerUpManager:
    def __init__(self):
        self.power_ups=[]
        self.power_ups_tnt=[]
        self.when_appears = TIME_RANDOM
        self.duration = random.randint(3,5)
        self.has = {
            1:False,
            2:True
        }
    def generate_power_up(self):
        power_up = Shield()
        power_up_tnt = Tnt()
        self.when_appears += TIME_RANDOM
        self.power_ups.append(power_up)
        self.power_ups_tnt.append(power_up_tnt)
    def update(self,game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed,self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = self.has[random.randint(1,2)]
                game.player.power_time_up = power_up.start_time + (self.duration*1000)
                game.player.set_image((65,75),SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)
        if len(self.power_ups_tnt) and current_time >= self.when_appears:
            self.generate_power_up()
        for power_up_tnt in self.power_ups_tnt:
            power_up_tnt.update(game.game_speed,self.power_ups_tnt)
            if game.player.rect.colliderect(power_up_tnt):
                power_up_tnt.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up_tnt.type
                game.player.has_power_up = self.has[2]
                game.player.power_time_up = power_up_tnt.start_time + (self.duration*1000)
                self.power_ups_tnt.remove(power_up)
                game.enemy.remove_enemies()
                
                
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        for power_up_tnt in self.power_ups_tnt:
            power_up_tnt.draw(screen)
    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.power_ups_tnt =[]
        self.when_appears = random.randint(now+5000,now+10000)

