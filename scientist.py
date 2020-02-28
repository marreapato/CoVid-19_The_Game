
import pygame

#Building the hero of our game

class Scientist():
    def __init__(self,screen):

        self.screen=screen

        #loading the scientist
        self.image=pygame.image.load("Covid_Scientist.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new scientist in the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

    def blitme(self):
        #drawn the scientist at its current location
        self.screen.blit(self.image,self.rect)

