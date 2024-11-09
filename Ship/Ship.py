import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False

        # Load the ship image and get rect
        self.image = pygame.image.load(
            r'C:\Users\tony8\PycharmProjects\Alien_Invasion\Ship_converted.bmp')
        desired_width = 150
        height = int(
            self.image.get_height() * desired_width / self.image.get_width())
        self.image = pygame.transform.scale(self.image, (desired_width, height))
        self.rect = self.image.get_rect()

        # Start each game with a new ship, bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)