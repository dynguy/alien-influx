import pygame


# Note in pygame, the origin (0,0) is at the top left

class Ship():

    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()  # puts the image into the rect object
        self.screen_rect = screen.get_rect()

        # This will put the new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Tester for movement
        self.moving_right = False
        self.moving_left = False

        # store decimal value for the ship's center
        self.center = float(self.rect.centerx)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:  # 0 because the left side starts at 0
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
