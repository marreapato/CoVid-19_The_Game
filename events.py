import sys

import pygame

#Function designed to run the in-game events

def check_events(scientist):

    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            sys.exit()

        elif event.type==pygame.KEYDOWN:

            if event.key==pygame.K_RIGHT:#BE CAREFUL, up there i am using .type while here i am using .key

                scientist.moving_right=True

            elif event.key==pygame.K_LEFT:

                scientist.moving_left=True

        elif event.type==pygame.KEYUP:

            if event.key==pygame.K_RIGHT:

                scientist.moving_right=False

            elif event.key==pygame.K_LEFT:

                scientist.moving_left=False




def update_screen(ai_settings,screen,scientist):

    screen.fill(ai_settings.bg_color)

    #ai_settings stands for the Settings() class' instance

    scientist.blitme()

    pygame.display.flip()

