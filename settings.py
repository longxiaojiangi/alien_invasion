class Settings():
    def __init__(self):
        self.screen_width = 1200 # 游戏窗口宽度
        self.screen_height = 600 # 游戏窗口高度
        self.bg_color = (230,230,230) # 游戏窗口背景色
        self.ship_speed_factor = 1.5 # 飞船移动速度
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 3 # 速度
        self.bullet_width = 3 # 宽
        self.bullet_height = 15 # 高
        self.bullet_color = 60,60,60 # 颜色
        self.bullets_allowed = 3 # 将屏幕上未消失的子弹限制为3颗
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1右-1左
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1 # 1右-1左
        self.alien_points = 50
    def increase_speed(self):
        # 提高速度
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)