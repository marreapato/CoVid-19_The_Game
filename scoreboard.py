import pygame.font

class Scoreboard():

    def __init__(self,ai_settings,screen,stats):

        self.ai_settings=ai_settings

        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.stats=stats

        #font settings for scoring info

        self.text_colour=(30,30,30)

        self.font=pygame.font.SysFont(None,48)

        #prepare the initial score image
        self.prep_score()

    def prep_score(self):

        rounded_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)
        
        self.score_image=self.font.render(score_str,True,self.text_colour,self.ai_settings.bg_color)

        #display the score at the top right of the screen

        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.screen_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)

