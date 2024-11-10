import os
import pygame
from Settings import Settings

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
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
        height = int(self.image.get_height() * desired_width / self.image.get_width())
        self.image = pygame.transform.scale(self.image, (desired_width, height))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's position based on the movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = int(self.x)

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)