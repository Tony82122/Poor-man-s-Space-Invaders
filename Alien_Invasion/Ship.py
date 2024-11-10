import os

import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False

        # Load the ship image and get rect
        current_dir = os.path.dirname(__file__)
        project_root = os.path.dirname(current_dir)
        image_path = os.path.join(project_root, 'Ship_converted.bmp')

        try:
            self.image = pygame.image.load(image_path)
        except pygame.error as e:
            print(f"Error loading image: {e}")
            print(f"Attempted to load from: {image_path}")
            raise

        desired_width = 50
        height = int(
            self.image.get_height() * desired_width / self.image.get_width())
        self.image = pygame.transform.scale(self.image, (desired_width, height))
        self.rect = self.image.get_rect()

        # Start each game with a new ship, bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
