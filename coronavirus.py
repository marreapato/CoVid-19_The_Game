import pygame

from pygame.sprite import Sprite

class Covid_19(Sprite):



    def __init__(self,ai_settings,screen):

        super(Covid_19,self). __init__()

        self.ai_settings=ai_settings
        self.screen=screen

        #loading the virus and setting its rect
        self.image=pygame.image.load("Covid_19.bmp")
        self.rect=self.image.get_rect()

        #choosing the top left side of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store the virus' position
        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)



