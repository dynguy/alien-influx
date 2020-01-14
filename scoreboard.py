import pygame.ftfont
from pygame.sprite import Group
from ship import Ship


class Scoreboard():

    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # Font defaults for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_score()  # Setting the initial score image
        self.prep_level()  # Setting the current level user is playing
        #self.prep_ships_left()  # Setting number of lives or ships left

    # Method that helps display the score user has earned
    def prep_score(self):
        # Must be rounded to look more like an arcade game
        rounded_score = int(round(self.stats.score, -1))  # Score will be multiple of 10
        score_str = "SCORE: {:,}".format(rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)

        # Displaying portion
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    # Method that actually displays all the necessary scoring content
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #self.screen.blit(self.ships_left_image, self.ships_left_image)

    # Method that helps display the level user is playing
    def prep_level(self):
        self.level_image = self.font.render("LEVEL: " + str(self.stats.level), True, self.text_color, self.game_settings.bg_color)

        # Setting position of the level
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    # Method that helps display how many lives are left
    # def prep_ships_left(self):
    #     self.ships_left_image = self.font.render("LIVES: " + str(self.stats.level), True, self.text_color, self.game_settings.bg_color)

        # Setting position of the level
        # self.ships_left_image = self.level_image.get_rect()
        # self.ships_left_image.left = self.score_rect.left
        # self.ships_left_image.top = 20

        # self.ships = Group()
        # for ship_number in range(self.stats.ships_left):
        #     ship = Ship(self.game_settings, self.screen)
        #     ship.rect.x = 10 + ship_number * ship.rect.width
        #     ship.rect.y = 10
        #     self.ships.add(ship)


