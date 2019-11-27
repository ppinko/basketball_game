import pygame
from pygame.sprite import Sprite

class Ball(Sprite):

    def __init__(self, screen, bs, direction, player):
        """Initilizing the ball and setting its position"""
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bs = bs
        self.direction = direction
        
        # Load the ball image and get its rect.
        self.image = pygame.image.load('images/ball.png')
        # Scaling image 
        self.image = pygame.transform.scale(self.image, 
                (bs.ball_width, bs.ball_height))
        self.rect = self.image.get_rect()
        
        # Setting initial position of the ball to the middle of the screen
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery

    def blitme(self):
        """Draw the ball at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self, bs):
        """Update position of the ball"""
        if self.direction == 'left':
            self.rect.centerx -= bs.ball_speed
        elif self.direction == 'right':
            self.rect.centerx += bs.ball_speed
        elif self.direction == 'up':
            self.rect.centery -= bs.ball_speed
        elif self.direction == 'down':
            self.rect.centery += bs.ball_speed

            
