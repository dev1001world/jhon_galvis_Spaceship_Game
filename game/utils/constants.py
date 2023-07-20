import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
TNT = pygame.image.load(os.path.join(IMG_DIR, 'Other/tnt.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

MESSEGER = pygame.image.load(os.path.join(IMG_DIR, 'Other/messager.png'))

GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))
RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))


DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
TNT_TYPE = 'tnt'


SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_ROCK =pygame.image.load(os.path.join(IMG_DIR, "Enemy/ROCA.png"))

SHIP_WIDTH = 40
SHIP_HEIGHT = 60

FONT_STYLE = 'freesansbold.ttf'
