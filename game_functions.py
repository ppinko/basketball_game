import pygame
import sys
import random
from backboard import Backboard

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

def create_backboard(screen, bs, backboards):
    """Generate backboards"""
    # Establishing available place in x direction
    min_x = int(bs.backboards_width/2 + 10)
    max_x = int(bs.screen_width - bs.backboards_width/2 - 10)
    
    # Establishing available place in q direction
    min_y = int(bs.backboards_height/2 + 10)
    max_y = int(bs.screen_height - bs.backboards_height/2 - 10)

    # Generating random positions
    backboard_positions = []
    for backboard in range(int(bs.backboards_number/2)):
        backboard_positions.append(random.randint(min_x, max_x))
        backboard_positions.append(random.randint(min_y, max_y))

    for index in range(bs.backboards_number):
        if index % 4 == 0:
            backboard = Backboard(screen, bs)
            backboard.rect.centerx = backboard_positions[index]
            backboard.rect.centery = max_y
            backboards.add(backboard)
        elif index % 4 == 1:
            backboard = Backboard(screen, bs)
            backboard.rect.centery = backboard_positions[index]
            backboard.rect.centerx = max_x 
            backboards.add(backboard)
        elif index % 4 == 2:
            backboard = Backboard(screen, bs)
            backboard.rect.centerx = backboard_positions[index]
            backboard.rect.centery = min_y 
            backboards.add(backboard)
        elif index % 4 == 3:
            backboard = Backboard(screen, bs)
            backboard.rect.centery = backboard_positions[index] 
            backboard.rect.centerx = min_x
            backboards.add(backboard)
    

def update_screen(screen, bs, player, backboards, ball):
    """Update screen"""
    # Redrawing screen background
    screen.fill(bs.screen_bg_color)
    
    # Checking events
    check_events(bs, player)
    
    # Updating position of the player
    player.update(bs)

    # Bliting the player
    player.blitme()
    
    # Blittin the ball
    ball.blitme()

    # Bliting all backboards
    backboards.draw(screen)

    # Refreshing screen
    pygame.display.flip()
