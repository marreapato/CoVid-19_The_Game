import pygame.font
from pygame.sprite import Group

from scientist import Scientist

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
        self.prep_high_score()
        self.prep_level()
        self.prep_scientists()

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
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)

        #draw the number of scientists left
        self.scientists.draw(self.screen)

    def prep_high_score(self):

        high_score=int(round(self.stats.high_score,-1))
        high_score_str="Highscore: "+"{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_colour,self.ai_settings.bg_color)

        #centering the high score on the top of the screen
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top


    def prep_level(self):

        level=int(self.stats.level)
        level_str="Level: "+format(level)

        self.level_image=self.font.render(level_str,True,self.text_colour,self.ai_settings.bg_color)

        #positioning the level below the score

        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10


    def prep_scientists(self):

        self.scientists=Group()

        for scientist_number in range(self.stats.scientist_left):

            scientist=Scientist(self.ai_settings,self.screen)
            scientist.rect.x=10+scientist_number*scientist.rect.width
            scientist.rect.y=10
            self.scientists.add(scientist)

