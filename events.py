import sys

import pygame

#Function designed to run the in-game events

def events():

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,scientist):

    screen.fill(ai_settings.bg_color)
    #ai_settings stands for the Settings() class' instance
    scientist.blitme()

    pygame.display.flip()

#bruno.dmasceno@gmail.com
