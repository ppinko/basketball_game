"""Main game script"""

import pygame
import sys

from settings import Settings
from player import Player
import game_functions as gf

def run_basketball():
    """Initilizing the game"""
    pygame.init()

    # creating an instance of Settings - bs (basketball settings)
    bs = Settings()
    
    # Create the game window
    screen = pygame.display.set_mode((bs.screen_width, bs.screen_height))
    pygame.display.set_caption("Be like Curry") # displaying name of the game

    # creating an instance of Player
    player = Player(screen, bs)

    while True:
        """Main loop of the game"""

        gf.update_screen(screen, bs, player) # Update the screen

run_basketball()



    
