import pygame
import sys

def check_events():
    """Collects and checks events"""
    
    for event in pygame.event.get():
        # Enables to close the game while clicking on the 'x'
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, bs, player):
    """Update screen"""
    
    # Redrawing screen background
    screen.fill(bs.screen_bg_color)
    
    # Checking events
    check_events()
    
    # Bliting the player
    player.blitme()

    # Refreshing screen
    pygame.display.flip()
