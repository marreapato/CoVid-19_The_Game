import sys

import pygame

#the funtion is supposed to initialize the game, create a screen object and watch for the events

def run_game():

    pygame.init()

    screen=pygame.display.set_mode((1200,800))#uses a tuple to set the dimensions

    pygame.display.set_caption("Covid19 The Game")

    #main loop for the game

    while True:

        #watching for the events
        for event in pygame.event.get():

            if event.type==pygame.QUIT:

                sys.exit()

            #Drawn the mostly recent screen
            pygame.display.flip()


run_game()
