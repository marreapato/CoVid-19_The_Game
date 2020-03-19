import sys

import pygame

from cure import Cure

#Function designed to run the in-game events


def check_keydown_events(event,ai_settings,screen,scientist,cure):#events triggered when pressing a key

    if event.key == pygame.K_RIGHT:  # BE CAREFUL, up there i am using .type while here i am using .key

        scientist.moving_right = True

    elif event.key == pygame.K_LEFT:

        scientist.moving_left = True

    elif event.key == pygame.K_UP:

        scientist.moving_up= True

    elif event.key == pygame.K_DOWN:

        scientist.moving_down=True

    elif event.key==pygame.K_SPACE:
    #Creates a new cure fragment and adds it to the screen

        fire_cure(ai_settings,screen,scientist,cure)




def check_key_up_events(event,scientist):#events triggered when realeasing a key

    if event.key == pygame.K_RIGHT:

        scientist.moving_right = False

    elif event.key == pygame.K_LEFT:

        scientist.moving_left = False

    elif event.key == pygame.K_UP:

        scientist.moving_up = False

    elif event.key == pygame.K_DOWN:

        scientist.moving_down = False

def check_events(ai_settings,screen,scientist,cure):

    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            sys.exit()

        elif event.type==pygame.KEYDOWN:

            check_keydown_events(event,ai_settings,screen,scientist,cure)


        elif event.type==pygame.KEYUP:

            check_key_up_events(event,scientist)





def update_screen(ai_settings,screen,scientist,cure):

    screen.fill(ai_settings.bg_color)

    #ai_settings stands for the Settings() class' instance

    scientist.blitme()

    for vaccine in cure.sprites():
        vaccine.draw_cure()

    pygame.display.flip()

def update_cure(cure):

    cure.update()

    for vaccine in cure.copy():
        if vaccine.rect.bottom <= 0:
            cure.remove(vaccine)


def fire_cure(ai_settings,screen,scientist,cure):

    if len(cure) < ai_settings.cure_allowed:  # limiting the number of projectiles

        new_cure = Cure(ai_settings, screen, scientist)

        cure.add(new_cure)
