import random

import pygame
from star import Star
from random import Random

class StatsSky():
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_heigth = 800
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_heigth)
        )
        # self.star = Star()
        self.random = Random
        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:

            self.screen.fill((230, 230, 230))
            self.stars.draw(self.screen)
            pygame.display.flip()


    def _create_fleet(self):
        """计算"""
        # 计算星星的宽度
        star = Star(self)
        star_width, star_heigth = star.rect.size
        avialable_space_x = self.screen_width - (2 * star_width)
        star_numbers = avialable_space_x // (2 * star_width)
        avialable_space_y = self.screen_heigth - (2 * star_heigth)
        row_numbers = avialable_space_y // (2 * star_heigth)
        print(f'x={avialable_space_x},y={avialable_space_y}')
        print(f'star_numbers = {star_numbers}, row_numbers = {row_numbers}')

        for i in range(0, 10):
            random_number_x = random.randint(0, self.screen_width)
            random_number_y = random.randint(0, self.screen_heigth)
            print(f'{random_number_x}, {random_number_y}')
            self._create_star(random_number_x, random_number_y)
            i += 1

        # for row_number in range(row_numbers):
        #     for star_number in range(star_numbers):
        #         self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """创建一个星星并加入当前行"""
        star = Star(self)
        # star_width, star_height = star.rect.size
        # star.rect.x = star_width + 2 * star_width * star_number
        # star.rect.y = star_height + 2 * star_height * row_number
        star.rect.x = star_number
        star.rect.y = row_number
        self.stars.add(star)









if __name__ == '__main__':
    ss = StatsSky()
    ss.run_game()




