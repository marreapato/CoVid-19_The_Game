
import pygame
from pygame.sprite import Sprite

#Building the hero of our game

class Scientist(Sprite):

    def __init__(self,ai_settings,screen):

        super(Scientist,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #loading the scientist
        self.image=pygame.image.load("Covid_scientist.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new scientist in the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom


        #storing a decimal value to the scientist's center, because the centerx function only holds integer values
        self.center=float(self.rect.centerx)
        self.centery=float(self.rect.bottom)


        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def blitme(self):

        #drawn the scientist at its current location

        self.screen.blit(self.image,self.rect)

    def update(self):#this function updates th position of the scientist

        if self.moving_right==True:

            if self.moving_right and self.rect.right < self.screen_rect.right:

                #limiting the right corner

                self.center+=self.ai_settings.scientist_speed

        if self.moving_left==True:

            #it's better to use an if in both cases, because the user can press two buttons at the same time

            if self.moving_left and self.rect.left > 0:

                #limiting the left corner

                self.center-=self.ai_settings.scientist_speed

        if self.moving_down==True:

            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:

                self.centery += self.ai_settings.scientist_speed


        if self.moving_up==True:

            if self.moving_up and self.rect.bottom > 150:

                self.centery -= self.ai_settings.scientist_speed


        self.rect.bottom = self.centery
        self.rect.centerx = self.center

        #update the rect object from self.center

    def center_scientist(self):
        #placing him in the center
        self.center=self.screen_rect.centerx
        self.centery=self.screen_rect.bottom




