import sys

import pygame

from settings import Settings

from scientist import Scientist

import events as gf



# the function is supposed to initialize the game, create a screen object and watch for the events

def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # uses a tuple to set the dimensions

    pygame.display.set_caption("Covid19 The Game")

    #creting the scientist

    scientist=Scientist(screen)

    # main loop for the game

    while True:

        # watching for the events
        gf.events()
        # Drawn the mostly recent screen

        gf.update_screen(ai_settings,screen,scientist)


run_game()
