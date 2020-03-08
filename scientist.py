
import pygame

#Building the hero of our game

class Scientist():

    def __init__(self,ai_settings,screen):

        self.screen=screen
        self.ai_settings=ai_settings

        #loading the scientist
        self.image=pygame.image.load("Covid_scientist.bmp")
        self.image_rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new scientist in the bottom center of the screen
        self.image_rect.centerx=self.screen_rect.centerx
        self.image_rect.bottom=self.screen_rect.bottom


        #storing a decimal value to the scientist's center, because the centerx function only holds integer values
        self.center=float(self.image_rect.centerx)
        self.centery=float(self.image_rect.bottom)


        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    def blitme(self):
        #drawn the scientist at its current location
        self.screen.blit(self.image,self.image_rect)

    def update(self):#this function updates th position of the scientist

        if self.moving_right==True:
            if self.moving_right and self.image_rect.right < self.screen_rect.right:
                #limiting the right corner

                self.center+=self.ai_settings.scientist_speed

        if self.moving_left==True:
#it's better to use an if in both cases, because the user can press two buttons at the same time
            if self.moving_left and self.image_rect.left > 0:
                #limiting the left corner

                self.center-=self.ai_settings.scientist_speed

        if self.moving_down==True:

            if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:

                self.centery += self.ai_settings.scientist_speed


        if self.moving_up==True:

            if self.moving_up and self.image_rect.bottom > 150:

                self.centery -= self.ai_settings.scientist_speed


        self.image_rect.bottom = self.centery
        self.image_rect.centerx = self.center

        #update the rect object from self.center





