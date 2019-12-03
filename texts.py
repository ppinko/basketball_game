import pygame
import math

class Timer():
    """Game timer"""

    def __init__(self, bs, screen):
        self.clock = pygame.time.Clock()
        self.timer = 0

    def reset_clock(self):
        """Reseting clock"""
        self.clock = pygame.time.Clock()

    def update_timer(self):
        """Update timer"""
        seconds = self.clock.tick() / 1000.0
        self.timer += seconds

    def blitme(self, bs, screen):
        """Blit timer on the screen"""
        displaytimer = math.trunc(self.timer)
        timefont = pygame.font.SysFont('Arial', 12)
        timertext = timefont.render(str(displaytimer), True, 
                bs.text_color, bs.screen_bg_color)
        timertext_image = timertext.get_rect()
        timertext_image.top = 10
        timertext_image.left = 10
        screen.blit(timertext, timertext_image)
