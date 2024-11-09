import sys
import pygame

from Settings.Settings import Settings
from Ship.Ship import Ship


class AlienInvaders:
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()  # Instantiate Settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Poor mans' Space Invaders")

        self.ship = Ship(self)  # Instantiate Ship

    def run_game(self):
        """Start main game ."""
        while True:
            self._check_events()
            self._update_screen()
            self._update_screen()

    def _check_events(self):
        """keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True

                self.ship.rect.x += 10

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvaders()
    ai.run_game()
