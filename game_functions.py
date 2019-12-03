import pygame
import sys
import random
import math

from backboard import Backboard
from ball import Ball

def check_events(screen, bs, player, balls):
    """Collects and checks events"""    
    for event in pygame.event.get():
        # Enables to close the game while clicking on the 'x'
        if event.type == pygame.QUIT:
            sys.exit() 
        elif event.type == pygame.KEYDOWN:
            check_events_KEYDOWNS(event, screen, bs, player, balls)
        elif event.type == pygame.KEYUP:
            check_events_KEYUPS(event, bs, player)

def check_events_KEYDOWNS(event, screen, bs, player, balls):
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

def check_number_balls(balls, bs):
    """Checking active balls"""
    if len(balls) < bs.ball_limit:
        return True
    else:
        return False

def update_balls_number(screen, bs, balls):
    """Removing balls that hit backboards or hit the edge of the screen"""
    for ball in balls.copy():
        if ball.rect.top <= 0 or ball.rect.top >= bs.screen_height or ball.rect.left <= 0 or ball.rect.right >= bs.screen_width:
            balls.remove(ball)
                
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
    else:
        pass

def show_time(screen, bs, clock, timer):
    seconds = clock.tick() / 1000.0
    timer += seconds
    print(timer)
    displaytimer = math.trunc(timer)
    timefont = pygame.font.SysFont('Arial', 12)
    timertext = timefont.render(str(displaytimer), True, bs.text_color, 
            bs.screen_bg_color)
    timertext_image = timertext.get_rect()
    timertext_image.top = 10
    timertext_image.left = 10
    screen.blit(timertext, timertext_image)
    return timer 

def update_screen(screen, bs, player, backboards, balls, clock, timer):
    """Update screen"""
    # Redrawing screen background
    screen.fill(bs.screen_bg_color)
    
    # Checking events
    check_events(screen, bs, player, balls)
    
    # Updating position of the player
    player.update(bs)

    # Bliting the player
    player.blitme()
    
    # Blittin the balls
    balls.update(bs)
    balls.draw(screen)
    update_balls_number(screen, bs, balls)

    # Bliting all backboards
    remove_backboards(backboards, balls)
    next_level(screen, bs, backboards)
    backboards.draw(screen)
    
    # Blitting timer
    show_time(screen, bs, clock, timer)

    # Refreshing screen
    pygame.display.flip()
