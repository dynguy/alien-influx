import sys
import pygame  # Importing Pygame
from settings import Settings  # Importing the game settings from settings class
from ship import Ship  # Importing ship class
import game_functions as gf
from pygame.sprite import Group
from alien import Alien



def run_game():
    # Initialize game properly and create a screen object
    pygame.init()
    game_settings = Settings()

    # Declaring screen variable that contains display content
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # 1200 wide, 800 high
    # Setting background color
    # background_color = (0, 120, 230)
    # Setting caption of game
    pygame.display.set_caption("Alien Invasion")
    # Creates ship
    ship = Ship(game_settings, screen)
    # Makes a group to store lasers in
    lasers = Group()
    # Creating Alien
    alien = Alien(game_settings, screen)
    # Makes a group of Aliens
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)


    # Main loop for the game.
    while True:
        # For loop that watches for keyboard and mouse events
        gf.check_events(game_settings, screen, ship, lasers)
        ship.update()
        gf.update_lasers(game_settings, screen, ship, aliens, lasers)
        gf.update_aliens(game_settings, aliens)
        # Takes 3 parameters and uses them to update the screen illusion
        gf.update_screen(game_settings, screen, ship, aliens, lasers)



# Running the game
run_game()