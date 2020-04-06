import pygame.font

class Button():

    def __init__(self,ai_settings,screen,msg):

        self.screen=screen
        self.screen_rect=screen.get_rect()

        #setting the dimensions and properties of the button

        self.width,self.height=200,50
        self.button_colour=(0,255,0)
        self.text_colour=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        #button's rect

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #the button message

        self.prep_msg(msg)
