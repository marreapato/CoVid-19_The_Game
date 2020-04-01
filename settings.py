class Settings():

    #Class made with the purpose of storing all the settings of the game

    def __init__(self):

        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(100,10,0)
        self.scientist_speed=1.5


        #Creating the cure

        self.cure_speed_factor=3
        self.cure_width=3
        self.cure_height=15
        self.cure_color=(0,100,50)
        self.cure_allowed=3

        #virus settings

        self.corona_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1
        #1 represents right and -1 represents left
