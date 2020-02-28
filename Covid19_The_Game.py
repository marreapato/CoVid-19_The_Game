import sys

import pygame

from settings import Settings

from scientist import Scientist


# the funtion is supposed to initialize the game, create a screen object and watch for the events

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
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            # Drawn the mostly recent screen

            screen.fill(ai_settings.bg_color)

            scientist.blitme()#drawns the scientist

            pygame.display.flip()


run_game()
