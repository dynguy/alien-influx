class Settings():
    def __init__(self):
        # Setting default values for each settings
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (0, 250, 230)
        self.bg_color = (102, 105, 156)
        #self.bg_color = (60, 60, 60)

        # Ship movement settings
        self.ship_speed_factor = 2.5
        # Laser settings
        self.bullet_speed_factor = 4
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.lasers_allowed = 7

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # Note: 1 is right and -1 is left
