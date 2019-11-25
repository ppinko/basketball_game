import pygame
import sys

def check_events(bs, player):
    """Collects and checks events"""    
    for event in pygame.event.get():
        # Enables to close the game while clicking on the 'x'
        if event.type == pygame.QUIT:
            sys.exit() 
        elif event.type == pygame.KEYDOWN:
            check_events_KEYDOWNS(event, bs, player)
        elif event.type == pygame.KEYUP:
            check_events_KEYUPS(event, bs, player)

def check_events_KEYDOWNS(event, bs, player):
    """Check key presses"""
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_LEFT:
        player.move_left = True
    if event.key == pygame.K_RIGHT:
        player.move_right = True
    if event.key == pygame.K_UP:
        player.move_up = True
    if event.key == pygame.K_DOWN:
        player.move_down = True

def check_events_KEYUPS(event, bs, player):
    """Check key releases"""
    if event.key == pygame.K_LEFT:
        player.move_left = False
    if event.key == pygame.K_RIGHT:
        player.move_right = False
    if event.key == pygame.K_UP:
        player.move_up = False
    if event.key == pygame.K_DOWN:
        player.move_down = False

def update_screen(screen, bs, player):
    """Update screen"""
    # Redrawing screen background
    screen.fill(bs.screen_bg_color)
    
    # Checking events
    check_events(bs, player)
    
    # Updating position of the player
    player.update(bs)

    # Bliting the player
    player.blitme()

    # Refreshing screen
    pygame.display.flip()
