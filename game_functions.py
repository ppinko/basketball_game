import pygame
import sys
import random
import math

from backboard import Backboard
from ball import Ball
from texts import Timer

def check_events(screen, bs, player, balls, game_button):
    """Collects and checks events"""    
    for event in pygame.event.get():
        # Enables to close the game while clicking on the 'x'
        if event.type == pygame.QUIT:
            sys.exit() 
        
        # Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # gather position of the click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_game_button(game_button, mouse_x, mouse_y, bs)

        # Keyboards presses
        if event.type == pygame.KEYDOWN:
            check_events_KEYDOWNS(event, screen, bs, player, balls)
        if event.type == pygame.KEYUP:
            check_events_KEYUPS(event, bs, player)

def check_events_KEYDOWNS(event, screen, bs, player, balls):
    """Check key presses"""

    # Game exit
    if event.key == pygame.K_q:
        sys.exit()
    
    # Player movement
    if event.key == pygame.K_LEFT:
        player.move_left = True
    if event.key == pygame.K_RIGHT:
        player.move_right = True
    if event.key == pygame.K_UP:
        player.move_up = True
    if event.key == pygame.K_DOWN:
        player.move_down = True

    # Shooting a ball
    if event.key == pygame.K_w and check_number_balls(balls, bs):
        new_ball = Ball(screen, bs, 'up', player)
        balls.add(new_ball)
    if event.key == pygame.K_s and check_number_balls(balls, bs):
        new_ball = Ball(screen, bs, 'down', player)
        balls.add(new_ball)
    if event.key == pygame.K_d and check_number_balls(balls, bs):
        new_ball = Ball(screen, bs, 'right', player)
        balls.add(new_ball)
    if event.key == pygame.K_a and check_number_balls(balls, bs):
        new_ball = Ball(screen, bs, 'left', player)
        balls.add(new_ball)

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

def check_game_button(game_button, mouse_x, mouse_y, bs):
    """Check when player cliks start"""
    button_clicked = game_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        # Start the game
        bs.game_active = True

        # Hide the mouse coursor
        pygame.mouse.set_visible(False)


def check_number_balls(balls, bs):
    """Checking active balls"""
    if len(balls) < bs.ball_limit:
        return True
    else:
        return False

def update_balls_number(screen, bs, balls):
    """Removing balls that hit the edge of the screen"""
    for ball in balls.copy():
        if ball.rect.top <= 0 or ball.rect.top >= bs.screen_height or ball.rect.left <= 0 or ball.rect.right >= bs.screen_width:
            balls.remove(ball)
            bs.ball_mistakes_limit -= 1

def create_backboard(screen, bs, backboards):
    """Generate backboards"""
    # Establishing available place in x direction
    min_x = int(3 * bs.backboards_width/2 + bs.player_width/2 + 50)
    max_x = int(bs.screen_width - 3*bs.backboards_width/2 - 
            bs.player_width/2 - 50)
    
    # Establishing available place in q direction
    min_y = int(3*bs.backboards_height/2 + bs.player_height/2 + 50)
    max_y = int(bs.screen_height - 3*bs.backboards_height/2 - 
            bs.player_height - 50)

    # Generating random positions
    backboard_positions = []
    for backboard in range(int(bs.backboards_number/2)):
        backboard_positions.append(random.randint(min_x, max_x))
        backboard_positions.append(random.randint(min_y, max_y))

    for index in range(bs.backboards_number):
        if index % 4 == 0:
            backboard = Backboard(screen, bs)
            backboard.rect.centerx = backboard_positions[index]
            backboard.rect.bottom = bs.screen_height - 25
            backboards.add(backboard)

        elif index % 4 == 1:
            backboard = Backboard(screen, bs)
            backboard.rect.centery = backboard_positions[index]
            backboard.rect.right = bs.screen_width - 25
            backboards.add(backboard)
        elif index % 4 == 2:
            backboard = Backboard(screen, bs)
            backboard.rect.centerx = backboard_positions[index]
            backboard.rect.top = 25
            backboards.add(backboard)
        elif index % 4 == 3:
            backboard = Backboard(screen, bs)
            backboard.rect.centery = backboard_positions[index] 
            backboard.rect.left = 25
            backboards.add(backboard)
    
def remove_backboards(backboards, balls):
    """Remove the backboards which were hit by ball"""
    collisions = pygame.sprite.groupcollide(balls, backboards, True, True)

def check_backboards(backboards):
    """Checking number of backboards"""
    if len(backboards) == 0:
        return True
    else:
        return False

def next_level(screen, bs, backboards):
    """Inceasing game level"""
    if check_backboards(backboards):
       create_backboard(screen, bs, backboards)
       bs.reset_mistakes()
    else:
        pass
 
def lost_game(timer, bs, screen):
    """Definies conditions when player loses the game"""

    # Time limit
    if timer.time_left <= 0 or bs.ball_mistakes_limit <= 0:
        return True

def restart_game(timer, bs, screen, backboards, balls, player):
    "Actions to take to restart the game"
    if lost_game(timer, bs, screen):
        bs.game_active = False
        backboards.empty()
        balls.empty()
        create_backboard(screen, bs, backboards)
        player.restart(bs)
        bs.ball_mistakes_limit = bs.mistakes_limit
        timer.reset_clock()
        pygame.mouse.set_visible(True)

def balls_update(screen, balls, bs):
    """Update balls positions and number"""

    balls.update(bs)
    update_balls_number(screen, bs, balls)

def player_update(player, bs):
    """Update position of the player"""
    player.update(bs)

def backboards_update(screen, bs, backboards, balls):
    """Update position of all backboard"""
    
    # Remove backboards which were hit by ball
    remove_backboards(backboards, balls)
    
    # Level up if no more backboards
    next_level(screen, bs, backboards)

def update_screen(screen, bs, player, backboards, balls, timer, game_button):
    """Update screen"""

    # Redrawing screen background
    screen.fill(bs.screen_bg_color)
    
    # Bliting the player
    player.blitme()
    
    # Drawing the balls
    balls.draw(screen)

    # Drawing the backboards
    backboards.draw(screen)
    
    # Checking if the player didn't lose the game
    lost_game(timer, bs, screen)

    # Blitting timer
    timer.update_timer()
    timer.countdown(bs)
    timer.blitme(bs, screen)

    # Restart game when loses
    restart_game(timer, bs, screen, backboards, balls, player)
    
    if not bs.game_active:
        game_button.draw_button()

    # Refreshing screen
    pygame.display.flip()
