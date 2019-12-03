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
        self.player_width = 180
        self.player_height = 180

        # Backboards settings.
        self.backboards_number = 4
        self.backboards_width = 80
        self.backboards_height = 80

        # Ball settings.
        self.ball_speed = 3
        self.ball_width = 40
        self.ball_height = 40
        self.ball_limit = 4

        # Text settings
        self.text_color = (0, 255, 0)        

        # Time settings.
        self.time = 10
        
