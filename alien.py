import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):


    def __init__(self, game_settings, screen):
        random_num = randint(1, 2)
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Loading the alien image and settings its rect attributes
        #self.image = pygame.image.load('images/alien.png')
        if random_num == 1:
            self.image = pygame.image.load('images/alien.png')
        else:
            self.image = pygame.image.load('images/alien2.png')

        self.rect = self.image.get_rect()

        # makes the alien start at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # This stores the alien's exact location
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
