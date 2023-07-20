import pygame,random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_WIDTH, SHIP_HEIGHT, DEFAULT_TYPE
from game.components.bullet.bullet import Bullet
class Spaceshipt(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = SCREEN_HEIGHT - 100
    SPEED_SHIP = 10
    def __init__(self):
        self.imgage = SPACESHIP
        self.imgage = pygame.transform.scale(self.imgage,(SHIP_WIDTH,SHIP_HEIGHT))
        self.rect = self.imgage.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.time = True
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

    def update(self,user_input,game):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
             self.move_down()
        if user_input[pygame.K_SPACE] or user_input[pygame.K_l]:
             self.shooter(game)
    def shooter(self,manager_bullet): #falta modificar para que pueda disparar bien
        bullet = Bullet(self)
        manager_bullet.add_bullet(bullet)
    def move_left(self):
        self.rect.x -=self.SPEED_SHIP
        if self.rect.x < -45:
            self.rect.x = SCREEN_WIDTH
    def move_right(self):
        self.rect.x +=self.SPEED_SHIP
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH - SCREEN_WIDTH
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 3:
                self.rect.y -= self.SPEED_SHIP
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
                self.rect.y += self.SPEED_SHIP
    def draw(self, screen):
        screen.blit(self.imgage,self.rect)
    def set_image(self,size = (40,60), image= SPACESHIP):
         self.imgage = image
         self.imgage = pygame.transform.scale(self.imgage, size)