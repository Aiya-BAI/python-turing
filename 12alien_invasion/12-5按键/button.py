import sys
import pygame

class Button:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event)
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)



if __name__ == '__main__':
    bt = Button()
    bt.run_game()





