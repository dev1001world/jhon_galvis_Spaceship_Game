import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH
class Spaceshipt(Sprite):
    def __init__(self):
        self.imgage = SPACESHIP
        self.imgage = pygame.transform.scale(self.imgage,(40,60))
        self.rect = self.imgage.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - 40
        self.rect.y = SCREEN_HEIGHT - 100
    def update(self,user_input):
        if user_input[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -=10
            
        elif user_input[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:                    
                self.rect.x +=10

        if user_input[pygame.K_UP]:
            if self.rect.y > SCREEN_HEIGHT // 3: #deje screenheing // 3  para poder crear una mecanica de esquivar naves enemigas
                self.rect.y -= 10
        elif user_input[pygame.K_DOWN]:
            if self.rect.y < SCREEN_HEIGHT - 70:
                self.rect.y += 10
    def draw(self, screen):
        screen.blit(self.imgage,self.rect)
