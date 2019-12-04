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
        self.mistakes_limit = 3
        self.ball_mistakes_limit = self.mistakes_limit

        # Text settings
        self.text_color = (0, 0, 0)

        # Button settings
        self.button_width = 100
        self.button_height = 50
        self.button_text_color = (255, 0, 0)
        self.button_bg_color = (0, 255, 0)
        self.button_text = "Start game"

        # Time settings
        self.time_limit = 10

        # Game settings
        self.game_active = False

    def reset_mistakes(self):
        """Reset number of mistakes to initial value"""
        self.ball_mistakes_limit = self.mistakes_limit
