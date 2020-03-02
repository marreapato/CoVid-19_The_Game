import sys

import pygame

def events():

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
