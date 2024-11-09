import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect =ai_game.screen.get_rect()

        # Load the ship image and get rect

        self.image = pygame.image.load('images/ship/bmp')
        self.rect = self.image.get_rect()

        #Start each game with a new ship, bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        def blitme(self):
            self.screen.blit(self.image,self.rect)