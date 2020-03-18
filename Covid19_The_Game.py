import sys

import pygame

from pygame.sprite import Group

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

    #creating the scientist

    scientist=Scientist(ai_settings,screen)

    cure=Group()

    # main loop for the game

    while True:

        # watching for the events
        gf.check_events(ai_settings,screen,scientist,cure)
        scientist.update()
        cure.update()
        #getting rid of cures that have disappeared

        for vaccine in cure.copy():
            if vaccine.rect.bottom<=0:
                cure.remove(vaccine)

            print(len(cure))
        # Drawn the mostly recent screen

        gf.update_screen(ai_settings,screen,scientist,cure)




run_game()
#goodfellas
