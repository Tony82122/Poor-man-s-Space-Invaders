import sys
import pygame

from Settings import Settings


class AlienInvaders:
    def __init__(self):
        """ overall class to manage game assets and behaviour"""
        pygame.init()
        self.settings = Settings

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Poor mans' Space Invaders")
        self.bg_color = (230,230,230)

        def run_game(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.quit():
                        sys.exit()
                        self.screen.fill(self.Settings.bg_color)
                        pygame.display.flip()

                        if __name__ == '__main__':
                            ai = AlienInvaders()
                            ai.run_game()