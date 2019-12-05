"""Main game script"""

import pygame
import sys
import random
from pygame.sprite import Group # THAT MUST BE CHECKED

from settings import Settings
from player import Player
from backboard import Backboard
from ball import Ball
from texts import Timer, Button, Scoreboard, Level
import game_functions as gf


def run_basketball():
    """Initilizing the game"""
    pygame.init()

    # creating an instance of Settings - bs (basketball settings)
    bs = Settings()
    
    # Create the game window
    screen = pygame.display.set_mode((bs.screen_width, bs.screen_height))
    pygame.display.set_caption("Be like Lebron") # displaying name of the game

    # create an instance of Timer
    timer = Timer(bs, screen)

    # create a scoreboard
    scoreboard = Scoreboard(bs, screen)

    # create a level
    level = Level(bs, screen)
    
    # creating an instance of Player
    player = Player(screen, bs)
    
    # creating an instance of Backboard
    backboards = Group()
    
    # creating a group of balls
    balls = Group()
    
    # Bliting backboards
    gf.create_backboard(screen, bs, backboards)
     
    # creating a game button
    game_button = Button(bs, screen)
    
    while True:
        """Main loop of the game"""
        
        gf.check_events(screen, bs, player, balls, game_button)

        if bs.game_active:
            gf.player_update(player, bs)
            gf.balls_update(screen, balls, bs)
            gf.backboards_update(screen, bs, backboards, balls, timer, player)

        gf.update_screen(screen, bs, player, backboards, balls, timer, 
                game_button, scoreboard, level) # Update the screen


run_basketball()



    
