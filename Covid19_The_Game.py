import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from scientist import Scientist

import events as gf

from coronavirus import Covid_19

from game_stats import Games_stats

from button import Button

from scoreboard import Scoreboard

# the function is supposed to initialize the game, create a screen object and watch for the events

def run_game():

    pygame.init()

    pygame.mixer.init()

    pygame.mixer.music.load("USSR.mp3")
    pygame.mixer.music.play()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # uses a tuple to set the dimensions

    background = pygame.image.load('combined_worldmap_wc_3800.png')

    background = pygame.transform.scale(background,(ai_settings.screen_width,ai_settings.screen_height))  #background with the same
    #size of the screen

    #making the play button

    play_button=Button(ai_settings,screen,"Play")


    pygame.display.set_caption("Covid19 The Game")

    #creating the scientist

    scientist=Scientist(ai_settings,screen)
    viruses=Group()
    cure=Group()


    #storing stats and score
    stats=Games_stats(ai_settings)
    score_board=Scoreboard(ai_settings,screen,stats)

    gf.create_fleet(ai_settings,screen,scientist,viruses)
    # main loop for the game

    while True:

        # watching for the events
        gf.check_events(ai_settings,screen,stats,score_board,scientist,cure,viruses,play_button)
        if stats.game_active==True:
            scientist.update()
            #getting rid of cures that have disappeared
            gf.update_cure(ai_settings,screen,stats,score_board,scientist,viruses,cure)
            gf.update_viruses(ai_settings,stats,screen,score_board,scientist,viruses,cure)
        # Draw the mostly recent screen
        gf.update_screen(background,screen,stats,score_board,scientist,viruses,cure,play_button)




run_game()

