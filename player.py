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
        self.image = pygame.image.load('images/player.png')
        # Scaling image 
        self.image = pygame.transform.scale(self.image, (35, 64))
        self.rect = self.image.get_rect()
        
        # Setting initial position of the player to the middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # Store the decimal value of the player's position
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

    def blitme(self):
        """Draw the player at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update position of the player"""
        for event in pygame.event.get():
            if event.type == pygame.K_LEFT:
                self.center_x -= bs.player_speed
            elif event.type == pygame.K_RIGHT:
                self.center_x += bs.player_speed
            elif event.type == pygame.K_UP:
                self.center_y -= bs.player_speed
            elif event.type == pygame.K_DOWN:
                self.center_y += bs.player_speed
