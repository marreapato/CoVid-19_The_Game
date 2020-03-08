import sys

import pygame

#Function designed to run the in-game events

def check_keydown_events(event,scientist):#events triggered when pressing a key

    if event.key == pygame.K_RIGHT:  # BE CAREFUL, up there i am using .type while here i am using .key

        scientist.moving_right = True

    elif event.key == pygame.K_LEFT:

        scientist.moving_left = True

    elif event.key == pygame.K_UP:

        scientist.moving_up= True

    elif event.key == pygame.K_DOWN:

        scientist.moving_down=True

def check_key_up_events(event,scientist):#events triggered when realeasing a key

    if event.key == pygame.K_RIGHT:

        scientist.moving_right = False

    elif event.key == pygame.K_LEFT:

        scientist.moving_left = False

    elif event.key == pygame.K_UP:

        scientist.moving_up = False

    elif event.key == pygame.K_DOWN:

        scientist.moving_down = False

def check_events(scientist):

    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            sys.exit()

        elif event.type==pygame.KEYDOWN:

            check_keydown_events(event,scientist)


        elif event.type==pygame.KEYUP:

            check_key_up_events(event,scientist)





def update_screen(ai_settings,screen,scientist):

    screen.fill(ai_settings.bg_color)

    #ai_settings stands for the Settings() class' instance

    scientist.blitme()

    pygame.display.flip()

