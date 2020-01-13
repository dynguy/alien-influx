class GameStats():
    def __init__(self, game_settings):
        self.game_settings = game_settings  # Sets game settings to game settings passed in
        self.reset_stats()  # Restores total lives left
        self.game_active = False  # Starts the game in an inactive state

    # Resets the total lives left
    def reset_stats(self):
        self.ships_left = self.game_settings.ship_limit
