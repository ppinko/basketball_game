"""Main game script"""

import pygame
import sys

from settings import Settings
import game_functions as gf

def run_basketball():
    """Initilizing the game"""
    pygame.init()

    # creating an instance of Settings - bs (basketball settings)
    bs = Settings()
    
    # Create the game window
    screen = pygame.display.set_mode((bs.screen_width, bs.screen_height))
    pygame.display.set_caption("Be like Curry") # displaying name of the game

    while True:
        """Main loop of the game"""

        gf.update_screen(screen, bs) # Update the screen

run_basketball()



    
