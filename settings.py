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
        self.init_backboards_width = 80
        self.init_backboards_height = 80
        self.backboards_height = self.init_backboards_height
        self.backboards_width = self.init_backboards_width

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
        self.button_text_color = (255, 255, 255)
        self.button_bg_color = (210, 105, 30)
        self.button_text = "START"

        # Time settings
        self.time_limit = 10.0

        # Game settings
        self.game_active = False

        # Scoreboard settings
        self.score = 0
        self.points_hit = 50
        self.level = 1

    def dynamic_settings(self):
        self.time_limit = round(self.time_limit - 0.2, 1)
        self.points_hit = int(self.points_hit * 1.2)
        if self.backboards_width > 30:
            self.backboards_width = int(self.backboards_width * 0.95)
        if self.backboards_height > 30:        
          self.backboards_height = int(self.backboards_height * 0.95)
        #if self.player_width > 40:
        #    self.player_width = int(self.player_width * 0.95)
        #if self.player_height > 40:
        #    self.player_height = int(self.player_height * 0.95)
        if self.ball_width > 10:
            self.ball_width = int(self.ball_width - 2)
        if self.ball_height > 10:
            self.ball_height = int(self.ball_height -2)


    def level_up(self):
        """Updates the score"""
        self.level += 1

    def update_score(self):
        """Updates the score"""
        self.score += self.points_hit
    
    def reset_score(self):
        """Reset the score after game over"""
        self.score = 0
        self.level = 1
        self.time_limit = 10
        self.backboards_width = self.init_backboards_width
        self.backboards_height = self.init_backboards_height
        self.player_height = 180
        self.player_width = 180
        self.ball_width = 40
        self.ball_height = 40

    def reset_mistakes(self):
        """Reset number of mistakes to initial value"""
        self.ball_mistakes_limit = self.mistakes_limit
