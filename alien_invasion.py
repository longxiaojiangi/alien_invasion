import pygame
from settings import Settings # 游戏设置类
from ship import Ship # 导入飞船类
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    pygame.init() # 初始化
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) # 游戏窗口
    play_button = Button(ai_settings,screen,"开始游戏")
    pygame.display.set_caption("武装飞船1.0") # 窗口左上角内容
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen) # 创建飞船
    bullets = Group() # 创建用于存储子弹的编组
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True: # 主循环
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game() # 运行游戏