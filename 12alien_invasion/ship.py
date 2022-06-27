import pygame
from settings import Settings

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 给ship类添加属性settings, 以便能够在update()中使用
        self.settings = Settings()
        # self.settings = ai_game.settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('12-6侧面射击/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每一艘新飞船，都将其放在屏幕底部中间
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.center = self.screen_rect.center

        # 在飞船属性x中存储最小数值,(可使用小数来设置rect的值，但是rect将只存储这个值的整数部分)
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        # if self.moving_right:
        #     self.rect.x += self.settings.ship_speed
        # if self.moving_left:
        #     self.rect.x -= self.settings.ship_speed

        # if self.moving_right:
        #     self.rect.x += self.settings.ship_speed
        # if self.moving_left:
        #     self.rect.x -= self.settings.ship_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # 根据self.x更新rect对象
        # self.rect.x = self.x

    def blime(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


