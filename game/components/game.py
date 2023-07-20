import pygame
from game.utils.constants import MESSEGER,RESET, GAMEOVER ,BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.space_ship import Spaceshipt
from game.components.enemy.mangener_enemy import EnemyMangener
from game.components.bullet.manager_bullet import BulletManager
from game.components.enemy.enemy import Enemy
from game.components.menu import Menu
from game.components.powerup.manager_powerup import PowerUpManager
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
        self.menu = Menu('press any key to star...', self.screen)
        self.score = 0
        self.score_player = 0
        self.death_count = 0
        self.high_score = 0
        self.power_up_manager = PowerUpManager()
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
        self.score = 0
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
        self.power_up_manager.update(self)
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.bullet.draw(self.screen)
        self.draw_score()
        self.power_up_manager.draw(self.screen)
        self.power_up_time()
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
            icon = self.image = pygame.transform.scale(ICON,(80,120))
            self.screen.blit(icon,(SCREEN_WIDTH//2-40,(SCREEN_HEIGHT//2)- 150))
            self.menu.draw(self.screen,'press any key to star...',SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        else:
            self.icon_reset()
            self.total_score()
            self.best_score()
            self.total_death() 
            self.resect()
        self.menu.update(self)

    def icon_reset(self):
        game_over = self.image = pygame.transform.scale(GAMEOVER,(500,200))
        self.screen.blit(game_over,(SCREEN_WIDTH//2-250,SCREEN_HEIGHT - 550))
        reset = self.image = pygame.transform.scale(RESET,(100,100))
        self.screen.blit(reset,(SCREEN_WIDTH//2-50,SCREEN_HEIGHT - 400))
        messeger = self.image = pygame.transform.scale(MESSEGER,(500,50))
        self.screen.blit(messeger,(SCREEN_WIDTH//2-250,SCREEN_HEIGHT - 150))      

    def draw_score(self):
        font=pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True,(255,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        self.screen.blit(text,text_rect)
    def total_score(self):
        font=pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Your Score: {self.score_player}', True,BLACK)
        text_rect = text.get_rect()
        text_rect.center = ((SCREEN_WIDTH//2-20,(SCREEN_HEIGHT//2) + 40))
        self.screen.blit(text,text_rect)
    def best_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        font=pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'best score:{self.high_score}', True,BLACK)
        text_rect = text.get_rect()
        text_rect.center = ((SCREEN_WIDTH//2-20,(SCREEN_HEIGHT//2) + 80))
        self.screen.blit(text,text_rect)
    def total_death(self):
        font=pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Total deaths: {self.death_count}', True,BLACK)
        text_rect = text.get_rect()
        text_rect.center = ((SCREEN_WIDTH//2-20,(SCREEN_HEIGHT//2) + 120))
        self.screen.blit(text,text_rect)
    def resect(self):
        if self.high_score > self.score or self.high_score <= self.score:
            self.enemy.remove_enemy()
            self.score_player = self.score
    def power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000,)
            if time_to_show >= 0:
                self.menu.draw(self.screen,f'all enemies did in{time_to_show}', 540,50,(255,255,255))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
                self.power_up_manager.reset()

        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000,)
            if time_to_show >= 0:
                self.menu.draw(self.screen,f'{self.player.power_up_type} is enable for {time_to_show} seconds', 540,50,(255,255,255))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
                self.power_up_manager.reset()
            
        else:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000,)
            if time_to_show >= 0:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
                self.power_up_manager.reset()

