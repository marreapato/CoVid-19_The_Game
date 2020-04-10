import pygame

from pygame.sprite import Sprite

class Cure(Sprite):

    def __init__(self,ai_settings,screen,scientist):

        super().__init__()

        self.screen=screen

        #creates a cure in (0,0) an then set the correct position

        self.rect=pygame.Rect(0,0,ai_settings.cure_width,ai_settings.cure_height)
        self.rect.centerx=scientist.rect.centerx
        self.rect.top=scientist.rect.top

        #storing the cure's position as a decimal value

        self.y=float(self.rect.y)

        self.color=ai_settings.cure_color

        self.speed_factor=ai_settings.cure_speed_factor


    def update(self):

        #updates the decimal pos for the cure
        self.y -= self.speed_factor

        #update the rect position

        self.rect.y=self.y


    def draw_cure(self):


        pygame.draw.rect(self.screen,self.color,self.rect)

