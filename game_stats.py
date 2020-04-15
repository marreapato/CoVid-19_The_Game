class Games_stats():

    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False



    def reset_stats(self):
        self.scientist_left=self.ai_settings.scientist_limit
        self.score=0
