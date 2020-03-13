import pygame

from pygame.sprite import Sprite

class Cure(Sprite):
    def __init__(self,ai_settings,screen,scientist):

        super().__init__()
        self.screen=screen

        #creates a cure in (0,0) an then set the correct position

        self.rect=pygame.Rect(0,0,ai_settings.cure_width,ai_settings.cure_height)
        self.rect.centerx=scientist.image_rect.centerx
        self.rect.top=scientist.image_rect.top

        #storing the cure's position as a decimal value

        self.y=float(self.rect.y)

        self.color=ai_settings.cure_color

        self.speed_factor=ai_settings.cure_speed_factor

#adding the update method later

