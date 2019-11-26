import pygame
from pygame.sprite import Sprite

class Backboard():

    def __init__(self, screen, bs):
        "Loading image an initilizing position"
        super(Backboard, self).__init__
        
        # Setting screen size
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bs = bs
        
        # Load the player image and get its rect.
        self.image = pygame.image.load('images/backboard.png')
        # Scaling image 
        self.image = pygame.transform.scale(self.image, (56, 64))
        self.rect = self.image.get_rect()
        
        # Setting initial position of the player to the middle of the screen
        self.rect.top = self.screen_rect.top
        self.rect.centerx = self.screen_rect.centerx
        
    def blitme(self):
        """Draw the backboard at its current position"""
        self.screen.blit(self.image, self.rect)
