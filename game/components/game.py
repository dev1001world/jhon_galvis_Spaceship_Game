import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.space_ship import Spaceshipt
from game.components.enemy.mangener_enemy import EnemyMangener
from game.components.bullet.manager_bullet import BulletManager
from game.components.enemy.enemy import Enemy
from game.components.menu import Menu
BLACK = (0,0,0)
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceshipt()
        self.enemy = EnemyMangener()
        self.bullet = BulletManager()
        self.classenemy = Enemy()
        self.running = False
        self.menu = Menu('press any key ta star...', self.screen)
        self.score = 0
        self.death_count = 0
        self.best_score_player = 0
        self.total_score_player = 0
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet)
        self.enemy.update(self)
        self.bullet.update(self)
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.bullet.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()
    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.updata_message("GAME OVER. Press SPACE key to restart")
            self.total_score()
            self.best_score()
            self.total_death()
            self.score = 0
        icon = self.image = pygame.transform.scale(ICON,(80,120))
        self.screen.blit(icon,(SCREEN_WIDTH//2-40,(SCREEN_HEIGHT//2)- 150))
        self.menu.update(self)
    def draw_score(self):
        font=pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True,(255,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        self.screen.blit(text,text_rect)
    def total_score(self):
        self.score_player = []
        self.var_score =True
        if self.var_score:
            self.score_player.append(self.total_score_player)
            font=pygame.font.Font(FONT_STYLE, 30)
            text = font.render(f'Your Score: {self.score_player[0]}', True,BLACK)
            text_rect = text.get_rect()
            text_rect.center = ((SCREEN_WIDTH//2-40,(SCREEN_HEIGHT//2) + 40))
            self.screen.blit(text,text_rect)   
    def best_score(self):
        font=pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Best score: {self.best_score_player}', True,BLACK)
        text_rect = text.get_rect()
        text_rect.center = ((SCREEN_WIDTH//2-40,(SCREEN_HEIGHT//2) + 80))
        self.screen.blit(text,text_rect)
    def total_death(self):
        font=pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Total deaths: {self.death_count}', True,BLACK)
        text_rect = text.get_rect()
        text_rect.center = ((SCREEN_WIDTH//2-40,(SCREEN_HEIGHT//2) + 120))
        self.screen.blit(text,text_rect)


            




            