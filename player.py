import pygame
from pygame.sprite import Sprite

class Player():

    def __init__(self, screen, bs):
        """Initilizing the player and setting its position"""
        super(Player, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bs = bs
        
        # Load the player image and get its rect.
        self.image = pygame.image.load('images/lebron.png')
        # Scaling image 
        self.image = pygame.transform.scale(self.image, 
                (bs.player_width, bs.player_height))
        self.rect = self.image.get_rect()
        
        # Setting initial position of the player to the middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # Store the decimal value of the player's position
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Set movement flags
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        # Player maximum field of movement
        self.min_x = bs.backboards_width + 50
        self.max_x = bs.screen_width - bs.backboards_width - 50
        self.min_y = bs.backboards_height + 50
        self.max_y = bs.screen_height - bs.backboards_height - 50


    def blitme(self):
        """Draw the player at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self, bs):
        """Update position of the player"""
        if self.move_left == True and self.rect.left >= self.min_x:
            self.rect.centerx -= bs.player_speed
        if self.move_right == True and self.rect.right <= self.max_x:
            self.rect.centerx += bs.player_speed
        if self.move_up == True and self.rect.top >= self.min_y:
            self.rect.centery -= bs.player_speed
        if self.move_down == True and self.rect.bottom <= self.max_y:
            self.rect.centery += bs.player_speed


