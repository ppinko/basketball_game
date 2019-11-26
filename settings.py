class Settings():
    """Class containing all settings of the game"""

    def __init__(self):
        """Initial settings"""

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 700
        self.screen_bg_color = (255, 255, 255) # white background

        # Player settings.
        self.player_speed = 2

        # Backboards settings.
        self.backboards_number = 4
        self.backboards_width = 40
        self.backboards_height = 40

