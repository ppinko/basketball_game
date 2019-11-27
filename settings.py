class Settings():
    """Class containing all settings of the game"""

    def __init__(self):
        """Initial settings"""

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 700
        self.screen_bg_color = (192, 192, 192) # background

        # Player settings.
        self.player_speed = 2
        self.player_width = 80
        self.player_height = 80

        # Backboards settings.
        self.backboards_number = 4
        self.backboards_width = 40
        self.backboards_height = 40

        # Ball settings.
        self.ball_speed = 2
        self.ball_width = 20
        self.ball_height = 20
        self.ball_limit = 4
