import sys

import pygame

from cure import Cure

from coronavirus import Covid_19

import time
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

    elif event.key==pygame.K_q:

        sys.exit()


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





def update_screen(ai_settings,screen,scientist,viruses,cure):

    screen.fill(ai_settings.bg_color)

    #ai_settings stands for the Settings() class' instance

    scientist.blitme()
    viruses.draw(screen)

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


def create_fleet(ai_settings,screen,scientist,viruses):
    #create a virus and find the number of viruses in a row

    covid = Covid_19(ai_settings, screen)

    number_viruses_x=get_number_viruses_x(ai_settings,covid.rect.width)

    number_rows = get_number_rows(ai_settings, scientist.image_rect.height, covid.rect.height)

    #create the first row of viruses
    for row_number in range(0,number_rows):
        for number_virus in range(0,number_viruses_x):
            create_virus(ai_settings,screen,viruses,number_virus,row_number)


def get_number_viruses_x(ai_settings,covid_width):
    # spacing between each virus is equal to one virus width
    available_space_x = ai_settings.screen_width - (2 * covid_width)

    # number of viruses in the screen

    number_viruses_x = int(available_space_x / (2 * covid_width))

    return number_viruses_x

def create_virus(ai_settings,screen,viruses,number_virus,row_number):
    # creates a virus and places it in the row
    covid = Covid_19(ai_settings, screen)
    covid_width = covid.rect.width
    covid.x = covid_width + 2 * covid_width * number_virus
    covid.rect.x = covid.x
    covid.rect.y=covid.rect.height+2*covid.rect.height*row_number
    # adding to the group
    viruses.add(covid)


def get_number_rows(ai_settings,scientist_height,covid_height):

    available_space_y=(ai_settings.screen_height-(3*covid_height)-scientist_height)

    number_rows=int(available_space_y/(2*covid_height))

    return number_rows

def update_viruses(ai_settings,covid):
    check_fleet_edges(ai_settings,covid)
    covid.update()

#changing the direction of the virus fleet

def change_fleet_direction(ai_settings,covid):
    for virus in covid.sprites():
        virus.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1


def check_fleet_edges(ai_settings,covid):

    for virus in covid.sprites():
        if virus.check_edges()==True:
            change_fleet_direction(ai_settings,covid)
            break


