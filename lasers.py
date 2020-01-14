import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    def __init__(self, game_settings, screen, ship):
        super(Laser, self).__init__()  # creates a laser object at the ship's location
        self.screen = screen

        self.rect = pygame.Rect(0, 0, game_settings.laser_width, game_settings.laser_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = game_settings.laser_color
        self.speed_factor = game_settings.laser_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)