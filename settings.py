class Settings():
    def __init__(self):
        # Setting default values for each settings
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (0, 250, 230)
        self.bg_color = (102, 105, 156)
        #self.bg_color = (60, 60, 60)
        # Ship settings
        self.ship_speed_factor = 2.5
        self.ship_limit = 3
        # Laser settings
        self.laser_speed_factor = 4
        self.laser_width = 5
        self.laser_height = 15
        self.laser_color = 255, 0, 0
        self.lasers_allowed = 7

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # Note: 1 is right and -1 is left

        # Leveling up speed
        self.speed_scale = 1.5
        self.initialize_dynamic_settings()

        # Scoring settings
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.laser_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # Note 1 is right and -1 is left
        self.alien_point_worth = 50


    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.laser_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale

        self.alien_point_worth = int(self.alien_point_worth * self.score_scale)
        # print(self.alien_point_worth)