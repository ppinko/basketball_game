import pygame
import math

class Timer():
    """Game timer"""

    def __init__(self, bs, screen):
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.time_limit = bs.time_limit
        self.time_left = bs.time_limit

    def reset_clock(self):
        """Reseting clock"""
        self.clock = pygame.time.Clock()

    def update_timer(self):
        """Update timer"""
        seconds = self.clock.tick() / 1000.0
        self.timer += seconds

    def countdown(self, bs):
        """Show the time left"""
        time_passed = math.trunc(self.timer)
        self.time_left = self.time_limit - time_passed        
        
    def blitme(self, bs, screen):
        """Blit timer on the screen"""
        timefont = pygame.font.SysFont('Arial', 20, bold=True)
        timertext = timefont.render(str(self.time_left), True, 
                bs.text_color, bs.screen_bg_color)
        timertext_image = timertext.get_rect()
        timertext_image.top = 10
        timertext_image.left = 10
        screen.blit(timertext, timertext_image)

class Scoreboard():
    """Tracks the score"""

class Button():
    """Start button"""
       
    def __init__(self, bs, screen):
        """Button initilization"""
                
        # Screen
        self.screen = screen
        self.screen_width = bs.screen_width
        self.screen_height = bs.screen_height
        
        # Copying settings from settings.py
        self.width = bs.buton_width
        self.height = bs.button_width
        self.text_color = bs.button_text_color
        self.bg_color = bs.button_bg_color
        self.text = bs.button_text

        # Creating font
        self.font = pygame.SysFont("Arial", 30, bold = True)

        # Create button background
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_width / 2
        self.rect.centery = self.screen_height / 2
       
        # creating a surface for text
        self.text = self.font.render(self.text, True, self.text_color, 
               self.bg_color)
        
        # creating rectangular image of text
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = self.screen_width / 2
        self.text_rect.centery = self.screen_height / 2

    def draw_button(self):
        """Draw button with text"""

        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.text_rect, self.text_color)
