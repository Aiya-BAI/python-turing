class Settings:
    """存储游戏《外星人入侵》中所有的设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_widch = 1200
        self.screen_heigrh = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 2

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3




