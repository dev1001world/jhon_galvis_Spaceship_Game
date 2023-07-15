import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SHIP_WIDTH, SHIP_HEIGHT
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
    def update(self,user_input):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
             self.move_down()
    def move_left(self):
        self.rect.x -=self.SPEED_SHIP
        if self.rect.x < -45:
            self.rect.x = SCREEN_WIDTH
    def move_right(self):
        self.rect.x +=self.SPEED_SHIP
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH - SCREEN_WIDTH
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 3: #deje screenheing // 3  para poder crear una mecanica de esquivar naves enemigas
                self.rect.y -= self.SPEED_SHIP
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
                self.rect.y += self.SPEED_SHIP
    def draw(self, screen):
        screen.blit(self.imgage,self.rect)
