import pygame
import sys

def check_events(bs, player):
    """Collects and checks events"""    
    for event in pygame.event.get():
        # Enables to close the game while clicking on the 'x'
        if event.type == pygame.QUIT:
            sys.exit() 
        elif event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_LEFT:
                player.rect.centerx -= bs.player_speed
            elif event.key == pygame.K_RIGHT:
                player.rect.centerx += bs.player_speed
            elif event.key == pygame.K_UP:
                player.rect.centery -= bs.player_speed
            elif event.key == pygame.K_DOWN:
                player.rect.centery += bs.player_speed

def update_screen(screen, bs, player):
    """Update screen"""
    # Redrawing screen background
    screen.fill(bs.screen_bg_color)
    
    # Checking events
    check_events(bs, player)
    
    # Bliting the player
    player.blitme()

    # Refreshing screen
    pygame.display.flip()
