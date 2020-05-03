class Settings():

    #Class made with the purpose of storing all the settings of the game

    def __init__(self):

        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(100,10,0)

        self.scientist_limit=3


        #Creating the cure


        self.cure_width=3
        self.cure_height=15
        self.cure_color=(0,100,50)
        self.cure_allowed=3

        #virus settings


        self.fleet_drop_speed=10


        #speeding up the game
        self.speedup_scale=1.1

        #how quick the virus' point value increases
        self.score_scale=1.5

        self.initialize_dinamic_settings()

    def initialize_dinamic_settings(self):

        self.scientist_speed=1.5
        self.cure_speed_factor=3
        self.corona_speed_factor=1

        #1 represents right and -1 represents left
        self.fleet_direction=1

        #scoring system
        self.virus_points=50

    def increase_speed(self):

        self.scientist_speed*=self.speedup_scale
        self.corona_speed_factor*=self.speedup_scale
        self.cure_speed_factor*=self.speedup_scale

        self.virus_points=int(self.virus_points*self.score_scale)#increasing the score as the game speeds up


 
