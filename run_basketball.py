"""Main game script"""

import pygame
import sys
import random
from pygame.sprite import Group # THAT MUST BE CHECKED

from settings import Settings
from player import Player
from backboard import Backboard
from ball import Ball
import game_functions as gf


def run_basketball():
    """Initilizing the game"""
    pygame.init()

    # creating an instance of Settings - bs (basketball settings)
    bs = Settings()
    
    # Create the game window
    screen = pygame.display.set_mode((bs.screen_width, bs.screen_height))
    pygame.display.set_caption("Be like Lebron") # displaying name of the game

    # creating an instance of Player
    player = Player(screen, bs)
    
    # creating an instance of Backboard
    backboards = Group()
    
    # creating a group of balls
    balls = Group()
    
    # Bliting backboards
    gf.create_backboard(screen, bs, backboards)
    
    while True:
        """Main loop of the game"""

        gf.update_screen(screen, bs, player, backboards, balls) # Update the screen

run_basketball()



    
